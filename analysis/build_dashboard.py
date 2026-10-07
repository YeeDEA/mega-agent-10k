import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load data
pop_path = 'population_10k.csv'
traffic_path = 'traffic_10k.csv'

# Assuming CSV files are in the same directory as this script
df_pop = pd.read_csv(pop_path)
df_traffic = pd.read_csv(traffic_path)

# Create Plotly figures
fig_pop = px.histogram(df_pop, x='population', nbins=30, title='Population Distribution')
fig_traffic = px.scatter(df_traffic, x='hour', y='traffic_volume', title='Traffic Volume by Hour')

# Build Dash app
app = Dash(__name__)
app.layout = html.Div([
    html.H1('10K Records Dashboard'),
    dcc.Graph(figure=fig_pop),
    dcc.Graph(figure=fig_traffic)
])

# Export static HTML
html_str = app.index()
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_str)

# Optional: run server for interactive view
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)
