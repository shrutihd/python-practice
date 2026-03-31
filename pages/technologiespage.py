from playwright.sync_api import Page

class Technologiespage:

    def __init__(self,page):
        self.techonolgies=page.locator('(//a[text()="Technologies"])[1]')

        #sub menu in technologies
        self.eCom =page.locator('//strong[text()="eCommerce Development"]')
        self.MobAppDev =page.locator('//strong[text()="Mobile App Development"]')
        self.ArtInt =page.locator('//strong[text()="Artificial Intelligence"]')

        self.Technologies_list =[self.eCom,self.MobAppDev,self.ArtInt]

        def techonolgies_hover():
            self.techonolgies.hover()

        def eCom_hover():
            self.eCom.hover()

        def MobAppDev_hover():
            self.MobAppDev.hover()

        def ArtInt_hover():
            self.ArtInt.hover()
            



