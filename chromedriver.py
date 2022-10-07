import time
from selenium import webdriver


class Chrome():
    def chrome_init(self):
        driver = webdriver.Chrome(executable_path="G:\\python\\Drivers\\chromedriver_win32 (2)\\chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_name("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

        act_title=driver.title
        exp_title="OrangeHRM"
        if act_title==act_title:
            print("login test pass")
        else:
            print("login test fail")

        driver.close()

object = Chrome()
object.chrome_init()