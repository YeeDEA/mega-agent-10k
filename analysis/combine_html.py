import os

# Paths
analysis_dir = r'C:\Users\user1\.gemini\antigravity\scratch\demo_site\analysis'
output_path = os.path.join(analysis_dir, 'index_combined.html')

dashboard_path = os.path.join(analysis_dir, 'dashboard.html')
# Attempt to read dashboard HTML
with open(dashboard_path, 'r', encoding='utf-8') as f:
    dashboard_html = f.read()

# Simple placeholder for report (since report HTML not generated yet)
report_placeholder = "<h2>Report Section (HTML not generated)</h2><p>The report markdown (REPORT_10k.md) could not be found. Once Pandoc is installed, generate the HTML report and replace this placeholder.</p>"

# Combine into a single HTML document
combined_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>Demo Site Combined Dashboard</title>
    <style>
        body {{font-family: Arial, sans-serif; margin: 20px;}}
        h1 {{text-align: center;}}
        .section {{margin-bottom: 40px;}}
    </style>
</head>
<body>
    <h1>Demo Site – Combined Dashboard</h1>
    <div class=\"section\">
        {report_placeholder}
    </div>
    <div class=\"section\">
        {dashboard_html}
    </div>
</body>
</html>"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(combined_html)

print('Combined HTML written to', output_path)
