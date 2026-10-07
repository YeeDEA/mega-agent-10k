import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import os

# Paths (assumes CSV files are in the same directory)
pop_path = 'population_10k.csv'
traffic_path = 'traffic_10k.csv'

# Load data
df_pop = pd.read_csv(pop_path)
df_traffic = pd.read_csv(traffic_path)

# Helper to convert matplotlib figure to base64 PNG
def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# Population histogram
fig1, ax1 = plt.subplots(figsize=(6,4))
ax1.hist(df_pop['population'], bins=30, color='skyblue', edgecolor='black')
ax1.set_title('Population Distribution')
ax1.set_xlabel('Population')
ax1.set_ylabel('Count')
pop_img = fig_to_base64(fig1)
plt.close(fig1)

# Traffic scatter plot
fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.scatter(df_traffic['hour'], df_traffic['traffic_volume'], alpha=0.7)
ax2.set_title('Traffic Volume by Hour')
ax2.set_xlabel('Hour')
ax2.set_ylabel('Traffic Volume')
traffic_img = fig_to_base64(fig2)
plt.close(fig2)

# Build simple HTML dashboard
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>10K Records Dashboard</title>
    <style>
        body {{font-family: Arial, sans-serif; margin: 40px;}}
        h1 {{text-align: center;}}
        .chart {{margin-bottom: 40px; text-align: center;}}
        img {{max-width: 100%; height: auto; border: 1px solid #ccc;}}
    </style>
</head>
<body>
    <h1>10K Records Dashboard</h1>
    <div class="chart">
        <h2>Population Distribution</h2>
        <img src="data:image/png;base64,{pop_img}" alt="Population histogram"/>
    </div>
    <div class="chart">
        <h2>Traffic Volume by Hour</h2>
        <img src="data:image/png;base64,{traffic_img}" alt="Traffic scatter"/>
    </div>
</body>
</html>'''

# Write dashboard.html
output_path = 'dashboard.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print('Dashboard written to', os.path.abspath(output_path))
