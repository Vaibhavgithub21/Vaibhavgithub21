import os

def generate_neofetch_svg(output_path="info-card.svg"):
    is_static = os.getenv("STATIC") == "1"
    
    info = [
        ("User", "Vaibhavgithub21"),
        ("OS", "GitHub Profile OS x86_64"),
        ("Host", "Developer Workspace"),
        ("Shell", "zsh 5.8"),
        ("Stack", "Python, JavaScript, Git"),
        ("Focus", "Web Development & Automation"),
        ("Status", "Building cool profile READMEs")
    ]
    
    width = 490
    height = 280
    line_height = 24
    
    svg_rows = ""
    for i, (key, value) in enumerate(info):
        y = 65 + (i * line_height)
        delay = 0.2 + (i * 0.1)
        anim_style = f"animation: fadeIn 0.4s ease-in-out {delay:.2f}s forwards; opacity: 0;" if not is_static else ""
        
        svg_rows += f'''
    <g style="{anim_style}">
      <text class="text key" x="20" y="{y}">{key}:</text>
      <text class="text" x="110" y="{y}">{value}</text>
    </g>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .text {{ font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace; font-size: 13px; fill: #c9d1d9; }}
    .key {{ fill: #58a6ff; font-weight: 600; }}
    .title {{ fill: #7ee787; font-weight: 700; }}
    .separator {{ fill: #484f58; }}
    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" />
  <text class="text title" x="20" y="30">vaibhav@github</text>
  <text class="text separator" x="20" y="42">-----------------------------------</text>
  {svg_rows}
</svg>'''

    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Info card re-generated clean at {output_path}")

if __name__ == "__main__":
    generate_neofetch_svg()
