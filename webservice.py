# -*- coding: utf-8 -*-
#After launch in commandline you will see address and port to access webservice.
#Examples of usage:
#127.0.0.1:5002/currency_converter
#127.0.0.1:5002/currency_converter?amount=1000&input_currency=EUR
#127.0.0.1:5002/currency_converter?amount=1000&input_currency=EUR&output_currency=USD

from converter import conversion
from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


@app.route('/currency_converter')

def get():
	"""	Sets parameters to GET query in webservice and call convert function """
	amount = request.args.get('amount', default = 1.0, type = float)
	input_currency = request.args.get('input_currency', default = 'USD', type = str)
	output_currency = request.args.get('output_currency', default = 'ALL', type = str)
	return conversion(amount, input_currency, output_currency)



if __name__ == '__main__':
	app.run(port='5002')