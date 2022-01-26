from flask import Flask,render_template,request,make_response,redirect
import json
from get_data import get_data
import plotly
import plotly.express as px
import pandas as pd
from plots import get_chloro

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/plots")
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City', 
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('notdash.html', graphJSON=graphJSON)

@app.route("/stats", methods=["GET", "POST"])
def stats():
    data = get_data()
    #response = make_response(json.dumps(data))
    #response.content_type = 'application/json'
    return render_template('stats.html',Data=data) 

@app.route("/chloro", methods=["GET", "POST"])
def chloro():
    fig = get_chloro()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('chloro.html', graphJSON=graphJSON) 



if __name__ == '__main__':
    app.run(debug=True)