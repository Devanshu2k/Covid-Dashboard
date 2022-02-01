import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from get_date import get_date
import plotly.express as px

ConfirmedCases_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
Deaths_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
Recoveries_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

def get_data():
    ## Read Data for Cases, Deaths and Recoveries
    d3 = get_date()
    Recoveries_raw_mod = Recoveries_raw.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
    Deaths_raw_mod = Deaths_raw.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
    ConfirmedCases_raw_mod = ConfirmedCases_raw.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})

    total_list = ConfirmedCases_raw_mod.groupby('Country')[d3].sum().tolist()
    total_deaths = Deaths_raw_mod.groupby('Country')[d3].sum().tolist()
    total_cases_count = sum(total_list)
    total_death_count = sum(total_deaths)
    
    return [total_cases_count, total_death_count]

def process_data(data,cntry='US',window=3):
    conf_ts = data
    conf_ts_cntry = conf_ts[conf_ts['Country/Region']==cntry]
    final_dataset = conf_ts_cntry.T[4:].sum(axis='columns').diff().rolling(window=window).mean()[40:]
    df = pd.DataFrame(final_dataset,columns=['Total'])
    return df
    
def fig_world_trend(cntry='US',window=3):
    df = process_data(data=ConfirmedCases_raw,cntry=cntry,window=window)
    df.head(10)
    if window==1:
        yaxis_title = "Daily Cases"
    else:
        yaxis_title = "Daily Cases ({}-day MA)".format(window)
    fig = px.line(df, y='Total', x=df.index, title='Daily confirmed cases trend for {}'.format(cntry),height=600,color_discrete_sequence =['maroon'])
    fig.update_layout(title_x=0.5,plot_bgcolor='#F2DFCE',paper_bgcolor='#F2DFCE',xaxis_title="Date",yaxis_title=yaxis_title)
    return fig

fig_world_trend()