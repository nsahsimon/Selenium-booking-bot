from selenium import webdriver
import os
import booking.constants as const
import time


class Booking:
    def __init__(self, driver_path = r"C:\Program Files (x86)\chromedriver.exe"):
        self.driver_path = driver_path
        os.environ["PATH"] += driver_path
        self.driver = webdriver.Chrome(self.driver_path)

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        time.sleep(20)
