from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load and sort data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# Layout with styling classes
app.layout = html.Div(className='container', children=[
    html.H1("Pink Morsel Sales Visualiser", className='header'),

    # Radio Button for Region Filtering
    html.Div(className='control-section', children=[
        html.Label("Select Region:", className='control-label'),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', # Default value
            className='radio-buttons'
        ),
    ]),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update the graph based on selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, x="date", y="sales",
        title=f"Sales Trend: {selected_region.capitalize()}",
        template="plotly_white"
    )
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run(debug=True)