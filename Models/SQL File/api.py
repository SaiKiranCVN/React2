import requests
#https://cloud.iexapis.com/stable//stock/AAPL/quote?token=pk_4005dbccb0834085ac1ec6baffbe8f2f
base_url = 'https://cloud.iexapis.com/stable/stock/'
stocks = ['AAPL','TSLA','AMZN','MSFT','NVDA']
rest = '/quote?token=pk_4005dbccb0834085ac1ec6baffbe8f2f'
'''
symbol
companyName
latestPrice
previousClose
change
changePercent
week52High
week52Low
marketCap
isUSMarketOpen
'''
def result():
	all_ = []
	for stock in stocks:
		send = {}
		res = requests.get(base_url+stock+rest).json()
		send['symbol'] = res['symbol']
		send['companyName'] = res['companyName']
		send['latestPrice'] = res['latestPrice']
		send['previousClose'] = res['previousClose']
		send['change'] = res['change']
		send['changePercent'] = res['changePercent']
		send['week52High'] = res['week52High']
		send['week52Low'] = res['week52Low']
		send['isUSMarketOpen'] = res['isUSMarketOpen']
		send['marketCap'] = res['marketCap']
		all_.append(send)
	return all_