#!/usr/bin/env python
# -*- coding: utf-8 -*-
# copied from huobi github
# modified by haha

from restAPI.HuobiUtil import http_get_request, api_key_post

class HuobiPerp:

    def __init__(self,url,access_key,secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key
    
    '''
    ======================
    Market data API
    ======================
    '''

    # 获取合约信息
    def get_contract_info(self, contract_code=''):
        """
        参数名称         参数类型  必填    描述
        contract_code   string  false   BTC-USD(either lower or upper cases)
        note：if contract_code is empty，get all contracts info
        """
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
    
        url = self.__url + '/swap-api/v1/swap_contract_info'
        return http_get_request(url, params)
    
    
    # 获取合约指数信息
    def get_contract_index(self, contract_code=''):
        """
        "contract_code   BTC-USD
        """
        params = {'contract_code': contract_code}
    
        url = self.__url + '/swap-api/v1/swap_index'
        return http_get_request(url, params)
    
    
    # 获取合约最高限价和最低限价
    def get_contract_price_limit(self, contract_code=''):
        """
        "contract_code   BTC-USD
        """
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
    
        url = self.__url + '/swap-api/v1/swap_price_limit'
        return http_get_request(url, params)
    
    
    # 获取当前可用合约总持仓量
    def get_contract_open_interest(self, contract_code=''):
        """
        "contract_code   BTC-USD
        """
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
    
        url = self.__url + '/swap-api/v1/swap_open_interest'
        return http_get_request(url, params)   
        
    
    # 获取行情深度
    def get_contract_depth(self, contract_code, type):
        """
        :contract_code:   BTC-USD
        :`type: 可选值：(150档数据) step0, step1, step2, step3, step4, step5（合并深度1-5）；step0时，不合并深度, (20档数据) step6, step7, step8, step9, step10, step11（合并深度7-11）；step6时，不合并深度
        """
        params = {'contract_code': contract_code,
                  'type': type}
    
        url = self.__url + '/swap-ex/market/depth'
        return http_get_request(url, params)
    
    
    # 获取KLine
    def get_contract_kline(self, contract_code, period, size=150):
        """
        :param contract_code  BTC-USD , ...
        :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1week, 1mon }
        :param size: [1,2000]
        :return: this returns PARTIAL kline data
        """
        params = {'contract_code': contract_code,
                  'period': period}
        if size:
            params['size'] = size
    
        url = self.__url + '/swap-ex/market/history/kline'
        return http_get_request(url, params)
    
    
    # 获取聚合行情
    def get_contract_market_merged(self, contract_code):
        """
        :contract_code	    "BTC-USD", ...
        """
        params = {'contract_code': contract_code}
    
        url = self.__url + '/swap-ex/market/detail/merged'
        return http_get_request(url, params)
    
    
    # 获取市场最近成交记录
    def get_contract_trade(self, contract_code):
        """
        :param contract_code: 可选值：{ BTC-USD, etc. }
        :return:
        """
        params = {'contract_code': contract_code}
    
        url = self.__url + '/swap-ex/market/trade'
        return http_get_request(url, params)
    
    
    # 批量获取最近的交易记录
    def get_contract_batch_trade(self, contract_code, size=1):
        """
        :param contract_code: 可选值：{ BTC-USD, etc. }, size: int
        :return:
        """
        params = {'contract_code': contract_code,
                  'size' : size}
    
        url = self.__url + '/swap-ex/market/history/trade'
        return http_get_request(url, params)
    
    # 查询合约风险准备金余额和预估分摊比例
    def get_contract_risk_info(self, contract_code=''):
        params = {}
        if contract_code:
            params["contract_code"] = contract_code

        url = self.__url + '/swap-api/v1/swap_risk_info'
        return http_get_request(url, params)
            

    # 查询合约风险准备金余额历史数据
    def get_contract_insurance_fund(self, contract_code, page_index=1, page_size=100):
        params = {'contract_code': contract_code}
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
            
        url = self.__url + '/swap-api/v1/swap_insurance_fund'
        return http_get_request(url, params)


    # 查询平台阶梯调整系数
    def get_contract_adjustfactor(self, contract_code):
        params = {'contract_code': contract_code}
        
        url = self.__url + '/swap-api/v1/swap_adjustfactor'
        return http_get_request(url, params)


    def get_contract_his_open_interest(self, contract_code, period, amount_type, size=48):
        """
        :param period: '60min', '4hour', '12hour', '1day'
        :param amount_type 1:number of contract, 2:number of coins
        :size [1, 200]
        """
        params = {'contract_code':contract_code,
                  'period':period,
                  'amount_type':amount_type}
        if size:
            params['size'] = size

        url = self.__url + '/swap-api/v1/swap_his_open_interest'
        return http_get_request(url, params)


    # 精英账户多空持仓对比-账户数
    def get_contract_elite_account_ratio(self, contract_code, period):
        """
        :param contract_code BTC-USD
        :param period: 5min, 15min, 30min, 60min, 4hour, '1day'
        """
        params = {'contract_code':contract_code,
                  'period':period}        

        url = self.__url + '/swap-api/v1/swap_elite_account_ratio'
        return http_get_request(url, params)
        
    
    # 精英账户多空持仓对比-持仓量
    def get_contract_elite_position_ratio(self, contract_code, period):
        """
        :param contract_code BTC-USD
        :param period: 5min, 15min, 30min, 60min, 4hour, '1day'
        """
        params = {'contract_code':contract_code,
                  'period':period}        

        url = self.__url + '/swap-api/v1/swap_elite_position_ratio'
        return http_get_request(url, params)


    # 查询系统状态
    def get_api_state(self, contract_code):
        """
        :param contract_code BTC-USD
        """
        params = {'contract_code':contract_code}

        url = self.__url + '/swap-api/v1/swap_api_state'
        return http_get_request(url, params)        
        

    # 获取合约的资金费率
    def get_funding_rate(self, contract_code):
        """
        :param contract_code BTC-USD
        """
        params = {'contract_code':contract_code}

        url = self.__url + '/swap-api/v1/swap_funding_rate'
        return http_get_request(url, params)        


    # 获取强平订单
    def get_liquidation_orders(self, contract_code, trade_type, create_date, page_index=1, page_size=20):
        """
        :param trade_type when “0”, request fully filled liquidated orders; when “5’, request liquidated close orders; when “6”, request liquidated open orders
        :param create_date 7, 90 ( 7 days or 90 days )
        """
        url = self.__url + '/swap-api/v1/swap_liquidation_orders'
        params = {'contract_code':contract_code,
                  'trade_type':trade_type,
                  'create_date':create_date}
        return http_get_request(url, params)        


    # 获取合约的溢价指数K线

    # 获取实时预测资金费率的K线数据

    # 获取基差数据
    
    
    '''
    ======================
    Trade/Account API
    ======================
    '''
    
    # 获取用户账户信息
    def get_contract_account_info(self, contract_code=''):
        """
        :param contract_code: "BTC-USD","ETH-USD"...如果缺省，默认返回所有品种
        :return:
        """
        
        params = {}
        if contract_code:
            params["contract_code"] = contract_code
    
        request_path = '/swap-api/v1/swap_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 获取用户持仓信息
    def get_contract_position_info(self, contract_code=''):
        """
        :param contract_code: "BTC-USD","ETH-USD"...如果缺省，默认返回所有品种
        :return:
        """
        
        params = {}
        if contract_code:
            params["contract_code"] = contract_code
    
        request_path = '/swap-api/v1/swap_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    

    # 查询用户账户和持仓信息
    def get_contract_account_position_info(self, contract_code=''):
        """
        :param contract_code: "BTC-USD","ETH-USD"...如果缺省，默认返回所有品种
        :return:
        """        
        params = {}
        if contract_code:
            params["contract_code"] = contract_code
    
        request_path = '/swap-api/v1/swap_account_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
        
    
    # 合约下单
    def send_contract_order(self, contract_code, client_order_id, price, volume,
                            direction, offset, lever_rate, order_price_type):
        """
        :contract_code: "BTC-USD"
        :client_order_id: 客户自己填写和维护，必须为数字, 请注意必须小于等于9223372036854775807
        :price             必填   价格
        :volume            必填  委托数量（张）
        :direction         必填  "buy" "sell"
        :offset            必填   "open", "close"
        :lever_rate        必填  杠杆倍数[“开仓”若有10倍多单，就不能再下20倍多单;首次使用高倍杠杆(>20倍)，请使用主账号登录web端同意高倍杠杆协议后，才能使用接口下高倍杠杆(>20倍)]
        :order_price_type  必填   订单报价类型 
            "limit":限价 
            "opponent":对手价 
            "post_only":只做maker单,post only下单只受用户持仓数量限制,
            optimal_5：最优5档、optimal_10：最优10档、optimal_20：最优20档，
            "fok":FOK订单，"ioc":IOC订单, opponent_ioc"： 对手价-IOC下单，"optimal_5_ioc"：最优5档-IOC下单，"optimal_10_ioc"：最优10档-IOC下单，"optimal_20_ioc"：最优20档-IOC下单,
            "opponent_fok"： 对手价-FOK下单，"optimal_5_fok"：最优5档-FOK下单，"optimal_10_fok"：最优10档-FOK下单，"optimal_20_fok"：最优20档-FOK下单
        """        
        params = {"contract_code": contract_code,
                  "price": price,
                  "volume": volume,
                  "direction": direction,
                  "offset": offset,
                  "lever_rate": lever_rate,
                  "order_price_type": order_price_type}
        if client_order_id:
            params['client_order_id'] = client_order_id
    
        request_path = '/swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 合约计划委托下单
    def send_contract_trigger_order(self, contract_code, trigger_type, trigger_price,
                                    order_price_type, volume, direction, offset, lever_rate, order_price=None):
        """
        :contract_code(true): "BTC-USD"
        :trigger_type(true): "ge"(trigger price greater than current price); "le"(trigger_price less than current price)
        :trigger_price(true): least decimal point has to be larger than min tick size
        :order_price(false): 委托价，精度超过最小变动单位会报错
        :order_price_type(false): limit(default); optimal_5; optimal_10; optimal_20
        :volume(true): int type - number of sheets
        :direction(true): "buy", "sell"
        :offset(true): "open", "close"
        :lever_rate(false): int - 开仓必须填写，平仓可以不填。杠杆倍数[开仓若有10倍多单，就不能再下20倍多单]
        """
        params = {"contract_code":contract_code,
                  "trigger_type": trigger_type,
                  "trigger_price":trigger_price,
                  "volume":volume,
                  "direction":direction,
                  "offset":offset,
                  "lever_rate":lever_rate}
        if order_price:
            params["order_price"] = order_price
        if order_price_type:
            params["order_price_type"] = order_price_type
        request_path = '/swap-api/v1/swap_trigger_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 合约批量下单
    def send_contract_batchorder(self, orders_data):
        """
        orders_data: example:
        orders_data = {'orders_data': [
               {'contract_code':'BTC-USD',  'client_order_id':'', 
                'price':1, 'volume':1, 'direction':'buy', 'offset':'open', 
                'leverRate':20, 'orderPriceType':'limit'},
               {'contract_code':'BTC181228', 'client_order_id':'', 
                'price':2, 'volume':2, 'direction':'buy', 'offset':'open', 
                'leverRate':20, 'orderPriceType':'limit'}]}                
        Parameters of each order: refer to send_contract_order
        """
        
        params = orders_data
        request_path = '/swap-api/v1/swap_batchorder'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 撤销订单
    def cancel_contract_order(self, contract_code, order_id='', client_order_id=''):
        """
        参数名称          是否必须 类型     描述
        contract_code     true   string  BTC-USD, ETH-USD, ...
        order_id	         false  string  订单ID(多个订单ID中间以","分隔,一次最多允许撤消10个订单)
        client_order_id  false  string  客户订单ID(多个订单ID中间以","分隔,一次最多允许撤消10个订单)
        备注： order_id 和 client_order_id都可以用来撤单，同时只可以设置其中一种，如果设置了两种，默认以order_id来撤单。
        撤单接口返回结果只代表撤单命令发送成功，建议根据订单查询接口查询订单的状态来确定订单是否已真正撤销。
        """        
        params = {"contract_code": contract_code}
        if order_id:
            params["order_id"] = order_id
        if client_order_id:
            params["client_order_id"] = client_order_id  
    
        request_path = '/swap-api/v1/swap_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托撤单
    def cancel_trigger_contract_order(self, contract_code, order_id):
        params = {"contract_code": contract_code, "order_id": order_id}
        request_path = '/swap-api/v1/swap_trigger_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 全部撤单
    def cancel_all_contract_order(self, contract_code):        
        params = {"contract_code": contract_code}
    
        request_path = '/swap-api/v1/swap_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # cancel all trigger order
    def cancel_all_trigger_contract_order(self, contract_code):
        """
        param_name     type    non-optional   description
        contract_code   string    false             BTC-USD
        """
        params = {"contract_code": contract_code}
        request_path = '/swap-api/v1/swap_trigger_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 获取合约订单信息
    def get_contract_order_info(self, contract_code, order_id='', client_order_id=''):
        """
        参数名称	        是否必须	类型	    描述
        contract_code    true    string  BTC-USD, ETH-USD, ...
        order_id	        false	string	订单ID（ 多个订单ID中间以","分隔,一次最多允许查询50个订单 ）
        client_order_id	false	string	客户订单ID(多个订单ID中间以","分隔,一次最多允许查询50个订单)
        备注：order_id和client_order_id都可以用来查询，同时只可以设置其中一种，如果设置了两种，默认以order_id来查询。
        return:
        status	true	int	订单状态	(1准备提交 2准备提交 3已提交 4部分成交 5部分成交已撤单 6全部成交 7已撤单 10失败 11撤单中)
        """
        
        params = {"contract_code": contract_code}
        if order_id:
            params["order_id"] = order_id
        if client_order_id:
            params["client_order_id"] = client_order_id  
    
        request_path = '/swap-api/v1/swap_order_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 获取合约订单明细信息        
    def get_contract_order_detail(self, contract_code, order_id, order_type, created_at=None, page_index=None, page_size=None):
        """
        参数名称     是否必须  类型    描述
        contract_code  true	    string "BTC-USD","ETH-USD"...
        order_id    true	    long	   订单id
        order_type  true    int    订单类型。1:报单， 2:撤单， 3:强平/爆仓， 4:交割
        created_at  true    number 下单时间戳
        page_index  false   int    第几页,不填第一页
        page_size   false   int    不填默认20，不得多于50
        """        
        params = {"contract_code": contract_code,
                  "order_id": order_id,
                  "order_type": order_type}
        if created_at:
            params["created_at"] = created_at
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size  
    
        request_path = '/swap-api/v1/swap_order_detail'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 获取合约当前未成交委托
    def get_contract_open_orders(self, contract_code, page_index=1, page_size=20):
        """
        参数名称     是否必须  类型   描述
        symbol      false   string "BTC-USD","ETH-USD"...
        page_index  false   int    第几页,不填第一页
        page_size   false   int    不填默认20，不得多于50
        """        
        params = {"contract_code":contract_code}
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size  
    
        request_path = '/swap-api/v1/swap_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 获取计划委托当前委托
    def get_contract_open_trigger_orders(self, contract_code, page_index=1, page_size=20):
        """
        param_name    type     non-optional  description
        contract_code   string    true              BTC-USD, LTC-USD, ...
        page_index      int        false              default is first page
        page_size         int       false              default is 20, has to be less than 50
        """
        params = {"contract_code":contract_code}
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size
        request_path = '/swap-api/v1/swap_trigger_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 获取合约历史委托
    def get_contract_history_orders(self, contract_code, trade_type, type, status, create_date,
                                    page_index=1, page_size=20):
        """
        参数名称     是否必须  类型     描述	    取值范围
        contract_code      true	    string  品种代码  "BTC-USD","ETH-USD"...
        trade_type  true	    int     交易类型  0:全部,1:买入开多,2: 卖出开空,3: 买入平空,4: 卖出平多,5: 卖出强平,6: 买入强平,7:交割平多,8: 交割平空; 11:减仓平多，12:减仓平空
        type        true	    int     类型     1:所有订单、2：结束汏订单
        status      true	    int     订单状态  0:全部,3:未成交, 4: 部分成交,5: 部分成交已撤单,6: 全部成交,7:已撤单
        create_date true	    int     日期     可随意输入正整数，如果参数超过90则默认查询90天的数据
        page_index  false   int     页码，不填默认第1页		
        page_size   false   int     不填默认20，不得多于50
        """        
        params = {"contract_code": contract_code,
                  "trade_type": trade_type,
                  "type": type,
                  "status": status,
                  "create_date": create_date}
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size  
    
        request_path = '/swap-api/v1/swap_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    #xxx left here
    
    # trigger order history
    def get_contract_history_trigger_orders(self, contract_code, trade_type, status, create_date,
                                            page_index=1, page_size=20):
        """
        param_name     type        non-optional   description
        symbol              string      true               BTC, ETH,...
        contract_code     string      false              EOS190118
        trade_type          int          true               0(all), 1(open long), 2(open short), 3(close short), 4(close long), 
        status                 string     true               0(all), 4(active), 5(failed), 6(canceled)
        create_date        int          true               how many days (less or equal to 90)
        page_index         int          false              page number default 1
        page_size           int           false             default 20, less than 50
        """
        params = {"contract_code":contract_code,
                  "trade_type":trade_type,
                  "status":status,
                  "create_date":create_date}
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size
        request_path = '/swap-api/v1/swap_trigger_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)        

    # 闪电平仓下单
    def lightning_close_position(self, contract_code, volume, direction,
                                 client_order_id='', order_price_type=''):
        """
        param_name     type        non-optional   description
        contract_code     string      false              BTC-USD
        volume              int          true                number of sheets
        direction            string      true                buy, sell
        client_order_id    long        false
        order_price_type string      false              不填，默认为“闪电平仓”，"lightning"：闪电平仓，"lightning_fok"：闪电平仓-FOK,"lightning_ioc"：闪电平仓-IOC
        """
        params = {"contract_code":contract_code,
                  "volume":volume,
                  "direction":direction}
        if client_order_id:
            params["client_order_id"] = client_order_id
        if order_price_type:
            params["order_price_type"] = order_price_type
        request_path = '/swap-api/v1/swap_lightning_close_position'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)        
