# Let's inspect pages to see which perspective they show
# We can make contact sheets (collages) of 9 images each: 
# 1-9, 10-18, 19-27, 28-36, 37-46
from PIL import Image
import os

img_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\hstk_3d_images"
collage_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\hstk_collages"
os.makedirs(collage_dir, exist_ok=True)

# Generate 5 collage sheets
batches = [
    (1, 9, "collage_1_9.jpg"),
    (10, 18, "collage_10_18.jpg"),
    (19, 27, "collage_19_27.jpg"),
    (28, 36, "collage_28_36.jpg"),
    (37, 46, "collage_37_46.jpg"),
]

for start_p, end_p, name in batches:
    images = []
    for p in range(start_p, end_p + 1):
        f = os.path.join(img_dir, f"page_{p:02d}.jpg")
        if os.path.exists(f):
            im = Image.open(f).resize((432, 270)) # 1/3 scale
            images.append((p, im))
    
    # Grid 3x3 (or 3x4)
    cols = 3
    rows = (len(images) + cols - 1) // cols
    collage = Image.new('RGB', (cols * 432, rows * 270), (255, 255, 255))
    
    for idx, (p_num, img) in enumerate(images):
        r = idx // cols
        c = idx % cols
        collage.paste(img, (c * 432, r * 270))
        
    out_path = os.path.join(collage_dir, name)
    collage.save(out_path, quality=85)
    print(f"Saved {out_path}")
