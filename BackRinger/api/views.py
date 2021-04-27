from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *

from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView 

import mysql.connector
import random
import string
import hashlib
import datetime as dt
import sys



# list - GET
# create - POST
# retrieve - GET with pk
# update - HTTP PUT with pk
# partial_update - PATCH with pk 
# destroy - HTTP DELETE


#establishing the connection
conn = mysql.connector.connect(
   user='root', password='rootroot', host='127.0.0.1', database='ringer',auth_plugin='mysql_native_password')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()





# index = never_cache(TemplateView.as_view(template_name="index.html"))


def getCode(length = 10, char = string.ascii_uppercase +
                          string.digits +           
                          string.ascii_lowercase ):
    return ''.join(random.choice(char) for x in range(length))




class CurrViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all()
    serializer_class = CurrSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class InvenViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InvenSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def retrieve(self,request,pk=None):
        print('Retrive Called')
        a = cursor.execute(f"SELECT * FROM inventory WHERE user_id='{pk}';")
        a = a[0]
        b = cursor.execute(f"SELECT * FROM item WHERE item_id='{a[1]}';")
        res = {}
        res['bought_price'] = a[2]
        res['quantity'] = a[3]
        res['name'] = b[0][2]
        return Response(data=res)
    def list(self,request):
        # print('Its List',request.data['pk'])
        print('list called for fetching inventory of a particular user')
        pk = request.data['pk']
        cursor.execute(f"SELECT * FROM inventory WHERE user_id='{pk}';")
        a = cursor.fetchall()
        # print('a-----',a)
        ans = []
        for it in a:
            cursor.execute(f"SELECT * FROM item WHERE item_id='{it[1]}';")
            b = cursor.fetchall()
            res = {}
            res['bought_price'] = it[2]
            res['quantity'] = it[3]
            res['name'] = b[0][2]
            ans.append(res)
        return Response(data=ans)
        # return HttpResponse()
    def update(self,request,pk):
        print('Its Update')
        return HttpResponse()
    def create(self,request,pk):
        print('Its Create')
        return HttpResponse()
    def partial_update(self,request,pk):
        print('Its Partial Update')
        return HttpResponse()
    def destroy(self,request,pk):
        print('Its Delete')
        return HttpResponse()



