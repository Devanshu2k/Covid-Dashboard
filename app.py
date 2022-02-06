from flask import Flask,render_template,request,make_response,redirect
import json
from get_data import get_data,fig_world_trend
import plotly
import plotly.express as px
import pandas as pd
from plots import get_chloro
import dash
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_bootstrap_components as dbc
from dash_gui import fig_world_trend,generate_layout,generate_cards

server = Flask(__name__)

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
   __name__,
   server=server,
   url_base_pathname='/',
   suppress_callback_exceptions=True,
   external_stylesheets=external_stylesheets
)
app.layout = generate_layout()

@app.callback(
    [Output(component_id='graph1',component_property='figure'), #line chart
    Output(component_id='card1',component_property='children')], #overall card numbers
    [Input(component_id='my-id1',component_property='value'), #dropdown
     Input(component_id='my-slider',component_property='value')] #slider
)
def update_output_div(input_value1,input_value2):
    return fig_world_trend(input_value1,input_value2),generate_cards(input_value1)

# @server.route("/")
# def index():
#     return render_template('home.html')

# @app.route("/home")
# def home():
#     return render_template('home.html')

@server.route("/plots/")
def notdash():
    df = pd.DataFrame({'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],'Amount': [4, 1, 2, 2, 4, 5],'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('notdash.html', graphJSON=graphJSON)


@server.route("/stats", methods=["GET", "POST"])
def stats():
    data = get_data()
    #response = make_response(json.dumps(data))
    #response.content_type = 'application/json'
    return render_template('stats.html',Data=data) 

@server.route("/chloro", methods=["GET", "POST"])
def chloro():
    fig = get_chloro()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('chloro.html', graphJSON=graphJSON) 

if __name__ == '__main__':
    server.run(debug=True)