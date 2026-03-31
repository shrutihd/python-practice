from playwright.sync_api import Page

class VerticalPage:

    def __init__(self, page):
        self.page = page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        #self.trading=page.locator('//strong[text()="Trading"]')

        self.trading = page.locator('//li[@data-id="trading"]')
        self.retailEcom = page.locator('//li[@data-id="retailEcommerce"]')
        self.healthcare = page.locator('//li[@data-id="healthcare"]')
        self.fintech = page.locator('//li[@data-id="fintech"]')
        self.Customapp = page.locator('//li[@data-id="customApp"]')

        #list of vertical menu
        self.vertical_list =[self.trading,self.retailEcom,self.healthcare,self.fintech,self.Customapp]

    def vertical_hover(self):
        self.vertical.hover()

    def trading_hover(self):
        self.trading.hover()

    def retailEcom_hover(self):
        self.retailEcom.hover()

    def healthcare_hover(self):
        self.healthcare.hover()

    def fintech(self):
        self.Fintech.hover()

    def customapp(self):
        self.Customapp.hover()

    
        

