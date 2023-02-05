from selenium import webdriver
import os
import booking.constants as const
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Program Files (x86)\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()

# this method is executed at the end a "with" block
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Running exit function")
        if self.teardown:
            print("Running teardown function")
            self.quit()
        else:
            input()

# takes the bot to the first page of the target website
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency="USD"):
        currency_element =  self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR,
                                                     f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go="Douala"):
        search_field = self.find_element(By.NAME, value="ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        try:
            print("selected dropdown item the first way")
            first_result = self.find_element(By.CSS_SELECTOR,
                            'li[data-i="0"]')
        except:
            print("Selected dropdown item the second way")
            first_result = self.find_element(By.CSS_SELECTOR,
                            'div[tabindex="-1"]')

        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR,
                        f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_in_element = self.find_element(By.CSS_SELECTOR,
                                             f'td[data-date="{check_out_date}"]')
        check_in_element.click()
