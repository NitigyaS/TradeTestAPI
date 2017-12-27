from flask import render_template , jsonify , request
from . import nse
from ..model import Nifty
from ..scripts import historic_data

@nse.route('/nse/nifty50')
def homepage():
    """
    Render the homepage template on the / route
    """
    company = Nifty.query.all()
    return jsonify(status="200", message=[i.serialize for i in Nifty.query.all()])

@nse.route('/nse/historic_data',methods=['GET'])
def historic_data_nse():
    try:
        symbol = request.headers.get("symbol")
        date_range = request.headers.get("daterange")
        from_date = request.headers.get("fromdate")
        to_date = request.headers.get("todate")
        data = historic_data.historic_data_bse(symbol,date_range,from_date,to_date)
        return jsonify(data)
    except AttributeError:
        message = "symbol : NSE Recognized Symbol ,"\
                  "datarange : [day|week|15days|1month|3month|12month|24month] ," \
                  "fromdate : DD-MM-YYYY ," \
                  "todate: DD-MM-YYY"
        return jsonify(status=403,message="Fail : Wrong Headers Provided",syntax=message)
