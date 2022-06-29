import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SeleniumDriver:
    URL = 'www.google.com'

    def __init__(self, maxWindow, URL):
        self.URL = URL
        # opt = webdriver.safari
        self.driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        if maxWindow:
            self.driver.maximize_window()
        self.driver.get(URL)

    def CheckID(self, username, password):
        time.sleep(3)
        try:
            self.driver.find_element(by=By.XPATH, value='//*[@type="text"]').send_keys(username)
            self.driver.find_element(by=By.XPATH, value='//*[@type="password"]').send_keys(password)
            self.driver.find_element(by=By.CLASS_NAME, value='login-button').click()
            time.sleep(3)
        except NoSuchElementException:
            raise Exception("Web Element Not Found for Logging In!!!")

        if self.driver.current_url == 'https://www.hulu.com/profiles?next=/':
            self.CloseApp()
            return {'Username': username, 'Password': password}
        else:
            self.driver.get(self.URL)
            return None

    def CloseApp(self):
        self.driver.close()
