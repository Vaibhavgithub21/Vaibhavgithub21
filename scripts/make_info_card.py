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
    height = 300
    line_height = 22
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .text {{ font-family: monospace; font-size: 13px; fill: #c9d1d9; }}
    .key {{ fill: #58a6ff; font-weight: bold; }}
    .title {{ fill: #7ee787; font-weight: bold; }}
    .separator {{ fill: #484f58; }}
    .fade-in {{
      opacity: {1 if is_static else 0};
      animation: fadeIn 0.4s ease-in-out forwards;
    }}
    @keyframes fadeIn {{
      to {{ opacity: 1; }}
    }}
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" />
  <g transform="translate(20, 30)">
    <text class="text title" x="0" y="0">vaibhav@github</text>
    <text class="text separator" x="0" y="12">-----------------------------------</text>
'''
    
    for i, (key, value) in enumerate(info):
        y = 35 + (i * line_height)
        delay = 0.2 + (i * 0.1)
        style_attr = "" if is_static else f'style="animation-delay: {delay:.2f}s;"'
        
        svg += f'''
    <g class="fade-in" {style_attr}>
      <text class="text key" x="0" y="{y}">{key}:</text>
      <text class="text" x="90" y="{y}">{value}</text>
    </g>
'''

    svg += '''  </g>
</svg>'''

    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Info card generated at {output_path}")

if __name__ == "__main__":
    generate_neofetch_svg()
