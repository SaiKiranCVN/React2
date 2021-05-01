from threading import Timer
from api import result

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='rootroot', host='127.0.0.1', database='ringer',auth_plugin='mysql_native_password')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()




def updating():
	Timer(6000,updating).start() 
	print('Updating every 6000 seconds (100 min)')
	data = result()
	
	docs = db.collection('stock').get()
	if len(docs) == 0:
		for d in data:
			# Inserting
			db.collection('stock').document(d['symbol']).set(d)
		return 
	for i,doc in enumerate(docs):
		doc = doc.to_dict()
		key = doc['symbol']
		db.collection('stock').document(key).update({'marketCap':data[i]['marketCap'],'isUSMarketOpen':data[i]['isUSMarketOpen']})
		if doc['latestPrice'] != data[i]['latestPrice']:
			db.collection('stock').document(key).update({'latestPrice':data[i]['latestPrice'],'previousClose':data[i]['previousClose'],'change':data[i]['change'],'changePercent':data[i]['changePercent']}) 
		if doc['week52High'] != data[i]['week52High']:
			db.collection('stock').document(key).update({'week52High':data[i]['week52High']})
		if doc['week52Low'] != data[i]['week52Low']:
			db.collection('stock').document(key).update({'week52Low':data[i]['week52Low']})
print('Started...')
updating()