from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


class RedirectPaymentPage(BasePage):
    def fill_in_payment_amount(self, amount):
        self.driver.find_element(By.ID, "amount").send_keys(amount)

    def fill_in_email_address(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def choose_swedbank(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.sc-iemXMA.iSPPGk'))).click()

    def click_submit_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    def click_checkbox_agreement(self):
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iklIKw.cRLtEU").click()