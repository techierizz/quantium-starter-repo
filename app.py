from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. Initialize the Dash app
app = Dash(__name__)

# 2. Load the processed data
# Ensure formatted_data.csv exists in the same directory
df = pd.read_csv("formatted_data.csv")
df = df.sort_values(by="date")

# 3. Create the Plotly Line Chart
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# 4. Define the App Layout
app.layout = html.Div(children=[
    # The Header
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    # The Graph
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 5. Run the app
if __name__ == '__main__':
    app.run(debug=True)