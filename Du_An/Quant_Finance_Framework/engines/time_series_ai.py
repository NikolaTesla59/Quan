import torch
import torch.nn as nn
import numpy as np

class TemporalAttention(nn.Module):
    """Multi-Head Temporal Self-Attention layer for Financial Time Series."""
    def __init__(self, hidden_dim: int, num_heads: int = 4):
        super().__init__()
        self.mha = nn.MultiheadAttention(embed_dim=hidden_dim, num_heads=num_heads, batch_first=True)
        self.norm = nn.LayerNorm(hidden_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        attn_out, _ = self.mha(x, x, x)
        return self.norm(x + attn_out)

class FinancialBiLSTMAttention(nn.Module):
    """
    Bi-directional LSTM with Multi-Head Attention for stock price / volatility forecasting.
    Input: [Batch, Sequence_Length, Features]
    Output: Forecasted next period return & directional probability.
    """
    def __init__(self, input_dim: int = 5, hidden_dim: int = 64, num_layers: int = 2, dropout: float = 0.2):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            bidirectional=True,
            dropout=dropout if num_layers > 1 else 0.0
        )
        self.attention = TemporalAttention(hidden_dim * 2, num_heads=4)
        self.fc = nn.Sequential(
            nn.Linear(hidden_dim * 2, 32),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(32, 1)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        lstm_out, _ = self.lstm(x)             # [Batch, Seq_Len, hidden_dim * 2]
        attn_out = self.attention(lstm_out)    # [Batch, Seq_Len, hidden_dim * 2]
        context = torch.mean(attn_out, dim=1)  # Global Average Pooling over time
        out = self.fc(context)                 # [Batch, 1]
        return out

def train_mini_ai_model(n_samples: int = 200, seq_len: int = 30, n_features: int = 5, epochs: int = 5) -> dict:
    """Trains a rapid sample model to return prediction metrics and losses."""
    np.random.seed(42)
    torch.manual_seed(42)

    X_data = np.random.randn(n_samples, seq_len, n_features).astype(np.float32)
    # Target: Next period return (with autoregressive momentum)
    y_data = (0.4 * X_data[:, -1, 0] - 0.2 * X_data[:, -5, 0] + np.random.randn(n_samples) * 0.1).astype(np.float32).reshape(-1, 1)

    X_tensor = torch.tensor(X_data)
    y_tensor = torch.tensor(y_data)

    model = FinancialBiLSTMAttention(input_dim=n_features, hidden_dim=32, num_layers=2)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    losses = []
    model.train()
    for ep in range(epochs):
        optimizer.zero_grad()
        preds = model(X_tensor)
        loss = criterion(preds, y_tensor)
        loss.backward()
        optimizer.step()
        losses.append(float(loss.item()))

    model.eval()
    with torch.no_grad():
        test_preds = model(X_tensor[:10]).numpy().flatten()
        actuals = y_tensor[:10].numpy().flatten()

    return {
        'epochs': list(range(1, epochs + 1)),
        'losses': [round(l, 4) for l in losses],
        'sample_actual': [round(float(a), 4) for a in actuals],
        'sample_pred': [round(float(p), 4) for p in test_preds],
        'directional_accuracy': round(float(np.mean(np.sign(test_preds) == np.sign(actuals)) * 100), 2)
    }
