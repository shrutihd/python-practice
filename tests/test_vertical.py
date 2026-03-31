import pytest

from pages.verticalpage import VerticalPage  # import from page file (page name) and class from that page i,e class name
from pages.trade_page import TradingPage
from pages.RetailEcompage import RetailEcompage
from pages.fintechpage import FintechPage
from pages.Customapp_page import CustomAppPage




@pytest.mark.smoke
def test_vertical(page):
    
    
    trade =TradingPage(page)  # creating a object 
    trade.tradingoption_click()

    retail = RetailEcompage(page)
    retail.click_retcomlist()

    fin = FintechPage(page)
    fin.click_fintech_list()

    custom = CustomAppPage(page)
    custom.click_customapp_list()
    
    