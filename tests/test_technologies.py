import pytest

from pages.technologiespage import Technologiespage
from pages.eCompage import eCom
from pages.MobileAppDevpage import MobileAppDevelop
from pages.RetailEcompage import RetailEcompage

@pytest.mark.smoke
def test_ecommerece_techonologies(page):

    ecom= eCom(page)
    ecom.eComoption_click()


    Mobapp =MobileAppDevelop(page)
    Mobapp.MobAppDev_click()

    RetailEcom = RetailEcompage(page)
    RetailEcom.click_retcomlist()
