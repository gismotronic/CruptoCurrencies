#!/usr/bin/env python

# BTC: 1PhMJdUpt9ER6czcXcr2dRCBhZewFmVpXq
#           Thank You

import hashlib
import hmac
import httplib
import json
import time
import urllib
import urllib2

class Btce(object):
   def __init__(self):
      self.key        = 'Your Key'
      self.secret     = 'Your Secret'
      self.nonceCount = time.time()
   def getNonce(self):
      self.nonceCount += 1
      return self.nonceCount

   # https://btc-e.com/api/3/docs#main
   def publicInfo(self):
      response = urllib2.urlopen('https://btc-e.com/api/3/info')
      html = response.read()
      data = eval(html)
      return data
   def publicTicker(self, coin, base='usd'):
      url = 'https://btc-e.com/api/3/ticker/' + coin + '_' + base
      response = urllib2.urlopen(url)
      html = response.read()
      data = eval(html)
      return data
   def publicDepth(self, coin, base='usd'):
      url = 'https://btc-e.com/api/3/depth/' + coin + '_' + base
      response = urllib2.urlopen(url)
      html = response.read()
      data = eval(html)
      return data
   def publicTrades(self, coin, base='usd'):
      url = 'https://btc-e.com/api/3/trades/' + coin + '_' + base
      response = urllib2.urlopen(url)
      html = response.read()
      data = eval(html)
      return data

   # https://btc-e.com/api/documentation
   def getInfo(self):
      nonce = getNonce()
      # method name and nonce go into the POST parameters
      params = {'method':'getInfo',
                'nonce': nonce}
      params = urllib.urlencode(params)
      # Hash the params string to produce the sign header value
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type' : 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data
   def transHistory(self):
      nonce = getNonce()
      params = {'method':'TransHistory',
                'nonce': nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data
   def tradeHistory(self):
      nonce = getNonce()
      params = {'method':'TradeHistory',
                'nonce': nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data
   def activeOrders(self):
      nonce = getNonce()
      params = {'method':'ActiveOrders',
                'nonce': nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data
   def buy(self, coin, amount, price, base='usd'):
      nonce = getNonce()
      coin  = coin.lower()
      base  = base.lower()
      pair  = coin + '_' + base
      params = {'method':'Trade',
                'pair'  : pair,
                'type'  :'buy',
                'rate'  : price,
                'amount': amount,
                'nonce' : nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data['success']
   def sell(self, coin, amount, price, base='usd'):
      nonce = getNonce()
      coin  = coin.lower()
      base  = base.lower()
      pair  = coin + '_' + base
      params = {'method':'Trade',
                'pair'  : pair,
                'type'  :'sell',
                'rate'  : price,
                'amount': amount,
                'nonce' : nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data['success']
   def cancelOrder(self, orderId):#
      nonce = getNonce()
      params = {'method':'CancelOrder',
                'order_id': orderId,
                'nonce' : nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data['success']

   # https://btc-e.com/tapi/docs#main
   def orderInfo(self, orderId):
      nonce = getNonce()
      params = {'method'  : 'OrderInfo',
                'order_id': orderId,
                'nonce'   : nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      if data['success'] == 1: return data['return']['address']
      else:                    return ''
   def coinDepositAddress(self, coin):
      nonce = getNonce()
      coin = coin.upper()
      params = {'method'  : 'CoinDepositAddress',
                'coinName': coin,
                'nonce'   : nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      if data['success'] == 1: return data['return']['address']
      else:                    return ''
   def withdrawCoin(self, coin, quantity, address):
      nonce = getNonce()
      coin = coin.upper()
      params = {'method'  : 'WithdrawCoin',
                'coinName': coin,
                'amount'  : quantity,
                'address' : address,
                'nonce'   : nonce}
      params = urllib.urlencode(params)
      hMac = hmac.new(self.secret, digestmod=hashlib.sha512)
      hMac.update(params)
      sign = hMac.hexdigest()
      headers = {'Content-type': 'application/x-www-form-urlencoded',
      		     'Key' : self.key, 'Sign' : sign}
      conn = httplib.HTTPSConnection('btc-e.com')
      conn.request('POST', '/tapi', params, headers)
      response = conn.getresponse()
      data = json.load(response)
      conn.close()
      return data['success']

