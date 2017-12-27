import requests
from bs4 import BeautifulSoup
import json



def fetch_data_bse(symbol,date_range,from_date,to_date):

    url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp"

    #querystring = {"symbol":"tcs","segmentLink":"3","symbolCount":"2","series":"ALL","dateRange":"1month","fromDate":"","toDate":"","dataType":"PRICEVOLUME"}
    querystring = {"symbol":symbol,"segmentLink":"3","symbolCount":"2","series":"ALL","dateRange":date_range,"fromDate":from_date,"toDate":to_date,"dataType":"PRICEVOLUME"}

    headers = {
        'host': "www.nseindia.com",
        'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.5",
        'accept-encoding': "gzip, deflate, br",
        'referer': "https://www.nseindia.com/products/content/equities/equities/eq_security.htm",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'postman-token': "14901e89-9c85-7d02-e53d-1efc943b3721"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return  response.text



def html2Json(html_text):
    keys = []

    historic_json = []

    parsed_html = BeautifulSoup(html_text, "html.parser")

    for key in parsed_html.table.tr.find_all('th'):
        keys.append(key.text)

    for rows in parsed_html.find_all('tr'):
        arr = {}
        item = 0
        for data in rows.find_all('td'):
            arr[keys[item]] = data.text
            item = item + 1
        historic_json.append(arr)
    historic_json.remove({})
    return historic_json

# List Json historic Price of a Company
def historic_data_bse(symbol,date_range="",from_date="",to_date=""):
    return html2Json(fetch_data_bse(symbol,date_range,from_date,to_date))

# List of Companies Matching the name
def list_companies(name_regex):
    url = "http://etsearch.indiatimes.com/etspeeds/ethome.ep"

    querystring = {"ticker": name_regex, "matchCompanyName": "true", "detail": "true", "pagesize": "6",
                   "outputtype": "json"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "32c2df47-ed0a-3556-0c0c-c5834bb12c9f"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text



