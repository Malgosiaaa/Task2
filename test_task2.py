from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from redirect_payment_page import RedirectPaymentPage
from select_payment_page import SelectPaymentPage
from home_page import HomePage
from variables import BASE_URL, ERROR_MSG_COLOR, PAYMENT_AMOUNT, EMAIL


def initialize_driver_chrome():
    options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    return chrome


driver = initialize_driver_chrome()
driver.get(BASE_URL)

# execute methods from the HomePage
home_page = HomePage(driver)
home_page.close_cookies()
home_page.click_demo()

# handle windows and iterate to newly opened window
current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

# execute method from SelectPaymentPage
select_payment = SelectPaymentPage(driver)
select_payment.click_redirect_payment_flow()

# execute methods from RedirectPaymentPage
redirect_payment = RedirectPaymentPage(driver)
redirect_payment.fill_in_payment_amount(PAYMENT_AMOUNT)
redirect_payment.fill_in_email_address(EMAIL)
redirect_payment.click_submit_btn()

# locate error message and store its color to variable
error_msg = driver.find_element(By.CSS_SELECTOR, ".sc-bkbjAj.sc-cBoprd.EIXTr.gChalR")
msg_color = error_msg.value_of_css_property('color')
print(msg_color)

# assert if error message appeared and assert if its color was rgba(255, 59, 48, 1)
assert error_msg.is_displayed()
assert msg_color == ERROR_MSG_COLOR

# click agreements checkbox and submit button
redirect_payment.click_checkbox_agreement()
redirect_payment.click_submit_btn()

driver.quit()

# revisit webpage
driver = initialize_driver_chrome()
driver.get(BASE_URL)

# assert if cookie bar is displayed
assert driver.find_element(By.CSS_SELECTOR, ".consent-banner____RE1adG").is_displayed()

driver.quit()