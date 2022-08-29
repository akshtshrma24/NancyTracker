import json
from datetime import date
import os

import requests

from influxHandler import *
from logger import *


def getData():
    response = requests.get(
        'https://phx.unusualwhales.com/api/senate_stocks/Nancy%20Pelosi',
        headers=constants.HEADERS_GET_DATA)
    for item in response.json()['senate_stocks']:
        if (str("2022-07-26") in str(item['filed_at_date'])):
            data = f"{item['txn_type']} {item['symbol']} {item['filed_at_date']}"
            return data
    return None

