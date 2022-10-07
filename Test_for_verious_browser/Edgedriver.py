import time

from selenium import webdriver

class Edge():
    def edge(self):
        driver = webdriver.Edge(executable_path="C:\\Users\\USER\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.google.com/")
        time.sleep(5)

object = Edge()
object.edge()