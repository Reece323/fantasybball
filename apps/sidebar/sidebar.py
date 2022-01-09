import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from pandas.io.formats import style
from app import app
import datetime
# from app import app


sidebar_header = dbc.Row(
    [
        dbc.Col(html.H4("Tropics")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        'margin-top': '1rem',
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "",
                    className="lead",
                ),
            ],
            id="blurb",
        ),

        html.Br(),

        html.Div([
            html.H1('**last updated on',
                style={
                    'opacity': '1',
                    'color': 'rgba(242,133,0,1)',
                    'fontSize': 16,
                    'text-align':'left',
                    'font-style': 'italic'
                    }),
                    html.Br(),

            html.H1(datetime.datetime.now().strftime('%A'),
                style={
                    'opacity': '1',
                    'color': 'white',
                    'fontSize': 28,
                    'text-align':'center'
                    }),

                    html.Br(),

            html.H1(datetime.datetime.now().strftime('%B %d, %Y'),
            style= {'opacity': '1',
                    'color': 'white',
                    'fontSize': 26,
                    'text-align':'center'
                    }),

                    html.Br(),

            html.H1(datetime.datetime.now().strftime('%-I:%M %p %Z'),
                style={
                    'opacity': '1',
                    'color': 'white',
                    'fontSize': 26,
                    'text-align':'center'
                    })
        ]),
        html.Br(),

        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink(html.H6('Player Table'), href='/', style={'color':'rgba(48,213,200,.8)'}),
                    dbc.NavLink(html.H6('Team Optimizer'), href='/optimalTeam', style={'color':'rgba(48,213,200,.8)'}),
                    dbc.NavLink(html.H6('Team Analysis'), href='/teamAnalysis', style={'color':'rgba(48,213,200,.8)'}),
                    dbc.NavLink(html.H6('Salary Calculator'), href='/salaryCalculator', style={'color':'rgba(48,213,200,.8)'}),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    # style={'padding-right':'0'},
    id="sidebar",
)

# content = html.Div(
#     id="page-content",
#     className='mx-0 my-0'
#     )


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# app.clientside_callback(
#     """
#     function(n) {          
#         const local_time_str = new Date().toLocaleTimeString();                   
#         return "The current time is: " + local_time_str
#     }
#     """,
#     Output('date-time-title', 'children'),
#     Input('clock', 'n_intervals'),
# )

