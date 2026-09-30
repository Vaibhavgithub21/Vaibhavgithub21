def generate_wordmark_svg(output_path="wordmark.svg"):
    width = 490
    height = 370
    
    # Precise 3D ASCII Block font for "VAIBHAV VIJAY" (V - I - J - A - Y)
    ascii_banner = [
        "██╗   ██╗ █████╗ ██╗██████╗ ██╗  ██╗ █████╗ ██╗   ██╗       ██╗   ██╗██╗  ██████╗  █████╗ ██╗   ██╗",
        "██║   ██║██╔══██╗██║██╔══██╗██║  ██║██╔══██╗██║   ██║       ██║   ██║██║  ╚══██╔╝ ██╔══██╗╚██╗ ██╔╝",
        "██║   ██║███████║██║██████╔╝███████║███████║██║   ██║       ██║   ██║██║     ██║  ███████║ ╚████╔╝ ",
        "╚██╗ ██╔╝██╔══██║██║██╔══██╗██╔══██║██╔══██║╚██╗ ██╔╝       ╚██╗ ██╔╝██║  ██ ██║  ██╔══██║  ╚██╔╝  ",
        " ╚████╔╝ ██║  ██║██║██████╔╝██║  ██║██║  ██║ ╚████╔╝         ╚████╔╝ ██║  ╚████╔╝ ██║  ██║   ██║   ",
        "  ╚═══╝  ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝           ╚═══╝  ╚═╝   ╚═══╝  ╚═╝  ╚═╝   ╚═╝   "
    ]
    
    font_size = 4.8
    line_height = 8.5
    start_y = 155
    start_x = 12
    
    text_lines = ""
    for i, line in enumerate(ascii_banner):
        y = start_y + (i * line_height)
        text_lines += f"<text x=\"{start_x}\" y=\"{y}\" class=\"ascii\">{line}</text>\n"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .ascii {{ 
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; 
      font-size: {font_size}px; 
      fill: #ff1010; 
      font-weight: bold; 
      white-space: pre;
    }}
    .title {{ 
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; 
      font-size: 12px; 
      fill: #8b949e; 
      text-anchor: middle;
    }}
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" />
  <circle cx="20" cy="18" r="5" fill="#ff5f56" />
  <circle cx="35" cy="18" r="5" fill="#ffbd2e" />
  <circle cx="50" cy="18" r="5" fill="#27c93f" />
  <text x="245" y="22" class="title">vaibhav@github: ~ $ ./wordmark.sh --3d</text>
  <line x1="0" y1="36" x2="{width}" y2="36" stroke="#21262d" stroke-width="1" />
  <g>
    {text_lines}
  </g>
</svg>"""

    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated wordmark SVG with complete J character for VAIBHAV VIJAY at {output_path}")

if __name__ == "__main__":
    generate_wordmark_svg()
