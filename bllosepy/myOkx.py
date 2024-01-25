# -*- coding:utf-8 -*-

import okx.Funding as Funding
import okx.Account as Account
import okx.TradingData as TradingData_api
import okx.MarketData as MarketData
import logging
import os
import time
import json


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    )

class myOkx():
    def __init__(self, env="test") :
        passphrase = os.environ['PASS_PHRASE']
        if env == 'pro':
            apikey = os.environ['API_KEY']
            secretkey = os.environ['CECRET_KEY']
            flag = "0" 
        else:
            apikey = "afa50758-7ac8-4689-b16f-03c1f8892fbb"
            secretkey = "E47D9AAF95AF7E0877153A7660B46714"
            flag = "1" 
        self.fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
        self.accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
        self.tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
        self.marketDataAPI =  MarketData.MarketAPI(flag=flag)
        self.volume_map = {}

    def get_index_tickers(self, instId = 'BTC-USD'):
        """
        获取指数行情数据
        :param instId: 指数类型
        """
        result = self.marketDataAPI.get_index_tickers(
            instId= instId
        )
        logging.info('>>>>>>' + instId + '<<<<<< ' + json.dumps(result))
        return result

    
    def get_index_candles(self, instId = 'BTC-USD'):
        """
        指数K线数据每个粒度最多可获取最近1,440条。
        """
        result = self.marketDataAPI.get_index_candlesticks(
                    instId=instId
                )
        logging.info('>>>>>>' + instId + '<<<<<< ' + json.dumps(result))
        return result

    def get_candles_after(self, before, instId = 'BTC-USD'):
        """
        获取指定时间之后的最新数据
        """
        result = self.marketDataAPI.get_index_candlesticks(
                    instId=instId, before= before
                )
        logging.info('>>>>>>' + instId + '<<<<<< ' + json.dumps(result))
        return result
        

    def is_support(self, ccy="BTC"):
        """
        判断当前币种是否被交易大数据所支持
        """
        result = self.tradingDataAPI.get_support_coin()
        if result['code'] != '0':
            return False
        contracts = result['data']['contract']
        return ccy in contracts

    def volume_taker(self, start='', ccy="BTC", instType="SPOT"):
        """
        获取主动买入/卖出情况
        :param ccy: 币种     BTC 比特币
        :param instType: 交易类型。 SPOT 币币交易
        """
        if not ccy in self.volume_map:
            self.volume_map[ccy] = {'buy': 0.00, 'sale': 0.00}
        result = self.tradingDataAPI.get_taker_volume(ccy=ccy, instType=instType, begin=start)
        max_time_stamp = 0
        
        if start != '' and int(result['data'][-1][0]) == int(start):
            result['data'].pop()
        for cur in result['data']:
            cur_time_stamp = int(cur[0])
            if cur_time_stamp > max_time_stamp:
                max_time_stamp = cur_time_stamp
            sale = float(cur[1])
            buy = float(cur[2])
            self.volume_map[ccy]['buy'] += buy
            self.volume_map[ccy]['sale'] += sale
        if max_time_stamp > 0:
            self.volume_map[ccy]['max_time_stamp'] = max_time_stamp
        logging.info('>>>>>>' + ccy + '<<<<<< ' + json.dumps(self.volume_map[ccy]))
        return self.volume_map
    
    def keep_volume(self, ccyList = ['BTC']):
        for index in range(3):
            for ccy in ccyList:
                if ccy in self.volume_map:
                    self.volume_taker(start=self.volume_map[ccy]['max_time_stamp'], ccy=ccy)
                else:
                    self.volume_taker(ccy=ccy)
            time.sleep(5*60)


    def asset_valuation(self, ccy = "USDT"):
        """
        获取当前账户资产估计价值
        """
        return self.fundingAPI.get_asset_valuation(ccy= ccy)
    
    def show_valuation(self, ccy="USDT"):
        result = self.asset_valuation(ccy)
        result1 = self.fundingAPI.get_balances(ccy)
        # result2 = self.accountAPI.get_account_bills()
        if(result["code"] == '0') :
            logging.info("当前账号总余额：" + result["data"][0]['totalBal'] + " " +ccy)
            logging.info("其中:")
            logging.info("金融账户:" + result["data"][0]['details']['earn'] + " " +ccy)
            logging.info("交易账户:" + result["data"][0]['details']['trading'] + " " +ccy)
            logging.info("资金账户:" + result["data"][0]['details']['funding'] + " " +ccy)
            logging.info("当前可用资金：")
            logging.info("可用余额:" + result1['data'][0]['availBal'] + ccy)
            logging.info("冻结余额:" + result1['data'][0]['frozenBal'] + ccy)
        else :
            logging.warn("查询当前用户余额失败!")

    
    def get_currencies(self):
        """
        当前账户余额
        """
        return self.fundingAPI.get_currencies()


if __name__ == '__main__':
    myOkx = myOkx("pro")
    # myOkx.show_valuation()
    # myOkx.is_support("ADA")
    myOkx.volume_taker(start='1705821600000')