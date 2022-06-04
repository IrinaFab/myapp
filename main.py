import dash
from dash import Dash, dcc, html
from google.cloud import bigquery
import pandas as pd
import plotly
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT * FROM 
    ML.EXPLAIN_FORECAST(MODEL covid19.numreports_forecast,
                STRUCT(14 AS horizon, 0.8 AS confidence_level))
"""

query_job = client.query(query) 

df = query_job.to_dataframe()

fig = px.line(df, x='time_series_timestamp', y ='time_series_data')

app.layout = html.Div(children = [
    html.H1("Covid 19 forecast Romania"),
    html.Div(children ='''An app to see what the expected covid19 cases over the next 14 days.'''),
    dcc.Graph(
        id = 'Covid 19 forecast Romania graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)