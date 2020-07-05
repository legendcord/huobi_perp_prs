#!/usr/bin/env python
# -*- coding: utf-8 -*-

from restAPI.HuobiPerpService import HuobiPerp
from pprint import pprint
import setting

perp = HuobiPerp(setting.URL, setting.API_KEY, setting.API_SECRET)

#%%  market data api ===============

contract_code = "BTC-USD"

#print (u' 获取合约信息 ')
#pprint (perp.get_contract_info(contract_code=contract_code))

#print (u' 获取合约指数信息 ')
#pprint (perp.get_contract_index(contract_code))

#print (u' 获取合约最高限价和最低限价 ')
#pprint (perp.get_contract_price_limit(contract_code=contract_code))

#print (u' 获取当前可用合约总持仓量 ')
#pprint (perp.get_contract_open_interest(contract_code=contract_code))

#print (u' 获取行情深度数据 ')
#pprint (perp.get_contract_depth(contract_code=contract_code, type='step0'))

#print (u' 获取K线数据 ')
#pprint (perp.get_contract_kline(contract_code=contract_code, period='4hour', size=20))

#print (u' 获取聚合行情 ')
#pprint (perp.get_contract_market_merged(contract_code))

#print (u' 获取市场最近成交记录 ')
#pprint (perp.get_contract_trade(contract_code))

#print (u' 批量获取最近的交易记录 ')
#pprint (perp.get_contract_batch_trade(contract_code=contract_code, size=5))

#print (u' 查询合约风险准备金余额和预估分摊比例 ')
#pprint (perp.get_contract_risk_info(contract_code=contract_code))

#print(u' 查询合约风险准备金余额历史数据 ')
#pprint (perp.get_contract_insurance_fund(contract_code=contract_code))

#print(u' 查询平台阶梯调整系数 ')
#print(perp.get_contract_adjustfactor(contract_code=contract_code))

#print(perp.get_contract_his_open_interest(contract_code=contract_code, period='4hour', amount_type=1))


#%% trade / account api  ===============

'''
print (u' 获取用户账户信息 ')
pprint (perp.get_contract_account_info())
pprint (perp.get_contract_account_info("BTC"))

print (u' 获取用户持仓信息 ')
pprint (perp.get_contract_position_info())
pprint (perp.get_contract_position_info("BTC"))

print (u' 合约下单 ')
pprint(perp.send_contract_order(symbol='', contract_type='', contract_code='BTC181228', 
                        client_order_id='', price=10000, volume=1, direction='sell',
                        offset='open', lever_rate=5, order_price_type='limit'))


print (u' 合约批量下单 ')
orders_data = {'orders_data': [
               {'symbol': 'BTC', 'contract_type': 'quarter',  
                'contract_code':'BTC181228',  'client_order_id':'', 
                'price':10000, 'volume':1, 'direction':'sell', 'offset':'open', 
                'leverRate':5, 'orderPriceType':'limit'},
               {'symbol': 'BTC','contract_type': 'quarter', 
                'contract_code':'BTC181228', 'client_order_id':'', 
                'price':20000, 'volume':2, 'direction':'sell', 'offset':'open', 
                'leverRate':5, 'orderPriceType':'limit'}]}
pprint(perp.send_contract_batchorder(orders_data))


print (u' 撤销订单 ')
pprint(perp.cancel_contract_order(symbol='BTC', order_id='42652161'))

print (u' 全部撤单 ')
pprint(perp.cancel_all_contract_order(symbol='BTC'))

print (u' 获取合约订单信息 ')
pprint(perp.get_contract_order_info(symbol='BTC', order_id='42652161'))

print (u' 获取合约订单明细信息 ')
pprint(perp.get_contract_order_detail(symbol='BTC', order_id='42652161', order_type=1, created_at=1542097630215))

print (u' 获取合约当前未成交委托 ')
pprint(perp.get_contract_open_orders(symbol='BTC'))

print (u' 获取合约历史委托 ')
pprint (perp.get_contract_history_orders(symbol='BTC', trade_type=0, type=1, status=0, create_date=7))
'''


