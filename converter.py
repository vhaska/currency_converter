# -*- coding: utf-8 -*-
import sys, argparse, json
from currency_converter import CurrencyConverter

def validate(symbol):
	"""Converts string input $, £, etc... to string output USD, GBP, etc...
	If you input not known symbol or error symbol, it will return uppercased input
	
		Example
			validate('$') = 'USD'
			validate('Kč') = 'CZK'
	"""
	
	currency_symbols = {
	'AUD':['AUSTRALIAN DOLLAR','A$'],
	'BGN':['ЛВ'],
	'BRL':['R$'],
	'CAD':['CAN$','C$'],
	'CHF':['FR','SFR'],
	'CNY':['CN¥','¥'],
	'CZK':['KČ','KC','ČESKÁ KORUNA'],
	'GBP':['£','POUND STERLING'],
	'HUF':['FT'],
	'HRK':['KN'], 
	'IDR':['RP'],
	'ILS':['₪'],
	'JPY':['JP¥'],
	'KRW':['₩'],
	'MYR':['RM'],
	'PLN':['ZŁ','ZL'],
	'PHP':['₱'],
	'RON':['LEI'],
	'RUB':['₽'],
	'THB':['฿'],
	'USD':['$','US DOLLAR'],
	'ZAR':['R']
	}
	
	for currency_international_name in currency_symbols:
		# if symbol is in name
		if symbol.upper() in currency_symbols[currency_international_name] or symbol.upper() == currency_international_name:
			return(currency_international_name)
	return(symbol.upper())



def conversion(amount, input_currency, output_currency):
	"""Converts amount of money to different currency
	Input:
		amount FLOAT
		input_currency STRING 
		output_currency STRING 
	Output: JSON
		{
		"input": {
			"amount": "100",
			"currency": "CZK"
		},
		"output": {
			"USD": 22.38
		}
	"""
	c = CurrencyConverter()
	input_currency = validate(input_currency)
	
	json_output = {}
	data_input_currency={}
	data_output_currency={}
	data_input_currency['amount']= amount
	data_input_currency['currency'] = input_currency
	
	if output_currency == 'ALL':
		# change set to list and sort it ascending
		currencies = list(c.currencies)
		currencies.sort()
		
		for currency in currencies:
			try:
				converted_amount = round(c.convert(amount, input_currency, currency), 2)
				data_output_currency[currency] = converted_amount
				
			except:
				#if currency present exchange rate was not found, we ignore it to prevent failure
				pass
			
	else:	
		output_currency = validate(output_currency)
		converted_amount = round(c.convert(amount, input_currency, output_currency), 2)
		data_output_currency[output_currency] = converted_amount
		
	json_output['input'] = data_input_currency
	json_output['output'] = data_output_currency
	
	return(json.dumps(json_output, indent = 4))



if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description = 'Converts AMOUNT in INPUT_CURRENCY and returns in OUTPUT_CURRENCY or ALL currencies (if OUTPUT_CURRENCY is not specified)')	
	parser.add_argument('--amount', default = '1')
	parser.add_argument('--input_currency', default = 'USD')
	parser.add_argument('--output_currency', default = 'ALL')
	args = parser.parse_args()
	amount, input_currency, output_currency = args.amount, args.input_currency,args.output_currency
	
	print(conversion(amount, input_currency, output_currency))