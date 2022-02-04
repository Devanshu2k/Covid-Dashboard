import plotly.graph_objects as go
import plotly as pt
import pandas as pd
from get_date import get_date

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

    fig.update_layout(modebar_remove=['zoom', 'pan'])

    return fig
