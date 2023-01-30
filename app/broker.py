import robin_stocks.robinhood as r
import pandas as pd
import pyotp

class robin:
    
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.totp = pyotp.TOTP("My2factorAppHere").now()
        print(self.totp)

    def login(self):
        r.login(self.account, self.password, store_session=False,mfa_code=self.totp)
        print("Log in successfully!")

    #get all hodling stocks with holding values 
    def getMyStockList(self):
        stock_list = {}
        my_stocks_info = r.build_holdings()
        for key in my_stocks_info.keys():
            stock_list[key] = float(my_stocks_info[key]['price'])
        return stock_list

    def requestInvestmentProfile(self):
        d = r.profiles.load_account_profile()
        return d

if __name__ == '__main__':
    rb = robin("danabaxia@gmail.com","Hanjb1314$")
    rb.login()
    print(rb.getMyStockList())
    print(rb.requestInvestmentProfile())