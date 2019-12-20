import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table

external_stylesheets = [\
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://codepen.io/chriddyp/pen/brPBPO.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'God please let this work'
app.config.suppress_callback_exceptions = True