class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def create(self,request):
        quantity = requst.data['quantity']
        buy_sell = request.data['buy_sell']
        price = request.data['price']
        item_id = request.data['item_id']
        un = request.data['un']
        opp = 'buyer_id' if buy_sell == 'B' else 'seller_id'
        if opp == 'buyer_id': # User Buying

            cursor.execute(f"""SELECT * from trade where {opp} = '1' and seller_id <> '1' and unit_price <= {price} and item_id='{item_id}' and pay_id='1';""")
            a = cursor.fetchall()
            # print(a)
            if len(a) == 0:
                # cursor.execute(f"""INSERT INTO offer VALUES ('{getCode(10)}',{quantity},{buy_sell},{price},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{quantity},{price},'{item_id}','{un}','1','1','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")		
            else:
                for e in a:
                    # the row has less items than required
                    if e[1] < quantity: 
                        quantity -= e[1]
                        # cursor.execute(f"""UPDATE offer set buy_sell='{'D'}' WHERE offer_id={e[0]};""")
                        # Include in payment
                        amount = e[1]*e[2]
                        iddd = getCode(10) # PaymentID
                        cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade
                        cursor.execute(f"""UPDATE trade SET buyer_id='{un}',pay_id='{iddd}',updated_date='{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
                        # Include in Offer
                        offer_id = getCode(10)
                        # BuySell - D is done, price is total amount
                        cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade_offer
                        cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
                        # Updating inventory
                        cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
                        there = cursor.fetchall()
                        if len(there) == 0:
                            # print(f"""INSERT INTO inventory(inven_id,item_id,bought_price,quantity,user_id,updated_date) VALUES('{getCode(10)}','{item_id}',{price},{e[1]},'{un}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                            cursor.execute(f"""INSERT INTO inventory(inven_id,item_id,bought_price,quantity,user_id,updated_date) VALUES('{getCode(10)}','{item_id}',{price},{e[1]},'{un}','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        else:
                            cursor.execute(f"""UPDATE inventory SET bought_price={price},quantity = quantity + {e[1]},updated_date = '{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
                    else:
                        remain = e[1] - quantity
                        amount = quantity*e[2]
                        iddd = getCode(10) # PaymentID
                        cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade
                        cursor.execute(f"""UPDATE trade SET buyer_id='{un}',pay_id='{iddd}',updated_date='{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
                        if remain != 0:
                            cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{remain},{e[2]},'{e[4]}','1','{un}','1','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in Offer
                        offer_id = getCode(10)
                        # BuySell - D is done, price is total amount
                        cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade_offer
                        cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
                        # Updating inventory
                        cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
                        there = cursor.fetchall()
                        if len(there) == 0:
                            cursor.execute(f"""INSERT INTO inventory(inven_id,item_id,bought_price,quantity,user_id,updated_date) VALUES('{getCode(10)}','{item_id}',{price},{e[1]},'{un}','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        else:
                            # print(type(e[1]),e[1],'233')
                            # print(f"""UPDATE inventory SET bought_price={str(round(price,2))},quantity = quantity + {str(round(e[1],2))},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = {there[0][0]};""")
                            cursor.execute(f"""UPDATE inventory SET bought_price={str(round(price,2))},quantity = quantity + {str(round(e[1],2))},updated_date = '{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
                        break
        else: # User Selling
            cursor.execute(f"""SELECT * from trade where {opp}='1' and buyer_id <> '1' and unit_price >= {price} and item_id='{item_id}' and pay_id='1';""")
            a = cursor.fetchall()
            if len(a) == 0:
                # cursor.execute(f"""INSERT INTO offer VALUES ('{getCode(10)}',{quantity},{buy_sell},{price},'{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{quantity},{price},'{item_id}','1','{un}','1','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")		
            else:
                for e in a:
                    # the row has less items than required
                    if e[1] < quantity: 
                        quantity += e[1]
                        # cursor.execute(f"""UPDATE offer set buy_sell='{'D'}' WHERE offer_id={e[0]};""")
                        # Include in payment
                        amount = e[1]*e[2]
                        iddd = getCode(10) # PaymentID
                        cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade
                        cursor.execute(f"""UPDATE trade SET seller_id='{un}',pay_id='{iddd}',updated_date='{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
                        # Include in Offer
                        offer_id = getCode(10)
                        # BuySell - D is done, price is total amount
                        cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade_offer
                        cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
                        # Updating inventory
                        cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
                        there = cursor.fetchall()
                        cursor.execute(f"""UPDATE inventory SET bought_price={price},quantity = quantity + {e[1]},updated_date = '{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
                    else:
                        remain = e[1] - quantity
                        amount = quantity*e[2]
                        iddd = getCode(10) # PaymentID
                        cursor.execute(f"""INSERT INTO payment VALUES ('{iddd}',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade
                        cursor.execute(f"""UPDATE trade SET seller_id='{un}',pay_id='{iddd}',updated_date='{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE trade_id='{e[0]}';""") 
                        if remain != 0:
                            cursor.execute(f"""INSERT INTO trade(trade_id,quantity,unit_price,item_id,buyer_id,seller_id,pay_id,updated_date) VALUES ('{getCode(10)}',{remain},{e[2]},'{e[4]}','{un}',1,1,'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in Offer
                        offer_id = getCode(10)
                        # BuySell - D is done, price is total amount
                        cursor.execute(f"""INSERT INTO offer VALUES ('{offer_id}',{e[1]},'D',{amount},'{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');""")
                        # Include in trade_offer
                        cursor.execute(f"""INSERT INTO trade_offer(pri,offer_id,trade_id) VALUES ('{getCode(10)}','{offer_id}','{e[0]}');""")
                        # Updating inventory
                        cursor.execute(f"""SELECT * from inventory where user_id='{un}' and item_id='{item_id}';""")
                        there = cursor.fetchall()
                        # print(e[1],type(e[1]),'282')
                        # print(f"""UPDATE inventory SET bought_price={price},quantity = quantity - {str(e[1])},updated_date = '{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = {there[0][0]};""")
                        cursor.execute(f"""UPDATE inventory SET bought_price={price},quantity = quantity + {str(e[1])},updated_date = '{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' where inven_id = '{there[0][0]}';""")
                        break
        conn.commit()



class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)




class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def list(self,request):
        stocks = []
        qs = Price.objects.values()
        # qi = Item.objects.values()
        # print(qs)
        for q in qs:
            rep = {}
            queryset2 = Item.objects.filter(price_id=q["price_id"]).values()
            # print('Queryset2-------------',queryset2)
            # rep[queryset2[0]["code"]] = [q["buy"],q["sell"]]
            # print('q--------',q)
            queryset2 = queryset2[0]
            rep['name'] = queryset2['name']
            rep['ticker'] = queryset2['code']
            rep['bid'] = q['buy']
            rep['ask'] = q['sell']
            rep['sector'] = queryset2['sector']
            rep['homepage'] = queryset2['homepage']
            rep['investorpage'] = queryset2['investorpage']
            rep['pe'] = queryset2['pe']
            # rep['divident'] = {}
            div = {}
            rep['change'] = q['changeper']
            qd = Divident.objects.filter(item_id=queryset2['item_id']).values()
            qd = qd[0]
            # print('qd-------',qd)
            div[2004] = qd['yr2004']
            div[2005] = qd['yr2005']
            div[2006] = qd['yr2006']
            div[2007] = qd['yr2007']
            div[2008] = qd['yr2008']
            div[2009] = qd['yr2009']
            div[2010] = qd['yr2010']
            div[2011] = qd['yr2011']
            div[2012] = qd['yr2012']
            div[2013] = qd['yr2013']
            div[2014] = qd['yr2014']
            div[2015] = qd['yr2015']
            div[2016] = qd['yr2016']
            div[2017] = qd['yr2017']
            div[2018] = qd['yr2018']
            div[2019] = qd['yr2019']
            div[2020] = qd['yr2020']
            div[2021] = qd['yr2021']
            rep['divident'] = div
            rep['research'] = []
            cursor.execute(f"SELECT * FROM research r JOIN item_research i on i.ids = r.ids WHERE item_id='{queryset2['item_id']}';")
            rss = cursor.fetchall() # ids, title,description,link,author_name,authorid,updated_date,item_id,ids
            for r in rss:
                re = {}
                re['title'] = r[1]
                re['description'] = r[2]
                re['link'] = r[3]
                re['author'] = { 'name': r[4], 'authorId' : r[5] }
                re['id'] = r[0]
                rep['research'].append(re)
            stocks.append(rep)
        print("Fetching done")
        return Response(data=stocks)




class UserDataViewSet(viewsets.ViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerial
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def create(self,request):
        if 'pk' not in request.data:
            print('Creating:-')
            # print(request.data)
            d = {}
            c = getCode()
            q = UserData.objects.raw("SELECT user_id FROM user_data")
            # print('q-----',q)
            while c in q:
                c = getCode()
            tom = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # em = request.data['user']['email']
            em = request.data['email']
            cursor.execute(f"INSERT INTO user_data(user_id,first_name,last_name,username,password,email,wallet,dob,gender,time_registered,updated_date) VALUES ('{c}','xxxx','xxxx','xxxxxxxx','xxxx','{em}',10000,'{tom}','U','{tom}','{tom}');")

            #Address
            a = getCode()
            aa = Address.objects.raw("SELECT add_id FROM address")
            while a in aa:
                a = getCode()

            cursor.execute(f"INSERT INTO address(add_id,type,street_address,city,state,zipcode,updated_date,user_id) VALUES ('{a}','home','xxxx','xxxx','xx',0,'{tom}','{c}');")



            b = {}
            bc = getCode()
            bb = Bank.objects.raw("SELECT bank_id FROM bank")
            while bc in bb:
                bc = getCode()
            cursor.execute(f"INSERT INTO BANK(bank_id,card_no,exp_date,cvv,name,defa,updated_date,user_id) VALUES ('{bc}',0,'{tom}',0,'xxxx','Y','{tom}','{c}');")
            conn.commit()

        else:
            print('Updating:-')
            pk = request.data['pk']
            #User
            cursor.execute(f"SELECT * FROM user_data WHERE user_id='{pk}';")
            us = cursor.fetchall()
            us = us[0]
            first_name = us[0]
            last_name = us[1]
            username = us[2]
            DOB = us[8]
            gender = us[9]
            updated_date = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(request.data['first_name']) != 0:
                first_name = request.data['first_name']
            if len(request.data['last_name']) != 0:
                last_name = request.data['last_name']
            if len(request.data['username']) != 0:
                username = request.data['username']
            if len(request.data['DOB']) != 0:
                DOB = request.data['DOB']
            if len(request.data['gender']) != 0:
                gender = request.data['gender']
            
            cursor.execute(f"UPDATE user_data SET first_name = '{first_name}',last_name = '{last_name}',username = '{username}',DOB = '{DOB}',gender = '{gender}',updated_date = '{updated_date}' WHERE user_id = '{pk}';")

            #Address
            cursor.execute(f"SELECT * FROM address where user_id='{pk}';")
            ar = cursor.fetchall()
            ar = ar[0]
            street_address = request.data['street_address']
            city = request.data['city']
            state = request.data['state']
            zipcode = request.data['zipcode']

            cursor.execute(f"UPDATE address SET street_address = '{street_address}',city='{city}',state='{state}',zipcode='{zipcode}',updated_date='{updated_date}' WHERE user_id='{pk}';")

            #Bank
            cursor.execute(f"SELECT * FROM bank WHERE user_id='{pk}';")
            br = cursor.fetchall()
            br = br[0]
            card_no = request.data['card_no']
            exp_date = request.data['exp_date']
            cvv = request.data['cvv']
            name = request.data['name']

            cursor.execute(f"UPDATE bank SET card_no='{card_no}',exp_date= STR_TO_DATE('{exp_date}', '%Y-%m-%d'),cvv='{cvv}',name='{name}',defa='Y',updated_date='{updated_date}' WHERE user_id='{pk}';")
            conn.commit()
        
        return HttpResponse()


    def update(self,request,pk=None):
        return HttpResponse()

    def partial_update(self,request,pk=None):
        if 'password' in request.data:
            connect.execute(f"UPDATE user_data SET password='{request.data['password']}' WHERE user_id='{pk}';")
            conn.commit()
        else: # Update Wallet Balance
            connect.execute(f"UPDATE user_data SET wallet = wallet + {request.data['amount']} WHERE user_id='{pk}';")
            conn.commit()
        return HttpResponse()

    def retrieve(self,request,pk=None):
        r = cursor.execute(f"SELECT * FROM user_data WHERE user_id='{pk}';")
        r = r[0]
        res['wallet'] = r[7]
        return Response(data=res)