from playwright.sync_api import Page

class RetailEcompage:

    def __init__(self,page):
        self.page = page

        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.retailEcom=page.locator('//li[@data-id="retailEcommerce"]')

        self.eComWebDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[2]')
        self.eComAppDev=page.locator('//a[text()="eCommerce App Development"]')
        
        self.retcomlist= [self.eComWebDev ,self.eComAppDev]


    def click_retcomlist(self):
        for option in self.retcomlist:
            self.vertical.hover()
            self.retailEcom.hover()

            option.click()
            self.page.wait_for_load_state("load") # navigates to sub menu page

            self.page.go_back()
            self.page.wait_for_load_state("load") # naviagte back to orginal page

            
            

