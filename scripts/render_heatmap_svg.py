import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_svg():
    with open("data/contributions.json") as f:
        data = json.load(f)
        
    box_size = 11
    box_gap = 3
    width = 860
    height = 160
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .rect-box {{
      animation: slideIn 0.3s ease-out forwards;
      opacity: 0;
    }}
    @keyframes slideIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    .text {{ font-family: monospace; font-size: 12px; fill: #8b949e; }}
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" />
  <g transform="translate(20, 25)">
'''
    
    for i, day in enumerate(data):
        week = i // 7
        day_of_week = i % 7
        
        x = week * (box_size + box_gap)
        y = day_of_week * (box_size + box_gap)
        color = PALETTE[min(day["level"], 5)]
        delay = (week + day_of_week) * 0.01
        
        svg += f'''
    <rect class="rect-box" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" style="animation-delay: {delay:.2f}s;" />
'''
        
    svg += '''
    <text class="text" x="0" y="115">Vaibhavgithub21 Contribution Activity</text>
  </g>
</svg>'''

    with open("contrib-heatmap.svg", "w") as f:
        f.write(svg)
    print("Generated contrib-heatmap.svg")

if __name__ == "__main__":
    render_svg()
