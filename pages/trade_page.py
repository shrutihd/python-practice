from playwright.sync_api import Page

class TradingPage:

    def __init__(self, page):
        self.page = page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('//li[@data-id="trading"]')

        self.ST=page.locator('(//a[text()="Stock Trading"])[1]')
        self.AT=page.locator('(//a[text()="Algo Trading"])[1]')
        self.PT=page.locator('(//a[text()="Paper Trading"])[1]')
        self.CustT=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.CFDT=page.locator('(//a[text()="CFD Trading"])[1]')
        self.Webport=page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.STDM=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.trad_list=[self.ST,self.AT,self.PT,self.CustT,self.CFDT,self.Webport,self.STDM]
        

    def tradingoption_click(self):
        for option in  self.trad_list:
            self.vertical.hover()
            self.trading.hover()
            option.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back() 
            self.page.wait_for_timeout(3000)


            
        

            
    