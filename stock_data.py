import requests
from bs4 import BeautifulSoup as bs

def get_historical_data(name, number_of_days):

    def scrap(number:int):
        if number == 0:
            return divs[number].span.text
        else:
            return float(divs[number].span.text.replace(',',''))
    keys = ['date','open','high','low','adj_close','volume']
    data = []
    url = "https://finance.yahoo.com/quote/" + name + "/history/"
    response = requests.get(url)
    rows = bs(response.content,"html.parser").findAll('table')[0].tbody.findAll('tr')
    for each_row in rows:
        divs = each_row.findAll('td')
        if divs[1].span.text != 'Dividend':
            vals = [scrap(x) for x in range(len(keys))]
            data.append({'{0}'.format(name.upper()):dict(zip(keys,vals))
                         })
    return data[:number_of_days]
