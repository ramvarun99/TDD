import time
import pytest
from selenium.webdriver.common.by import By

from PageObject.sell import Sell


@pytest.mark.usefixtures("setup")
class TestSell:

    def test_mb_one(self):
        sell = Sell(self.driver)
        sell.get_access_to_website()
        time.sleep(3)
        sell.get_sell()
        time.sleep(5)

    def test_mb_two(self):
        sell = Sell(self.driver)
        sell.get_access_to_website()
        sell.get_sell()
        # sell.get_post_prop()

    def test_mb_three(self):
        sell = Sell(self.driver)
        sell.get_access_to_website()
        sell.get_sell()
        sell.get_access_to_property()
        time.sleep(5)
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)
        sell.get_ab()
        sell.get_bc()
        sell.get_cd()
        sell.get_de()
        time.sleep(5)
        sell.get_ef()

    def test_mb_four(self):
        sell = Sell(self.driver)
        sell.get_access_to_website()
        sell.get_del()
        sell.get_sell()
        time.sleep(5)
        sell.get_fg()
        time.sleep(5)
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)
        sell.get_gh()
        sell.get_hi()
        sell.get_ij()
        sell.get_jk()
        time.sleep(4)
        sell.get_kl()
        time.sleep(3)
        sell.get_lm()
        time.sleep(3)
        sell.get_mn()

    def test_mb_five(self):
        sell = Sell(self.driver)
        sell.get_access_to_website()
        sell.get_sell()
        time.sleep(3)
        sell.get_ram()
        time.sleep(5)
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)
        sell.get_op()
        time.sleep(5)
        sell.get_pq()

    def test_mb_six(self):
        sell = Sell(self.driver)
        sell.get_access_to_website()
        sell.get_sell()
        time.sleep(5)
        sell.get_qr()
        time.sleep(4)
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)
        sell.get_rs()
        time.sleep(3)
        sell.get_st()
        time.sleep(3)
        sell.get_tu()
        time.sleep(3)
        sell.get_uv()
        time.sleep(3)
        sell.get_wx()
        time.sleep(3)
        sell.get_xy()
        time.sleep(3)
        sell.get_yz()
        sell.get_abc()
        sell.get_bcd()
