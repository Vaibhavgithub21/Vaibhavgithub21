import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def process_photo(input_path, output_path="source-prepped.png"):
    inp = Image.open(input_path)
    out = remove(inp)  # Remove background
    
    img_np = np.array(out)
    alpha = img_np[:, :, 3]
    rgb = img_np[:, :, :3]
    
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    # Enhance face contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    # Composite onto pure white background
    white_bg = np.ones_like(enhanced) * 255
    result = np.where(alpha > 0, enhanced, white_bg)
    
    cv2.imwrite(output_path, result)
    print(f"Prepped photo saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py <photo_path>")
        sys.exit(1)
    process_photo(sys.argv[1])
