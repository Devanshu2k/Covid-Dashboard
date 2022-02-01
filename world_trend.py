from get_data import fig_world_trend

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

fig = fig_world_trend()

def get_country_list():
    return covid_conf_ts['Country/Region'].unique()

def create_dropdown_list(cntry_list):
    dropdown_list = []
    for cntry in sorted(cntry_list):
        tmp_dict = {'label':cntry,'value':cntry}
        dropdown_list.append(tmp_dict)
    return dropdown_list

def get_country_dropdown(id):
    return html.Div([
                        html.Label('Select Country'),
                        dcc.Dropdown(id='my-id'+str(id),
                            options=create_dropdown_list(get_country_list()),
                            value='US'
                        ),
                        html.Div(id='my-div'+str(id))
                    ])

def get_slider():
    return html.Div([  
                        dcc.Slider(
                            id='my-slider',
                            min=1,
                            max=15,
                            step=None,
                            marks={
                                1: '1',
                                3: '3',
                                5: '5',
                                7: '1-Week',
                                14: 'Fortnight'
                            },
                            value=3,
                        ),
                        html.Div([html.Label('Select Moving Average Window')],id='my-div'+str(id),style={'textAlign':'center'})
                    ])