#from scancovia import ScanCovModel
#model = ScanCovModel()

import io
import base64
from flask import Flask,render_template,request,make_response,redirect,Response
import json
from get_data import get_data,fig_world_trend
import plotly
import plotly.express as px
import pandas as pd
from plots import get_chloro
from plots import case_plot

import dash
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_bootstrap_components as dbc
from dash_gui import fig_world_trend,generate_layout,generate_cards
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

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


@server.route("/stats", methods=["GET", "POST"])
def stats():
    data = get_data()
    #response = make_response(json.dumps(data))
    #response.content_type = 'application/json'
    return render_template('stats.html',Data=data) 

@server.route("/plots/")
def notdash():
    return render_template('plots.html',PageTitle = "COVID-19 Plots")

@server.route('/plot.png')
def plot_png():
    fig = case_plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@server.route("/chloro", methods=["GET", "POST"])
def chloro():
    fig = get_chloro()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('chloro.html', graphJSON=graphJSON) 

def severity_pred(val):
    print(val)
    risk_val = model(val)
    return risk_val

@server.route("/severity")
def mortality():
    return render_template('severity.html')

def conv(di):
    for key,value in di.items():
        di[key] = int(value)
    return di

@server.route("/result", methods=["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = conv(to_predict_list)
        f = request.files['nii_path']
        f.save(f.filename)  
        to_predict_list['nii_path'] = f.filename
        sample = {
        'Oxygen saturation': 80,
        'Age': 75,
        'Sex': 0, # 1 for Male, 0 for Female
        'Platelet': 4.5,
        'Urea': 1.3,
        'nii_path': 'patient_exam.nii',
        }
        print(sample)
        print("################")
        print(to_predict_list)
        
        result = severity_pred(to_predict_list)    
        prediction = result['AI-severity']*100             
        return render_template('result.html',prediction = prediction)
        
        
    

@server.route("/support", methods=["GET", "POST"])
def chatbot():
    return render_template('chloro.html')

if __name__ == '__main__':
    server.run(debug=True)