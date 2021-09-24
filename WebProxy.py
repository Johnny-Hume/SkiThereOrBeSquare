from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import Select
import time


class WebProxy:

    driver = None

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            executable_path="./chromedriver.exe"
        )

    def get_webpage(self, url):
        self.driver.get(url)

    def click_ok_button(self):
        button = self.driver.find_element_by_id("eventlist-ok-button")
        button.click()

    def select_qubs_dropdown_option(self):
        select = self.get_select_dropdown_options()
        self.find_qubs_index(select)

    def find_qubs_index(self, select):
        self.find_option(select, "CUS")

    def find_option(self, select, choice):
        for option in select.options:
            value = option.text
            print(value)
            if choice in value:
                option.click()
                break
    
    def get_select_dropdown_options(self):
        select = Select(self.driver.find_element_by_tag_name("select"))
        if len(select.options) < 2:
            self.get_select_dropdown_options()
        return select
