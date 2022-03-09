import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly as pt
import pandas as pd
from get_date import get_date
import matplotlib.pyplot as plt

def get_chloro():
    d3 = get_date()
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    df = df.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})

    total_list = df.groupby('Country')[d3].sum().tolist()

    country_list = df["Country"].tolist()
    country_set = set(country_list)
    country_list = list(country_set)
    country_list.sort()

    new_df = pd.DataFrame(list(zip(country_list, total_list)), 
                columns =['Country', 'Total_Cases'])

    colors = ["#F9F9F5", "#FAFAE6", "#FCFCCB", "#FCFCAE",  "#FCF1AE", "#FCEA7D", "#FCD97D",
            "#FCCE7D", "#FCC07D", "#FEB562", "#F9A648",  "#F98E48", "#FD8739", "#FE7519",
            "#FE5E19", "#FA520A", "#FA2B0A", "#9B1803",  "#861604", "#651104", "#570303",]


    fig = go.Figure(data=go.Choropleth(
        locationmode = "country names",
        locations = new_df['Country'],
        z = new_df['Total_Cases'],
        text = new_df['Total_Cases'],
        #color='unemp',
        #color_continuous_scale="Viridis",
        colorscale = colors,
        #autocolorscale=True,
        #range_color=(0, 12),
        #reversescale=True,
        colorbar_title = 'Reported Covid-19 Cases'
    ))

    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})

    #fig.update_layout(modebar_remove=['zoom', 'pan'])

    return fig

def case_plot():
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]
    
    fig = plt.figure(figsize=(16,10))
    
    ax = plt.axes()
    ax.grid(linewidth=0.4, color='#8f8f8f')
    
    ax.set_facecolor("black")
    ax.set_xlabel('\nDate',size=15,color='#4bb4f2')
    ax.set_ylabel('Number of Confirmed Cases\n',
                size=15,color='#4bb4f2')
    
    plt.xticks(rotation='vertical',size='1',color='white')
    plt.yticks(size=1,color='white')
    plt.tick_params(size=1,color='white')
    
    for i,j in zip(X,Y):
        ax.annotate(str(j),xy=(i,j+100),color='white',size='10')
        
    
    plt.title("COVID-19 IN : Daily Confirmed\n",
            size=15,color='#28a9ff')
    
    ax.plot(X,Y,
            color='#1F77B4',
            marker='o',
            linewidth=4,
            markersize=10,
            markeredgecolor='#035E9B')

    return fig

case_plot()