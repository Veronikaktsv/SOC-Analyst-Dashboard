import pandas as pd
from datetime import datetime
import dash
from dash import dcc, html
import plotly.express as px

# Load and preprocess data
df = pd.read_csv("incidents.csv", parse_dates=["start_time", "detect_time", "resolve_time"])

# Calculate MTTD and MTTR (in minutes)
df['time_to_detect'] = (df['detect_time'] - df['start_time']).dt.total_seconds() / 60
df['time_to_respond'] = (df['resolve_time'] - df['detect_time']).dt.total_seconds() / 60

mttd = df['time_to_detect'].mean()
mttr = df['time_to_respond'].mean()

# Incident counts by type and severity
count_by_type = df['type'].value_counts().reset_index()
count_by_type.columns = ['type', 'count']

count_by_severity = df['severity'].value_counts().reset_index()
count_by_severity.columns = ['severity', 'count']

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "SOC Analyst Dashboard"

app.layout = html.Div(style={'padding': '20px'}, children=[
    html.H1("SOC Analyst Dashboard", style={'textAlign': 'center'}),
    
    # KPI cards
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '30px'}, children=[
        html.Div(style={'border': '1px solid #ccc', 'padding': '20px', 'width': '30%', 'textAlign': 'center', 'borderRadius': '5px'}, children=[
            html.H3("Mean Time to Detect (MTTD)"),
            html.H2(f"{mttd:.1f} minutes")
        ]),
        html.Div(style={'border': '1px solid #ccc', 'padding': '20px', 'width': '30%', 'textAlign': 'center', 'borderRadius': '5px'}, children=[
            html.H3("Mean Time to Respond (MTTR)"),
            html.H2(f"{mttr:.1f} minutes")
        ]),
    ]),
    
    # Incident counts by type bar chart
    html.Div([
        html.H3("Incident Counts by Type"),
        dcc.Graph(
            figure=px.bar(count_by_type, x='type', y='count', color='type', text='count')
            .update_layout(showlegend=False)
        )
    ], style={'marginBottom': '40px'}),
    
    # Incident counts by severity pie chart
    html.Div([
        html.H3("Incident Counts by Severity"),
        dcc.Graph(
            figure=px.pie(count_by_severity, values='count', names='severity', color='severity',
                          color_discrete_map={'Low':'green', 'Medium':'orange', 'High':'red'})
        )
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
