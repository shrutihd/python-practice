from playwright.sync_api import Page

class MobileAppDevelop:

    def __init__(self,page):
        self.page =page

        self.techonolgies=page.locator('(//a[text()="Technologies"])[1]')
        self.MobAppDev =page.locator('//strong[text()="Mobile App Development"]')

        #sub menu of MobileAppdevelopment
        self.ReaNavMobApp =page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.XMobAppDev =page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.FluMobAppDev =page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.SwiAppDev =page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.EnpMobAppDev =page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.KotMobAppDev =page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.IonMobApp =page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.AppBookDev =page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.MobAppDev_list =[self.ReaNavMobApp ,self.XMobAppDev,self.FluMobAppDev ,self.SwiAppDev, self.EnpMobAppDev,self.KotMobAppDev ,self.IonMobApp,self.AppBookDev ]

        def MobAppDev_click(self):

            for option in  self.MobAppDev_list:
                self.techonolgies.hover()
                self.MobAppDev.hover()
                option.click()
                self.page.wait_for_timeout(3000)
                self.page.go_back() 
                self.page.wait_for_timeout(3000)
