from playwright.sync_api import Page

class CustomAppPage:

    def __init__(self,page):
        self.page=page

        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.customapp =page.locator('//strong[text()="Custom App"]')

        #submenu

        
        self.HRM=page.locator('(//a[text()="HRM Development"])[1]')
        self.ERP =page.locator('(//a[text()="ERP App Development"])[1]')
        self.RealEst =page.locator('(//a[text()="Real Estate"])[1]')
        self.Travel =page.locator('(//a[text()="Travel"])[1]')
        self.Elearn =page.locator('(//a[text()="E-Learning"])[1]')
        self.DatAppDev =page.locator('(//a[text()="Dating App Development"])[1]')
        self.CRMDUS=page.locator('(//a[text()="CRM Development USA"])[1]')
        self.DeskAppDev =page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.CRM=page.locator('(//a[text()="CRM Development"])[1]')


        #create list
        self.customapp_list=[self.CRM,self.HRM,self.ERP,self.RealEst,self.Travel,self.Elearn,self.DatAppDev,self.CRMDUS,self.DeskAppDev]

    def click_customapp_list(self):
        for option in self.customapp_list:
            self.vertical.hover()
            self.customapp.hover()
            option.click()
            self.page.wait_for_timeout(5000)
            self.page.go_back()
            self.page.wait_for_timeout(5000)
