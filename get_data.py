import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from get_date import get_date



def get_data():
    ## Read Data for Cases, Deaths and Recoveries
    ConfirmedCases_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    Deaths_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    Recoveries_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    d3 = get_date()
    Recoveries_raw = Recoveries_raw.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
    Deaths_raw = Deaths_raw.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
    ConfirmedCases_raw = ConfirmedCases_raw.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})

    total_list = ConfirmedCases_raw.groupby('Country')[d3].sum().tolist()
    total_deaths = Deaths_raw.groupby('Country')[d3].sum().tolist()
    total_cases_count = sum(total_list)
    total_death_count = sum(total_deaths)
    
    return [total_cases_count, total_death_count]
    
