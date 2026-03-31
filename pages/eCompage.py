from playwright.sync_api import Page

class eCom:

    def __init__(self,page):
        self.page =page
        self.techonolgies=page.locator('(//a[text()="Technologies"])[1]')
        self.eCom =page.locator('//strong[text()="eCommerce Development"]')

        #sub menu
        self.MagDev= page.locator('//a[text()="Magento Development"]')#1
        self.OpenCartDev =page.locator('(//a[text()="Opencart Development"])[1]')
        self.CodeignDev =page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.WordPDev =page.locator('(//a[text()="WordPress Development"])[1]')
        self.BigCom =page.locator('(//a[text()="Big Commerce"])[1]')
        self.ShopDev =page.locator('(//a[text()="Shopify Development"])[1]')
        self.CsCartDev =page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.NodJSDev =page.locator('(//a[text()="Node JS Development"])[1]')
        self.NopCom =page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')#Nop Commerece
        self.WooCom =page.locator('(//a[text()="Woo Commerce"])[1]')
        self.LarDev =page.locator('(//a[text()="Laravel Development"])[1]')
        self.PresDev =page.locator('(//a[text()="Prestashop Development"])[1]')
        self.DruDev =page.locator('(//a[text()="Drupal Development"])[1]')
        self.WixDev =page.locator('(//a[text()="Wix Development"])[1]')
        self.JoomDev =page.locator('(//a[text()="Joomla Development"])[1]')
        self.ReactJSDev =page.locator('(//a[text()="React JS Development"])[1]')
        self.ExpJSDev =page.locator('(//a[text()="Express JS Development"])[1]')
        

        self.eCom_list = [self.MagDev,self.OpenCartDev,self.CodeignDev,self.WordPDev,self.BigCom,self.ShopDev,self.CsCartDev,self.NodJSDev,self.NopCom,self.WooCom,self.LarDev,self.PresDev,self.DruDev,self.WixDev,self.JoomDev,self.ReactJSDev, self.ExpJSDev]
        


    def eComoption_click(self):
        for option in  self.eCom_list:
            self.techonolgies.hover()
            self.eCom.hover()
            option.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(3000)


        
        
        
        
        
       


#self. =page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')#Xamarin Mobile App
        