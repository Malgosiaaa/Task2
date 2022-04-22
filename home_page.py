from selenium.webdriver.common.by import By

from base_page import BasePage


class HomePage(BasePage):
    def close_cookies(self):
        self.driver.find_element(By.CSS_SELECTOR, ".base-button.landing-button.-primary.-small-text").click()

    def click_demo(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='https://demo.kevin.eu/']").click()