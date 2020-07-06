#!/usr/bin/env python
# -*- coding: utf-8 -*-

from restAPI.HuobiPerpService import HuobiPerp
from pprint import pprint
#import setting_btc
import setting

contract_code = "BTC-USD"
#perp = HuobiPerp(setting_btc.URL, setting_btc.API_KEY, setting_btc.API_SECRET)

contract_code = "ETH-USD"
perp = HuobiPerp(setting.URL, setting.API_KEY, setting.API_SECRET)

#%%  market data api ===============

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
#pprint(perp.get_contract_adjustfactor(contract_code=contract_code))

#pprint(perp.get_contract_his_open_interest(contract_code=contract_code, period='4hour', amount_type=1))

#print(u ' 精英账户多空持仓对比-账户数 ')
#pprint(perp.get_contract_elite_account_ratio(contract_code=contract_code, period='4hour'))

#print(u ' 精英账户多空持仓对比-持仓量 ')
#pprint(perp.get_contract_elite_position_ratio(contract_code=contract_code, period='4hour'))

#print(u ' 查询系统状态 ')
#pprint(perp.get_api_state(contract_code=contract_code))

#print(u ' 获取合约的资金费率 ')
#pprint(perp.get_funding_rate(contract_code=contract_code))

#print(u ' 获取强平订单 ')
#pprint(perp.get_liquidation_orders(contract_code=contract_code, ...))



#%% trade / account api  ===============

#print (u' 获取用户账户信息 ')
#pprint (perp.get_contract_account_info())
#pprint (perp.get_contract_account_info(contract_code))

#print (u' 获取用户持仓信息 ')
#pprint (perp.get_contract_position_info())
#pprint (perp.get_contract_position_info(contract_code))

#pprint (perp.get_contract_account_position_info(contract_code))


#print (u' 合约下单 ')
#pprint(perp.send_contract_order(contract_code=contract_code, 
#                        client_order_id='', price=250, volume=1, direction='sell',
#                        offset='open', lever_rate=5, order_price_type='limit'))

#print (u' 合约批量下单 ')
#orders_data = {'orders_data': [
#               {'contract_code':contract_code,  'client_order_id':'', 
#                'price':250, 'volume':1, 'direction':'sell', 'offset':'open', 
#                'leverRate':5, 'orderPriceType':'limit'},
#               {'contract_code':contract_code, 'client_order_id':'', 
#                'price':260, 'volume':2, 'direction':'sell', 'offset':'open', 
#                'leverRate':5, 'orderPriceType':'limit'}]}
#pprint(perp.send_contract_batchorder(orders_data))

#print (u' 撤销订单 ')
#pprint(perp.cancel_contract_order(contract_code, order_id='729668420622188546'))

#print (u' 全部撤单 ')
#pprint(perp.cancel_all_contract_order(contract_code))

#print (u' 获取合约订单信息 ')
#pprint(perp.get_contract_order_info(contract_code, order_id='729668420622188546'))

#print (u' 获取合约订单明细信息 ')
#pprint(perp.get_contract_order_detail(contract_code, order_id='729668420622188546', order_type=1, created_at=1594008108061))
#pprint(perp.get_contract_order_detail(contract_code, order_id='729668420622188546', order_type=1))

#print (u' 获取合约当前未成交委托 ')
#pprint(perp.get_contract_open_orders(contract_code))

#print (u' 获取合约历史委托 ')
#pprint (perp.get_contract_history_orders(contract_code, trade_type=0, type=1, status=0, create_date=7))

#print(u' 合约计划委托下单 ')
#pprint(perp.send_contract_trigger_order(contract_code=contract_code, trigger_type="ge", trigger_price=250,
#                                        order_price_type='optimal_20', volume=1, direction="buy", offset="open", lever_rate=5))

#print(u' 合约计划委托撤单 ')
#pprint(perp.cancel_trigger_contract_order(contract_code=contract_code, order_id=1909842))

#pprint(perp.cancel_all_trigger_contract_order(contract_code))

#print(u' 获取计划委托当前委托 ')
#pprint(perp.get_contract_open_trigger_orders(contract_code, page_index=1, page_size=20))

#print(u' trigger order history ')
#pprint(perp.get_contract_history_trigger_orders(contract_code, trade_type=0, status=0, create_date=90))

#print(u' 闪电平仓下单')
#pprint(perp.lightning_close_position(contract_code, 1, "buy"))
