from playwright.sync_api import Page

class HealthcarePage:

    def __init__(self,page): # craete a constuctor
        self.page = page

        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.healthcare = page.locator('//li[@data-id="healthcare"]')

        #sub menu of healthcare
        self.DietNut =page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthTrack =page.locator('(//a[text()="Health tracking App"])[1]')

        #create a list
        self.healthcare_list=[self.DietNut , self.healthTrack]


    def healthcare_list_click(self):
        for option in self.healthcare_list:
            self.vertical.hover()
            self.healthcare.hover()
            option.click()
            self.page.wait_for_timeout(5000)
            self.page_go_back()
            self.page.wait_for_timeout(5000)

          




    


        