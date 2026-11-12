import torch
import torch.nn as nn
import numpy as np

class TemporalAttentionBlock(nn.Module):
    def __init__(self, dim: int, heads: int = 4):
        super().__init__()
        self.mha = nn.MultiheadAttention(embed_dim=dim, num_heads=heads, batch_first=True)
        self.norm = nn.LayerNorm(dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        attn, _ = self.mha(x, x, x)
        return self.norm(x + attn)

class DeepFinancialForecaster(nn.Module):
    def __init__(self, in_features: int = 5, hidden_dim: int = 32):
        super().__init__()
        self.lstm = nn.LSTM(in_features, hidden_dim, num_layers=2, batch_first=True, bidirectional=True)
        self.attn = TemporalAttentionBlock(hidden_dim * 2, heads=4)
        self.head = nn.Sequential(
            nn.Linear(hidden_dim * 2, 32),
            nn.GELU(),
            nn.Linear(32, 1)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.lstm(x)
        out = self.attn(out)
        pooled = torch.mean(out, dim=1)
        return self.head(pooled)

def run_ai_training(epochs: int = 8) -> dict:
    np.random.seed(42)
    torch.manual_seed(42)
    X = np.random.randn(150, 20, 5).astype(np.float32)
    y = (0.35 * X[:, -1, 0] - 0.2 * X[:, -4, 0] + np.random.randn(150) * 0.1).astype(np.float32).reshape(-1, 1)

    X_t = torch.tensor(X)
    y_t = torch.tensor(y)

    model = DeepFinancialForecaster()
    opt = torch.optim.AdamW(model.parameters(), lr=0.01, weight_decay=1e-4)
    loss_fn = nn.MSELoss()

    history = []
    for _ in range(epochs):
        opt.zero_grad()
        p = model(X_t)
        l = loss_fn(p, y_t)
        l.backward()
        opt.step()
        history.append(float(l.item()))

    with torch.no_grad():
        preds = model(X_t[:10]).numpy().flatten()
        actual = y_t[:10].numpy().flatten()

    acc = float(np.mean(np.sign(preds) == np.sign(actual)) * 100.0)
    return {
        'losses': [round(x, 4) for x in history],
        'actual': [round(float(a), 4) for a in actual],
        'pred': [round(float(p), 4) for p in preds],
        'acc': round(acc, 1)
    }
