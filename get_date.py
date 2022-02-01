from datetime import date,timedelta

def get_date():
    today = date.today()
    today = today - timedelta(days = 1)
    d3 = today.strftime("%#m/%#d/%y")
    return d3