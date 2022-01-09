import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import numpy as np
import pandas as pd
from pandas.io.formats import style
from scripts.baseDataCreation import create_base_df
from app import app

# print(create_base_df(2021-22))
total_df_with_salaries = create_base_df(season_year=2021)
# total_df_with_salaries = pd.read_csv('nba)
total_df_with_salaries['2021-22'].replace('[\$,]', '', regex=True).astype(float)

def normalize(array):
    return np.asarray([float(i)/np.max(array) for i in array])


layout = html.Div([
    html.Div([
        html.H3('urLeague Analytics', style={'font-size':'3.5rem', 'color':'white', 'text-decoration': 'underline'}),
        html.H3('Player Data Table', style={'font-size':'1.7rem'}),
        html.Br(),
        html.Hr(),
        html.Div([
            dcc.Checklist(
            id='checklist-options',
            options=[
                {'label': 'FG%', 'value': 'field_goal_percentage'},
                {'label': 'FT%', 'value': 'free_throw_percentage'},
                {'label': '3PM', 'value': 'made_three_point_field_goals'},
                {'label': 'REB', 'value': 'rebounds'},
                {'label': 'AST', 'value': 'assists'},
                {'label': 'STL', 'value': 'steals'},
                {'label': 'BLK', 'value': 'blocks'},
                {'label': 'TO', 'value': 'turnovers'},
                {'label': 'PPG', 'value': 'ppg'}
            ],
            value=[
                'field_goal_percentage', 'free_throw_percentage', 'made_three_point_field_goals',
                'rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'ppg'
            ],
            labelStyle={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
        ),
        html.Div([
            html.Div(
                dcc.Dropdown(
                    id='fg-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='ft-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='3p-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='reb-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='ast-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='stl-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='blk-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='to-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='ppg-weighting',
                    options=[
                        {'label': '0.5x', 'value': '0.5x'},
                        {'label': '1x', 'value': '1x'},
                        {'label': '1.5x', 'value': '1.5x'},
                        {'label': '2x', 'value': '2x'}
                    ],
                    value='1x'
                ),
                style={
                    'display': 'inline-block', 'width': '11%', 'color':'rgba(242,133,0,1)'}
            )
        ])
    ], style={
        'display': 'inline-block',
        'width': '90%',
        'color':'rgba(242,133,0,1)',
        }
    )]),
    html.Br(),
    html.Br(),

    html.Div(
        id='table-filtering-be',
        className='tableDiv'
    )
])

@app.callback(
    Output('table-filtering-be', 'children'),
    [Input('fg-weighting', 'value'),
     Input('ft-weighting', 'value'),
     Input('3p-weighting', 'value'),
     Input('reb-weighting', 'value'),
     Input('ast-weighting', 'value'),
     Input('stl-weighting', 'value'),
     Input('blk-weighting', 'value'),
     Input('to-weighting', 'value'),
     Input('ppg-weighting', 'value'),
     Input('checklist-options', 'value')])
def update_table(fg_value, ft_value, three_point_value, rebs, asts, stls, blks,
    tos, ppg, checklist_options):
    weight_dict = {
        'field_goal_percentage': float(fg_value[:-1]),
        'free_throw_percentage': float(ft_value[:-1]),
        'made_three_point_field_goals': float(three_point_value[:-1]),
        'rebounds': float(rebs[:-1]),
        'assists': float(asts[:-1]),
        'steals': float(stls[:-1]),
        'blocks': float(blks[:-1]),
        'turnovers': float(tos[:-1]),
        'ppg': float(ppg[:-1])
    }

    temp_table = total_df_with_salaries

    temp_table['ppg'] = temp_table.ppg.round(1)

    temp_table['raw_score'] = 0

    for option in checklist_options:
        if option == 'turnovers':
            temp_table['raw_score'] -= normalize(temp_table[option])*weight_dict[option]
        else:
            temp_table['raw_score'] += normalize(temp_table[option])*weight_dict[option]

    temp_table['raw_score'] = (normalize(temp_table['raw_score'])*100).round(2)

    temp_table = temp_table.drop('no_accents', 1)
    # print(temp_table)

    temp_table.columns = ['Player', 'FG%', 'FT%', '3PM', 'FGM', 'FTM', 'GP', 'FGA', 'FTA',
       'REB', 'AST', 'BLK', 'STL', 'TO', 'TEAM', '2021-22', 'PPG', 'RAW']

    # print(temp_table.columns)

    temp_table_cols = [{'name': i, 'id': i} for i in temp_table.columns]
    return html.Div([

            dash_table.DataTable(
                id='main-table',
                columns=temp_table_cols,
                data=temp_table.to_dict('rows'),
                sort_action='native',
                # style_as_list_view=True,

                style_table = {
                    'overflowX': 'scroll',
                    'maxWidth': '100%',
                    'minWidth': '40%'
                },

                style_header = {
                    'backgroundColor': 'rgba(48,213,200,1)',
                    'fontWeight': 'bold',
                    'color': 'white',
                    'fontSize': '1.3rem',
                    'padding-top': '1rem',
                    'padding-bottom': '.5rem',
                    'border': '1px solid rgba(0,0,60,.7)'
                },

                style_cell = {
                    'font-family':'sans-serif',
                    'fontSize': '.8rem',
                    'color': 'white',
                    'backgroundColor': 'rgba(48,213,200,.8)',
                    'textAlign': 'center',
                    'border': '1px solid rgba(0,0,220,.4)',
                    'minWidth': '50px', 'width': '80px', 'maxWidth': '300px',
                    # 'whiteSpace': 'normal'
                },
                style_cell_conditional=[
                    {'if': {'column_id': 'Player'},'textAlign': 'left'},
                    {'if': {'column_id': 'Player'},'width': '100px'},
                    {'if': {'column_id': 'Player'},'padding-left': '18px'},
                    {'if': {'column_id': '2021-22'},'width': '110px'},
                ],
                style_data_conditional=[
                    {
                        'if': {
                            'filter_query': '{{{}}} >= {}'.format(col, value),
                            'column_id': col
                        },
                        'backgroundColor': 'rgba(242,133,0,1)',
                        'color': 'white'
                    } for (col, value) in temp_table.quantile(0.96).iteritems()
                ]
            )
    ])
