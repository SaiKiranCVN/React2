import mysql.connector
import random
import string
import hashlib
import datetime as d
import sys
from api import result
#establishing the connection
conn = mysql.connector.connect(
   user='root', password='rootroot', host='ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com', database='ringer',auth_plugin='mysql_native_password')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


cursor.execute("set foreign_key_checks=0;")
conn.commit()

# For initial Volume
cursor.execute("SELECT * FROM user_data WHERE user_id='1';")
on = cursor.fetchall()
if len(on) == 0:
	cursor.execute(f"""INSERT INTO user_data VALUES ('1','xxxxxx','xxxxxx','xxxxxxxxxxxx','xxxxxxxx','xxxx@xxxx.xxx','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}',10000,'{d.date(random.randint(1990,2010), random.randint(1,12),random.randint(1,28)).strftime("%y-%m-%d")}','M','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
cursor.execute("SELECT * FROM payment WHERE pay_id='1';")
on = cursor.fetchall()
if len(on) == 0:
	cursor.execute(f"""INSERT INTO payment VALUES ('1','1','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
conn.commit()


def getCode(length = 10, char = string.ascii_uppercase +
                          string.digits +           
                          string.ascii_lowercase ):
    return ''.join(random.choice(char) for x in range(length))

def insert_users():
	inserted_users = []
	sql = """INSERT INTO user_data(user_id,first_name,last_name,username,password,email,time_registered
		,wallet,DOB,gender,updated_date) VALUES ("""
		# Executing the SQL command
	name = ['Sai','Ann','Kiran','Jake','Paul','John','Doe','David','Paul','Kim','Malena','Billy','Candis','Meghan','Kieth','Rene']
	domain = ['gmail','yahoo','outlook','icloud']
	gender = ['M','F']
	for i in range(100):
		id_ = getCode(10)
		f = random.choice(name)
		l = random.choice(name)
		u = f+l+getCode(3)
		dt = d.date(random.randint(1990,2010), random.randint(1,12),random.randint(1,28)).strftime("%y-%m-%d")
		rest = ["'"+id_ + "'","'" + f + "'","'" + l + "'","'" + u + "'","'" + hashlib.md5(getCode().encode('utf-8')).hexdigest() + "'","'" + u + '@' + random.choice(domain) + '.com' + "'" , "'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'",'10000',"'" + dt + "'","'" + random.choice(gender) + "'","'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'"]
		cursor.execute(sql+','.join(rest)+');')
		# print(sql+','.join(rest)+');')
		inserted_users.append(id_)
	print('*****************************************')
	print('Inserted 100 documents(rows) into Users')
	print('*****************************************')
	# Commit your changes in the database
	conn.commit()
	return inserted_users

ins = choose = result()
def insert_address(inserted_users):
	sql = """INSERT INTO address(add_id,type,street_address,city,state,zipcode,user_id,updated_date) VALUES ("""
	city = ['Brooklyn','New York','Dallas','Daton','London','Buffalo']
	state = ['TX','NY','CA','OH']
	for i in inserted_users:
		no_of_add = random.randint(1,2)
		type_ = random.choice(['work','home'])
		rest = ["'"+getCode(10)+"'","'"+type_+"'","'"+getCode(3,string.digits)+" st'","'"+random.choice(city)+"'","'"+random.choice(state)+"'",getCode(5,string.digits),"'"+i+"'","'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "');"]
		cursor.execute(sql+','.join(rest))
		if no_of_add != 1:
			type_ = random.choice(['work','home'])
			rest = ["'"+getCode(10)+"'","'"+type_+"'","'"+getCode(3,string.digits)+" st'","'"+random.choice(city)+"'","'"+random.choice(state)+"'",getCode(5,string.digits),"'"+i+"'","'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "');"]
			cursor.execute(sql+','.join(rest))
	# Commit your changes in the database
	conn.commit()
	print('*****************************************')
	print('Inserted documents(rows) into Address')
	print('*****************************************')

def insert_bank(inserted_users):
	sql = """INSERT INTO bank(bank_id,card_no,exp_date,cvv,name,defa,user_id,updated_date) VALUES ("""
	for i in inserted_users:
		no_of_banks = random.randint(1,2)
		name = ['Sai','Ann','Kiran','Jake','Paul','John','Doe','David','Paul','Kim','Malena','Billy','Candis','Meghan','Kieth','Rene']
		rest = ["'"+getCode(10)+"'",getCode(16,string.digits),"'"+d.date(random.randint(1990,2010), random.randint(1,12),1).strftime("%y-%m-%d")+"'",getCode(3,string.digits),"'"+random.choice(name)+' '+random.choice(name)+"'",'true',"'"+i+"'","'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "');"]
		cursor.execute(sql+','.join(rest))
		if no_of_banks != 1:
			rest = ["'"+getCode(10)+"'",getCode(16,string.digits),"'"+d.date(random.randint(1990,2010), random.randint(1,12),1).strftime("%y-%m-%d")+"'",getCode(3,string.digits),"'"+random.choice(name)+' '+random.choice(name)+"'",'true',"'"+i+"'","'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "');"]
			cursor.execute(sql+','.join(rest))
	# Commit your changes in the database
	conn.commit()
	print('*****************************************')
	print('Inserted documents(rows) into Bank')
	print('*****************************************')				


def insert_currency():
	sql = """INSERT INTO currencies(code,name,is_active,is_base_currency,updated_date) VALUES ('USD','United States Dollar','Y', 'Y',"""
	cursor.execute("SELECT * FROM currencies;")
	a = cursor.fetchall()
	# print(a)
	if not a:
		cursor.execute(sql + "'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "');")
		conn.commit()
		print('*****************************************')
		print('Inserted documents(rows) into Currencies')
		print('*****************************************')
	# print(type(a))



def insert_price_item():
	# print(ins)
	sql = """SELECT * FROM item WHERE code="""
	items = []
	for s in ins:
		cursor.execute(sql+"'"+s['symbol']+"';")
		a = cursor.fetchall()
		if len(a) == 0:
			price_id = getCode(10)
			# print(type(s['latestPrice']))
			sql1 = """INSERT INTO price(price_id,buy,sell,ts,updated_date,changeper) VALUES ("""
			sql2 = """INSERT INTO item(item_id,code,name,price_id,updated_date,pe,homepage,investorpage,sector) VALUES ("""
			it = getCode(10)
			items.append(it)
			cursor.execute(sql1 + "'" +price_id +"',"+ str(s['latestPrice']) +','+ str(s['latestPrice']+1) + ",'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "','" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'," + str(s['changePercent']) + ");")
			cursor.execute(sql2+ "'"+ it +"','"+ s['symbol'] +"','"+ s['companyName'] +"','"+ price_id +"','" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'," + str(15) + "," + "'www.google.com'," + "'www.google.com','Technology');")
		else:
			# print(a)
			# print('Updating')
			price_id = a[0][3]
			sql1 = f"""UPDATE price SET buy={str(s['latestPrice'])},sell={str(s['latestPrice']+1)},updated_date='{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE price_id='{str(price_id)}';"""
			# sql1 = """INSERT INTO price(price_id,buy,sell,ts,updated_date) VALUES ("""
			# cursor.execute(sql1 + str(price_id) +','+ str(s['latestPrice']) +','+ str(s['latestPrice']+1) +",'" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +"','" + d.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "');")
			cursor.execute(sql1)
	# Commit your changes in the database
	conn.commit()
	print('*****************************************')
	print('Inserted documents(rows) into price and/or item')
	print('*****************************************')	
	return items

# Insert by trading
def insert_rest(inserted_users):
	# Sells for initial volume
	for us in inserted_users:
		no_of_trades = random.randint(1,20)
		for i in range(no_of_trades):
			ch = random.choice(choose)
			cursor.execute(f"""SELECT * from item where code='{ch['symbol']}';""")
			i = cursor.fetchall()
			item_id = i[0][0]
			no_of_shares = random.randint(1,100)
			share_cost = ch['latestPrice'] + random.randint(-5,5)
			dt = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			# print(item_id)
			cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{no_of_shares},{share_cost},'{item_id}','1','{us}','1',current_time());""")
	conn.commit()
	# Create Trades
	for us in inserted_users:
		remaining = 10000
		no_of_trades = random.randint(1,20)
		for i in range(no_of_trades):
			ch = random.choice(choose)
			cursor.execute(f"""SELECT * from item where code='{ch['symbol']}';""")
			i = cursor.fetchall()
			item_id = i[0][0]
			# print(item_id)
			no_of_shares = random.randint(1,10)
			share_cost = ch['latestPrice'] + random.randint(-5,5)
			# Buy or Sell
			bs = random.choice(['B','S'])
			if bs == 'B':
				cursor.execute(f"""select * from user_data where user_id='{us}';""")
				bn = cursor.fetchall()
				# print(bn)
				wallet = bn[0][7]
				if no_of_shares*share_cost <= wallet:
					cursor.execute(f"""UPDATE user_data SET wallet = wallet - {no_of_shares*share_cost} where user_id='{us}';""")
				else:
					continue
			if bs == 'S':
				cursor.execute(f"""SELECT quantity from inventory where user_id = '{us}' and item_id = '{item_id}';""")
				isthere = cursor.fetchall()
				# print(isthere)
				if len(isthere) == 0 or isthere[0][0] < no_of_shares:
					continue
				cursor.execute(f"""UPDATE user_data SET wallet = wallet + {no_of_shares*share_cost} where user_id='{us}';""")
			trade_insert(no_of_shares,share_cost,item_id,bs,us)
	conn.commit()
	print('*****************************************')
	print('Trading Done')
	print('*****************************************')




def trade_insert(quantity,price,item_id,buy_sell,un):
	opp = 'buyer_id' if buy_sell == 'B' else 'seller_id'
	if opp == 'buyer_id': # User Buying

		cursor.execute(f"""SELECT * from trade where {opp} = '1' and seller_id <> '1' and unit_price <= {price} and item_id='{item_id}' and pay_id='1';""")
		a = cursor.fetchall()
		# print(a)
		if len(a) == 0:
			# cursor.execute(f"""INSERT INTO offer VALUES ('{getCode(10)}',{quantity},{buy_sell},{price},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
			cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{quantity},{price},'{item_id}','{un}','1','1','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")		
		else:
			for e in a:
				# the row has less items than required
				if e[1] < quantity: 
					quantity -= e[1]
					# cursor.execute(f"""UPDATE offer set buy_sell='{'D'}' WHERE offer_id={e[0]};""")
					# Include in payment
					amount = e[1]*e[2]
					iddd = getCode(10) # PaymentID
					cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade
					cursor.execute(f"""UPDATE trade SET buyer_id='{un}',pay_id='{iddd}',updated_date='{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
					# Include in Offer
					offer_id = getCode(10)
					# BuySell - D is done, price is total amount
					cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade_offer
					cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
					# Updating inventory
					cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
					there = cursor.fetchall()
					if len(there) == 0:
						# print(f"""INSERT INTO inventory(inven_id,item_id,bought_price,quantity,user_id,updated_date) VALUES('{getCode(10)}','{item_id}',{price},{e[1]},'{un}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
						cursor.execute(f"""INSERT INTO inventory(inven_id,item_id,bought_price,quantity,user_id,updated_date) VALUES('{getCode(10)}','{item_id}',{price},{e[1]},'{un}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					else:
						cursor.execute(f"""UPDATE inventory SET bought_price={price},quantity = quantity + {e[1]},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
				else:
					remain = e[1] - quantity
					amount = quantity*e[2]
					iddd = getCode(10) # PaymentID
					cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade
					cursor.execute(f"""UPDATE trade SET buyer_id='{un}',pay_id='{iddd}',updated_date='{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
					if remain != 0:
						cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{remain},{e[2]},'{e[4]}','1','{un}','1','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in Offer
					offer_id = getCode(10)
					# BuySell - D is done, price is total amount
					cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade_offer
					cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
					# Updating inventory
					cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
					there = cursor.fetchall()
					if len(there) == 0:
						cursor.execute(f"""INSERT INTO inventory(inven_id,item_id,bought_price,quantity,user_id,updated_date) VALUES('{getCode(10)}','{item_id}',{price},{e[1]},'{un}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					else:
						# print(type(e[1]),e[1],'233')
						# print(f"""UPDATE inventory SET bought_price={str(round(price,2))},quantity = quantity + {str(round(e[1],2))},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = {there[0][0]};""")
						cursor.execute(f"""UPDATE inventory SET bought_price={str(round(price,2))},quantity = quantity + {str(round(e[1],2))},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
					break
	else: # User Selling
		cursor.execute(f"""SELECT * from trade where {opp}='1' and buyer_id <> '1' and unit_price >= {price} and item_id='{item_id}' and pay_id='1';""")
		a = cursor.fetchall()
		if len(a) == 0:
			# cursor.execute(f"""INSERT INTO offer VALUES ('{getCode(10)}',{quantity},{buy_sell},{price},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
			cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{quantity},{price},'{item_id}','1','{un}','1','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")		
		else:
			for e in a:
				# the row has less items than required
				if e[1] < quantity: 
					quantity += e[1]
					# cursor.execute(f"""UPDATE offer set buy_sell='{'D'}' WHERE offer_id={e[0]};""")
					# Include in payment
					amount = e[1]*e[2]
					iddd = getCode(10) # PaymentID
					cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade
					cursor.execute(f"""UPDATE trade SET seller_id='{un}',pay_id='{iddd}',updated_date='{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
					# Include in Offer
					offer_id = getCode(10)
					# BuySell - D is done, price is total amount
					cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade_offer
					cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
					# Updating inventory
					cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
					there = cursor.fetchall()
					cursor.execute(f"""UPDATE inventory SET bought_price={price},quantity = quantity + {e[1]},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
				else:
					remain = e[1] - quantity
					amount = quantity*e[2]
					iddd = getCode(10) # PaymentID
					cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade
					cursor.execute(f"""UPDATE trade SET seller_id='{un}',pay_id='{iddd}',updated_date='{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
					if remain != 0:
						cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{remain},{e[2]},'{e[4]}','{un}',1,1,'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in Offer
					offer_id = getCode(10)
					# BuySell - D is done, price is total amount
					cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
					# Include in trade_offer
					cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
					# Updating inventory
					cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
					there = cursor.fetchall()
					# print(e[1],type(e[1]),'282')
					# print(f"""UPDATE inventory SET bought_price={price},quantity = quantity - {str(e[1])},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = {there[0][0]};""")
					cursor.execute(f"""UPDATE inventory SET bought_price={price},quantity = quantity + {str(e[1])},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
					break
	conn.commit()
	print('*****************************************')
	print('Inserted documents(rows) into trade,payment,trade_offer,offer')
	print('*****************************************')
 	

def insert_divident(items):
	for it in items:
		sq = f"INSERT INTO divident(item_id,yr2004,yr2005,yr2006,yr2007,yr2008,yr2009,yr2010,yr2011,yr2012,yr2013,yr2014,yr2015,yr2016,yr2017,yr2018,yr2019,yr2020,yr2021) VALUES "
		sq1 = f"('{it}',{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)},{random.randint(10,40)});"
		cursor.execute(sq+sq1)
	conn.commit()
	print('*****************************************')
	print('Inserted documents(rows) into Divident')
	print('*****************************************')	


def insert_research(items):
	for it in items:
		ch = random.randint(1,2)
		title = "First research"
		description = "This is the description. It is usually a lot longer than the title and contains information about the research that has been done"
		link = "https://google.com"
		author_name = "Ann"
		authorid = "author123"
		updated_date = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		id1 = getCode()
		sqm = "INSERT INTO research (ids,title,description,link,author_name,authorid,updated_date) VALUES "
		sq = f"('{id1}','{title}','{description}','{link}','{author_name}','{authorid}','{updated_date}');"
		cursor.execute(sqm+sq)
		cursor.execute(f"INSERT INTO item_research (item_id,ids) VALUES ('{it}','{id1}');")
		conn.commit()
		if ch != 1:
			title = "Second Research"
			author_name = "Sai"
			authorid = "author124"
			id2 = getCode()
			sq = f"('{id2}','{title}','{description}','{link}','{author_name}','{authorid}','{updated_date}');"
			cursor.execute(sqm+sq)
			cursor.execute(f"INSERT INTO item_research (item_id,ids) VALUES ('{it}','{id2}');")
	conn.commit()
	print('*****************************************')
	print('Inserted documents(rows) into Research')
	print('*****************************************')


def gen_all():
	iu = insert_users()
	insert_address(iu)
	insert_bank(iu)
	insert_currency()
	items = insert_price_item()
	insert_rest(iu)
	insert_divident(items)
	insert_research(items)


gen_all()
cursor.execute("set foreign_key_checks=1;")
conn.commit()
conn.close()


'''



RDS:
Username: root
Password: rootroot
Port: 3306
DB Name : ring


Redshift:
DB Name: dev
Port: 5439
Username: awsuser
Password: aws()User1


export PATH=$PATH:/Applications/MySQLWorkbench.app/Contents/MacOS

Staging-Initial -

Staging-User-

mysql -u root -p --database=ringer --host=ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com --port=3306 --batch -e "select u.user_id,u.first_name,u.last_name,u.username,u.email,u.wallet,DATE(u.DOB),u.gender,DATE(u.updated_date),a.add_id,a.type,a.street_address,a.city,a.state,a.zipcode,b.bank_id,DATE(b.exp_date),i.inven_id,i.item_id,i.bought_price,i.quantity from user_data u join bank b on u.user_id = b.user_id join address a on u.user_id = a.user_id join inventory i on u.user_id = i.user_id WHERE u.updated_date > date_sub(curdate(),interval 30 day) or b.updated_date > date_sub(curdate(),interval 30 day) or a.updated_date > date_sub(curdate(),interval 30 day) or i.updated_date > date_sub(curdate(),interval 30 day);" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > user_bank_add_inven.csv

Staging-Trade-

mysql -u root -p --database=ringer --host=ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com --port=3306 --batch -e "select t.trade_id,t.quantity,t.unit_price,DATE(t.updated_date),t.buyer_id,t.seller_id,p.pay_id,p.amount,o.offer_id,ROUND(o.quantity,3) as "totalquantity",o.buy_sell,o.price,u.user_id, a.add_id,b.bank_id,i.inven_id,t.item_id,it.price_id from trade t,trade_offer tto,offer o,payment p ,user_data u, address a, bank b, inventory i, item it WHERE (t.pay_id = p.pay_id and tto.trade_id = t.trade_id and tto.offer_id = o.offer_id and (u.user_id=t.buyer_id or u.user_id=t.seller_id) and (a.user_id=t.buyer_id or a.user_id=t.seller_id) and (b.user_id=t.buyer_id or b.user_id=t.seller_id) and (i.user_id=t.buyer_id or i.user_id=t.seller_id) and (t.item_id=it.item_id)) and (t.updated_date > date_sub(curdate(),interval 30 day) or p.updated_date > date_sub(curdate(),interval 30 day) or o.updated_date > date_sub(curdate(),interval 30 day));" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > trade_pay_offer.csv



Staging-item -

mysql -u root -p --database=ringer --host=ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com --port=3306 --batch -e "select i.item_id,i.code,i.name,p.price_id,p.buy,p.sell,DATE(p.updated_date) from item i join price p on p.price_id = i.price_id WHERE i.updated_date > date_sub(curdate(),interval 30 day) or p.updated_date > date_sub(curdate(),interval 30 day);" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > item_price.csv





COPY public.user_data from 's3://ringer-csv/initialload/user_bank_add_inven.csv' iam_role 'arn:aws:iam::903662732244:role/redshiftfullaccess' IGNOREHEADER 1 TIMEFORMAT 'auto' csv;

COPY public.trade from 's3://ringer-csv/initialload/trade_pay_offer.csv' iam_role 'arn:aws:iam::903662732244:role/redshiftfullaccess' IGNOREHEADER 1 TIMEFORMAT 'auto' csv;

COPY public.item from 's3://ringer-csv/initialload/item_price.csv' iam_role 'arn:aws:iam::903662732244:role/redshiftfullaccess' IGNOREHEADER 1 TIMEFORMAT 'auto' csv;




Incremental Load:-


USER-

mysql -u root -p --database=ringer --host=ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com --port=3306 --batch -e "select u.user_id,u.first_name,u.last_name,u.username,u.email,u.wallet,DATE(u.DOB),u.gender,DATE(u.updated_date),a.add_id,a.type,a.street_address,a.city,a.state,a.zipcode,b.bank_id,DATE(b.exp_date),i.inven_id,i.item_id,i.bought_price,i.quantity from user_data u join bank b on u.user_id = b.user_id join address a on u.user_id = a.user_id join inventory i on u.user_id = i.user_id WHERE u.updated_date > date_sub(curdate(),interval 0.5 day) or b.updated_date > date_sub(curdate(),interval 0.5 day) or a.updated_date > date_sub(curdate(),interval 0.5 day) or i.updated_date > date_sub(curdate(),interval 0.5 day);" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > user_bank_add_inven.csv

truncate table user_datadw;

COPY public.user_datadw from 's3://ringer-csv/incrementalload/user_bank_add_inven.csv' iam_role 'arn:aws:iam::903662732244:role/redshiftfullaccess' IGNOREHEADER 1 TIMEFORMAT 'auto' csv;

create or replace PROCEDURE load_merge_user_dataDW() AS $$
DECLARE s record;
BEGIN
for s in (select * from user_datadw)
loop
    delete from user_data where user_id=s.user_id and email=s.email and bank_id=s.bank_id and add_id=s.add_id and inven_id=s.inven_id and item_id=s.item_id;
     INSERT into user_data(user_id,first_name,last_name,username,email,wallet,dob,gender,updated_date,add_id,type,street_address,city,state,zipcode,bank_id,exp_date,inven_id,item_id,bought_price,quantity) VALUES (s.user_id,s.first_name,s.last_name,s.username,s.email,s.wallet,s.dob,s.gender,s.updated_date,s.add_id,s.type,s.street_address,s.city,s.state,s.zipcode,s.bank_id,s.exp_date,s.inven_id,s.item_id,s.bought_price,s.quantity);
end loop;
end;
$$ LANGUAGE PLPGSQL;

call load_merge_user_dataDW()



Trade-

mysql -u root -p --database=ringer --host=ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com --port=3306 --batch -e "select t.trade_id,t.quantity,t.unit_price,DATE(t.updated_date),t.buyer_id,t.seller_id,p.pay_id,p.amount,o.offer_id,ROUND(o.quantity,3) as "totalquantity",o.buy_sell,o.price,u.user_id, a.add_id,b.bank_id,i.inven_id,t.item_id,it.price_id from trade t,trade_offer tto,offer o,payment p ,user_data u, address a, bank b, inventory i, item it WHERE (t.pay_id = p.pay_id and tto.trade_id = t.trade_id and tto.offer_id = o.offer_id and (u.user_id=t.buyer_id or u.user_id=t.seller_id) and (a.user_id=t.buyer_id or a.user_id=t.seller_id) and (b.user_id=t.buyer_id or b.user_id=t.seller_id) and (i.user_id=t.buyer_id or i.user_id=t.seller_id) and (t.item_id=it.item_id)) and (t.updated_date > date_sub(curdate(),interval 0.5 day) or p.updated_date > date_sub(curdate(),interval 0.5 day) or o.updated_date > date_sub(curdate(),interval 0.5 day));" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > trade_pay_offer.csv

truncate table tradedw;
COPY public.tradedw from 's3://ringer-csv/incrementalload/trade_pay_offer.csv' iam_role 'arn:aws:iam::903662732244:role/redshiftfullaccess' IGNOREHEADER 1 TIMEFORMAT 'auto' csv;


create or replace PROCEDURE load_merge_tradeDW() AS $$
DECLARE s record;
BEGIN
for s in (select * from tradedw)
loop
    delete from trade where trade_id=s.trade_id and buyer_id=s.buyer_id and seller_id=s.seller_id and pay_id=s.pay_id and offer_id=s.offer_id and item_id=s.item_id and user_id=s.user_id and add_id=s.add_id and bank_id=s.bank_id and inven_id=s.inven_id and price_id=s.price_id;
     INSERT into trade(trade_id,quantity,unit_price,updated_date,buyer_id,seller_id,pay_id,amount,offer_id,total_quantity,buy_sell,price,user_id,add_id,bank_id,inven_id,item_id,price_id) VALUES (s.trade_id,s.quantity,s.unit_price,s.updated_date,s.buyer_id,s.seller_id,s.pay_id,s.amount,s.offer_id,s.total_quantity,s.buy_sell,s.price,s.user_id,s.add_id,s.bank_id,s.inven_id,s.item_id,s.price_id);
end loop;
end;
$$ LANGUAGE PLPGSQL;

call load_merge_tradeDW()


item-

mysql -u root -p --database=ringer --host=ring.cpqiozbjlzz9.us-east-1.rds.amazonaws.com --port=3306 --batch -e "select i.item_id,i.code,i.name,p.price_id,p.buy,p.sell,DATE(p.updated_date) from item i join price p on p.price_id = i.price_id WHERE i.updated_date > date_sub(curdate(),interval 0.5 day) or p.updated_date > date_sub(curdate(),interval 0.5 day);" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > item_price.csv

truncate table itemdw;
COPY public.itemdw from 's3://ringer-csv/incrementalload/item_price.csv' iam_role 'arn:aws:iam::903662732244:role/redshiftfullaccess' IGNOREHEADER 1 TIMEFORMAT 'auto' csv;

create or replace PROCEDURE load_merge_itemDW() AS $$
DECLARE s record;
BEGIN
for s in (select * from itemdw)
loop
    delete from item where item_id=s.item_id and price_id=s.price_id;
     INSERT into item(item_id,code,name,price_id,buy,sell,updated_date) VALUES (s.item_id,s.code,s.name,s.price_id,s.buy,s.sell,s.updated_date);
end loop;
end;
$$ LANGUAGE PLPGSQL;

call load_merge_itemDW()


------------------------------------



SHOW VARIABLES LIKE "secure_file_priv";


select u.user_id,u.first_name,u.last_name,u.username,u.email,u.wallet,u.DOB,u.gender,u.updated_date,
b.bank_id,b.exp_date,b.updated_date,a.add_id,a.type,a.street_address,a.city,a.state,a.zipcode,a.updated_date,
i.inven_id,i.item_id,i.bought_price,i.quantity,i.updated_date 
into outfile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\user_bank_add_inven.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY ''
LINES TERMINATED BY '\n'
from user_data u join bank b on u.user_id = b.user_id join address a on u.user_id = a.user_id join inventory i on u.user_id = i.user_id
 WHERE u.updated_date > date_sub(curdate(),interval 30 day) or b.updated_date > date_sub(curdate(),interval 30 day) or
        a.updated_date > date_sub(curdate(),interval 30 day) or i.updated_date > date_sub(curdate(),interval 30 day);


select t.trade_id,t.quantity,t.unit_price,t.buyer_id,t.seller_id,t.updated_date,p.pay_id,p.amount,p.updated_date,
o.offer_id,o.quantity,o.buy_sell,o.price,o.updated_date 
into outfile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\trade_pay_offer.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY ''
LINES TERMINATED BY '\n'
from trade t join payment p on t.pay_id = p.pay_id join trade_offer tto on tto.trade_id = t.trade_id 
join offer o on tto.offer_id = o.offer_id
 WHERE t.updated_date > date_sub(curdate(),interval 30 day) or p.updated_date > date_sub(curdate(),interval 30 day) or
        o.updated_date > date_sub(curdate(),interval 30 day);



select i.item_id,i.code,i.name,i.updated_date,p.price_id,p.buy,p.sell,p.updated_date
into outfile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\item_price.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY ''
LINES TERMINATED BY '\n'
from item i join price p on p.price_id = i.price_id
WHERE i.updated_date > date_sub(curdate(),interval 30 day) or p.updated_date > date_sub(curdate(),interval 30 day);

CREATE TABLE price_history (
	pid MEDIUMINT NOT NULL AUTO_INCREMENT,
	price_id VARCHAR(10) NOT NULL,
	buy           DECIMAL(10, 3) NOT NULL,
    sell          DECIMAL(10, 3) NOT NULL,
    ts            DATETIME NOT NULL,
    updated_date  DATETIME NOT NULL,
    PRIMARY KEY (pid)
);
ALTER TABLE price_history AUTO_INCREMENT=100;


CREATE DEFINER=`root`@`localhost` TRIGGER `price_BEFORE_UPDATE` BEFORE UPDATE ON `price` FOR EACH ROW BEGIN
  INSERT INTO Price_History(price_id,buy,sell,ts,updated_date) SELECT price_id,buy,sell,ts,updated_date FROM price WHERE price_id=OLD.price_id;
  update Price_History 
  set updated_date=current_timestamp()
  where price_id=old.price_id;
END




-- set foreign_key_checks=0;
-- truncate table address;
-- truncate table bank;
-- truncate table currencies;
-- truncate table inventory;
-- truncate table item;
-- truncate table offer;
-- truncate table payment;
-- truncate table price;
-- truncate table trade;
-- truncate table trade_offer;
-- truncate table user_data;
-- set foreign_key_checks=1;







'''