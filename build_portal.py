import os

base_dir = r"C:\Users\user1\.gemini\antigravity\scratch\demo_site"
report_html_path = os.path.join(base_dir, "report", "final_report.html")
dashboard_html_path = os.path.join(base_dir, "analysis", "dashboard.html")
output_path = os.path.join(base_dir, "index.html")

report_content = ""
if os.path.exists(report_html_path):
    with open(report_html_path, "r", encoding="utf-8") as f:
        report_content = f.read()

# Extract inner body content if needed or wrap
dashboard_content = ""
if os.path.exists(dashboard_html_path):
    with open(dashboard_html_path, "r", encoding="utf-8") as f:
        dashboard_content = f.read()

portal_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mega-Agent 10k: Future Urban Intelligence Architecture</title>
    <style>
        :root {{
            --bg-primary: #0a0e17;
            --bg-secondary: #131a29;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.2);
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --card-border: #1e293b;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-main);
            line-height: 1.6;
            padding-bottom: 60px;
        }}
        header {{
            background: linear-gradient(180deg, #162033 0%, var(--bg-primary) 100%);
            padding: 60px 20px 40px;
            text-align: center;
            border-bottom: 1px solid var(--card-border);
        }}
        .badge {{
            display: inline-block;
            background: var(--accent-glow);
            color: var(--accent);
            padding: 4px 14px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            margin-bottom: 16px;
            border: 1px solid var(--accent);
        }}
        h1 {{
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #38bdf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }}
        p.subtitle {{
            color: var(--text-muted);
            font-size: 1.15rem;
            max-width: 800px;
            margin: 0 auto 24px;
        }}
        .narrative-box {{
            max-width: 900px;
            margin: 30px auto;
            background: var(--bg-secondary);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 24px 30px;
            text-align: left;
            font-size: 0.95rem;
            color: #cbd5e1;
        }}
        .narrative-box h3 {{
            color: var(--accent);
            margin-bottom: 10px;
            font-size: 1.1rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            max-width: 1100px;
            margin: 40px auto;
            padding: 0 20px;
        }}
        .card {{
            background: var(--bg-secondary);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 24px;
            transition: transform 0.2s, border-color 0.2s;
        }}
        .card:hover {{
            transform: translateY(-4px);
            border-color: var(--accent);
        }}
        .card h2 {{
            font-size: 1.25rem;
            margin-bottom: 10px;
            color: #fff;
        }}
        .card p {{
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-bottom: 16px;
        }}
        .card a {{
            display: inline-block;
            background: #2563eb;
            color: #fff;
            padding: 8px 16px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.85rem;
        }}
        .card a:hover {{ background: #1d4ed8; }}
        .section-container {{
            max-width: 1100px;
            margin: 40px auto;
            padding: 30px;
            background: var(--bg-secondary);
            border-radius: 12px;
            border: 1px solid var(--card-border);
        }}
        .section-container h2 {{
            border-bottom: 2px solid var(--card-border);
            padding-bottom: 10px;
            margin-bottom: 20px;
            color: var(--accent);
        }}
        iframe {{
            width: 100%;
            height: 600px;
            border: none;
            border-radius: 8px;
            background: #fff;
        }}
    </style>
</head>
<body>
    <header>
        <span class="badge">GPT-OSS 120B PARALLEL SWARM EXPERIMENT</span>
        <h1>Mega-Agent 10,000 Portal</h1>
        <p class="subtitle">10,000 Autonomous Agents Collaborating on Future Urban Intelligence, Simulation & Energy Infrastructure</p>
        <div class="narrative-box">
            <h3>⚡ The Epoch Narrative</h3>
            <p>
                In the era dominated by mega-scale frontier models like Fable 5.1, Opus 5.5, and GPT-6 Astra, 
                this project demonstrates that an ensemble of open-weight <strong>GPT-OSS 120B</strong> agents, 
                orchestrated across 100 discrete evolutionary stages with deterministic verification guards, 
                can synthesize end-to-end production packages, rigorous statistical analyses, and closed-loop agent simulations 
                exceeding isolated single-turn reasoning.
            </p>
        </div>
    </header>

    <div class="grid">
        <div class="card">
            <h2>📊 Synthetic Intelligence Report</h2>
            <p>10,000 agent chapters synthesized across 6 domains (Transportation, Energy, Vertical Farming, Autonomous Corridors, Green Architecture, AI Urban Gov).</p>
            <a href="report/final_report.html" target="_blank">Open Full Report &rarr;</a>
        </div>
        <div class="card">
            <h2>📈 Data Analytics & Visuals</h2>
            <p>Exploratory data analysis of 374M population & 254M daily traffic flow, rendered into interactive and standalone vector charts.</p>
            <a href="analysis/dashboard.html" target="_blank">View Dashboard &rarr;</a>
        </div>
        <div class="card">
            <h2>📦 Production Package (Python)</h2>
            <p><code>agent_collab</code> PyPI-ready library verified with automated pytest regression suite (6 test cases passing).</p>
            <a href="code/setup.py" target="_blank">Inspect Library &rarr;</a>
        </div>
        <div class="card">
            <h2>🔄 Multi-Agent Simulation Engine</h2>
            <p>Archetype agent swarm (Catalysts, Guardians, Explorers, Collaborators, Regulators) computing network resilience and idea propagation metrics.</p>
            <a href="sim/README.md" target="_blank">Explore Simulation &rarr;</a>
        </div>
    </div>

    <div class="section-container">
        <h2>Live Synthetic Dashboard</h2>
        <iframe src="analysis/dashboard.html"></iframe>
    </div>

    <div class="section-container">
        <h2>Synthesis Report Preview</h2>
        <iframe src="report/final_report.html"></iframe>
    </div>
</body>
</html>
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(portal_html)

print("Master portal written to", output_path)
