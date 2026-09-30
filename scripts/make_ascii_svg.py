import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"
GRID_WIDTH = 100

def image_to_ascii(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    aspect_ratio = h / w
    grid_height = int(GRID_WIDTH * aspect_ratio * 0.55)
    
    resized = cv2.resize(img, (GRID_WIDTH, grid_height))
    
    ascii_lines = []
    for row in resized:
        line = ""
        for val in row:
            idx = int((val / 255.0) * (len(RAMP) - 1))
            line += RAMP[idx]
        ascii_lines.append(line)
    return ascii_lines

def build_svg(ascii_lines, output_path="avi-ascii.svg"):
    font_size = 10
    char_width = 6
    line_height = 11
    
    width = GRID_WIDTH * char_width + 20
    height = len(ascii_lines) * line_height + 20
    
    svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .ascii {{ font-family: monospace; font-size: {font_size}px; fill: #8b949e; white-space: pre; }}
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="6" />
  <g transform="translate(10, 15)">
'''
    
    svg_body = ""
    row_duration = 0.05
    
    for i, line in enumerate(ascii_lines):
        y_pos = i * line_height
        delay = i * row_duration
        clip_id = f"clip_{i}"
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        svg_body += f'''
    <clipPath id="{clip_id}">
      <rect x="0" y="{y_pos - 8}" width="0" height="{line_height}">
        <animate attributeName="width" from="0" to="{width}" begin="{delay:.2f}s" dur="{row_duration:.2f}s" fill="freeze" />
      </rect>
    </clipPath>
    <text x="0" y="{y_pos}" class="ascii" clip-path="url(#{clip_id})">{escaped_line}</text>
'''

    svg_footer = '''  </g>
</svg>'''

    with open(output_path, "w") as f:
        f.write(svg_header + svg_body + svg_footer)
    print(f"ASCII SVG generated at {output_path}")

if __name__ == "__main__":
    lines = image_to_ascii("source-prepped.png")
    build_svg(lines)
