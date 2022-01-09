import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.sidebar.sidebar import sidebar
from app import app, server
from apps import playerTable, salaryCalculator, optimalTeam, teamAnalysis

app.layout = html.Div([
    sidebar,
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == "/":
        return playerTable.layout
    elif pathname == '/salaryCalculator':
        return salaryCalculator.layout
    elif pathname == '/optimalTeam':
        return optimalTeam.layout
    elif pathname == '/teamAnalysis':
        return teamAnalysis.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
