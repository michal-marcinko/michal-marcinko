import sys, pathlib
# Regenerates assets/header-{dark,light}.svg. Usage: python3 scripts/gen_header.py assets
out = pathlib.Path(sys.argv[1])

PALETTES = {
    "dark": dict(bg="#0d1117", border="#30363d", grid="#ffffff", grid_o="0.05", fg="#e6edf3", muted="#7d8590",
                 e1="#ff6b35", e2="#ffb627", teal="#5eead4", term="#161b22", glow_o="0.22"),
    "light": dict(bg="#ffffff", border="#d0d7de", grid="#1f2328", grid_o="0.05", fg="#1f2328", muted="#59636e",
                  e1="#d9480f", e2="#e67700", teal="#0f766e", term="#f6f8fa", glow_o="0.14"),
}

PHRASES = ["fast Rust tools", "Solana programs", "edge AI on NVIDIA Jetson", "full-stack TypeScript apps"]

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340" role="img" aria-labelledby="t">
  <title id="t">Michal Marcinko. I build fast Rust tools, Solana programs, edge AI on NVIDIA Jetson and full-stack TypeScript apps.</title>
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="{grid}" stroke-opacity="{grid_o}" stroke-width="1"/>
    </pattern>
    <radialGradient id="fade" cx="35%" cy="40%" r="75%">
      <stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
    </radialGradient>
    <mask id="gridmask"><rect width="1200" height="340" fill="url(#fade)"/></mask>
    <radialGradient id="glowA"><stop offset="0" stop-color="{e1}" stop-opacity="{glow_o}"/><stop offset="1" stop-color="{e1}" stop-opacity="0"/></radialGradient>
    <radialGradient id="glowB"><stop offset="0" stop-color="{teal}" stop-opacity="{glow_o}"/><stop offset="1" stop-color="{teal}" stop-opacity="0"/></radialGradient>
    <linearGradient id="ember" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox" spreadMethod="reflect">
      <stop offset="0" stop-color="{e1}"/><stop offset="0.5" stop-color="{e2}"/><stop offset="1" stop-color="{e1}"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="2 0" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
    <clipPath id="card"><rect width="1200" height="340" rx="18"/></clipPath>
  </defs>
  <style>
    .sans {{ font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
    .fg {{ fill: {fg}; }} .muted {{ fill: {muted}; }} .e1 {{ fill: {e1}; }} .teal {{ fill: {teal}; }}
    .l {{ white-space: pre; }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .glow {{ animation: drift 14s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }}
    @keyframes drift {{ to {{ transform: translate(40px, 18px) scale(1.12); }} }}
    .p {{ opacity: 0; animation: rot 12s infinite both; }}
    .p0 {{ opacity: 1; }}
    .p1 {{ animation-delay: 3s; }} .p2 {{ animation-delay: 6s; }} .p3 {{ animation-delay: 9s; }}
    @keyframes rot {{
      0% {{ opacity: 0; transform: translateY(10px); }}
      3%, 22% {{ opacity: 1; transform: translateY(0); }}
      25%, 100% {{ opacity: 0; transform: translateY(-10px); }}
    }}
{line_css}
    @media (prefers-reduced-motion: reduce) {{
      .cursor, .glow, .p, .l {{ animation: none !important; }}
    }}
  </style>
  <g clip-path="url(#card)">
    <rect width="1200" height="340" fill="{bg}"/>
    <rect width="1200" height="340" fill="url(#grid)" mask="url(#gridmask)"/>
    <ellipse class="glow" cx="260" cy="110" rx="420" ry="230" fill="url(#glowA)"/>
    <ellipse class="glow" cx="1000" cy="300" rx="380" ry="200" fill="url(#glowB)" style="animation-duration:18s"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="339" rx="18" fill="none" stroke="{border}"/>

  <text x="64" y="92" class="mono" font-size="18"><tspan class="teal">❯</tspan><tspan class="muted"> whoami</tspan><tspan class="e1 cursor"> ▍</tspan></text>
  <text x="62" y="172" class="sans" font-size="68" font-weight="800" letter-spacing="-2" fill="url(#ember)">Michal Marcinko</text>
  <g class="sans" font-size="26" font-weight="500">
{phrases}
  </g>
  <text x="64" y="282" class="mono muted" font-size="15" letter-spacing="0.5">rust · typescript · python · c# · solana · cuda</text>

  <g transform="translate(784 70)">
    <rect width="352" height="200" rx="12" fill="{term}" stroke="{border}"/>
    <circle cx="22" cy="22" r="6" fill="#ff5f57"/><circle cx="42" cy="22" r="6" fill="#febc2e"/><circle cx="62" cy="22" r="6" fill="#28c840"/>
    <text x="176" y="27" text-anchor="middle" class="mono muted" font-size="13">fastlaunch</text>
    <g class="mono" font-size="16" xml:space="preserve">
{lines}
    </g>
  </g>
</svg>
"""

LINES = [
    '<tspan class="teal">$</tspan><tspan class="fg"> fastlaunch</tspan>',
    '<tspan class="muted">  scanning steam … </tspan><tspan class="teal">ok</tspan>',
    '<tspan class="muted">  scanning epic  … </tspan><tspan class="teal">ok</tspan>',
    '<tspan class="muted">  </tspan><tspan class="fg">ready in </tspan><tspan class="e1" font-weight="700">0.17s</tspan>',
]

def build(p):
    phrases = "\n".join(
        f'    <text x="64" y="226" class="p p{i}"><tspan class="fg">I build </tspan><tspan class="e1">{t}</tspan><tspan class="fg">.</tspan></text>'
        for i, t in enumerate(PHRASES))
    lines = "\n".join(f'      <text x="22" y="{70 + i * 32}" class="l l{i}">{l}</text>' for i, l in enumerate(LINES))
    # each line appears in turn, all hold, then fade together; 8s loop
    line_css = []
    for i in range(len(LINES)):
        start = 6 + i * 12
        line_css.append(f"    .l{i} {{ animation: l{i} 8s infinite; }}\n"
                        f"    @keyframes l{i} {{ 0%, {start}% {{ opacity: 0; }} {start + 2}%, 88% {{ opacity: 1; }} 96%, 100% {{ opacity: 0; }} }}")
    return TEMPLATE.format(phrases=phrases, lines=lines, line_css="\n".join(line_css), **p)

for name, p in PALETTES.items():
    (out / f"header-{name}.svg").write_text(build(p))
print("ok")
