from selenium import webdriver
import os
import booking.constants as const
import time


class Booking:
    def __init__(self, driver_path = r"C:\Program Files (x86)\chromedriver.exe", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += driver_path
        # super(Booking, self).__init__()
        self.driver = webdriver.Chrome(self.driver_path)

# this method is executed at the end a "with" block
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

# this method is used at the beginning of the a "with" block
    def __enter__(self):
        print("Enter function run")

# takes the bot to the first page of the target website
    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        # self.get(const.BASE_URL)
