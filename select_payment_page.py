from selenium.webdriver.common.by import By

from base_page import BasePage


class SelectPaymentPage(BasePage):
    def click_redirect_payment_flow(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.sc-kEqYlL.IXWjM").click()