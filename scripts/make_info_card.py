def generate_neofetch_svg(output_path="info-card.svg"):
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
    height = 250
    line_height = 24
    
    svg_rows = ""
    for i, (key, value) in enumerate(info):
        y = 65 + (i * line_height)
        svg_rows += f'<text font-family="monospace" font-size="13" fill="#58a6ff" font-weight="bold" x="20" y="{y}">{key}:</text><text font-family="monospace" font-size="13" fill="#c9d1d9" x="110" y="{y}">{value}</text>'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d"/>
  <text font-family="monospace" font-size="13" font-weight="bold" fill="#7ee787" x="20" y="30">vaibhav@github</text>
  <text font-family="monospace" font-size="13" fill="#484f58" x="20" y="42">-----------------------------------</text>
  {svg_rows}
</svg>'''

    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Info card regenerated successfully at {output_path}")

if __name__ == "__main__":
    generate_neofetch_svg()
