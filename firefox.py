import time

from selenium import webdriver
from selenium.webdriver import firefox


class Firefox():
    def firefox(self):
        driver = webdriver.Firefox(executable_path="G:\\python\\Drivers\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        driver.get("https://www.google.com/")
        time.sleep(5)
        driver.close()

abcd = Firefox()
abcd.firefox()
