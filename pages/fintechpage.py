from playwright.sync_api import Page

class FintechPage:

    def __init__(self,page):
        self.page =page

        self.vertical =page.locator('(//a[text()="Verticals"])[1]')
        self.fintech=page.locator('//strong[text()="Fintech"]')

        #sub menu
        self.POSsoftDev=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]') #POS Software Development
        self.Crypto=page.locator('(//a[text()="Crypto"])[1]') #Crypto


        self.fintech_list =[self.POSsoftDev , self.Crypto] # list in fintech

    def click_fintech_list(self):
        for option in self.fintech_list:
            self.vertical.hover()
            self.fintech.hover()
            option.click()
            self.page.wait_for_timeout(5000)
            self.page.go_back()
            self.page.wait_for_timeout(5000)

