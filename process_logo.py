from PIL import Image
import numpy as np
import os
import base64

# Use the existing logo file
inp = "img/logo.PNG"
if not os.path.exists(inp):
    print(f"Error: {inp} not found!")
    exit(1)

img = Image.open(inp).convert("RGBA")
arr = np.array(img)

# Make near-white pixels transparent
rgb = arr[..., :3]
alpha = arr[..., 3]
mask = (rgb > 245).all(axis=-1)  # adjust threshold
arr[..., 3] = np.where(mask, 0, alpha)

# Crop to content (non-transparent)
alpha2 = arr[..., 3]
ys, xs = np.where(alpha2 > 0)
if len(ys) == 0 or len(xs) == 0:
    print("Error: No content found after processing!")
    exit(1)
    
y0, y1 = ys.min(), ys.max()
x0, x1 = xs.min(), xs.max()
cropped = Image.fromarray(arr).crop((x0, y0, x1+1, y1+1))

# Add padding
pad = 80
w, h = cropped.size
canvas = Image.new("RGBA", (w+pad*2, h+pad*2), (0,0,0,0))
canvas.paste(cropped, (pad, pad))

# Upscale to big header-friendly width (e.g., 3200px wide)
target_w = 3200
scale = target_w / canvas.size[0]
target_h = int(canvas.size[1] * scale)
big = canvas.resize((target_w, target_h), Image.LANCZOS)

out_png = "img/primefixusa_logo_transparent_3200w.png"
big.save(out_png)
print(f"Saved PNG: {out_png}")

# Create SVG wrapper embedding the PNG (still raster but scales in layout)
with open(out_png, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("ascii")
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{target_w}" height="{target_h}" viewBox="0 0 {target_w} {target_h}">
  <image href="data:image/png;base64,{b64}" x="0" y="0" width="{target_w}" height="{target_h}" />
</svg>'''
out_svg = "img/primefixusa_logo_transparent_embedded.svg"
with open(out_svg, "w") as f:
    f.write(svg)

print(f"Saved SVG: {out_svg}")
print("Logo processing complete!")
