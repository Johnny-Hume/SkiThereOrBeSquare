from selenium import webdriver
from selenium.webdriver.support import wait
from constants import login_url
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

    def login(self, username, password):
        self.get_webpage(login_url)
        self.driver.find_element_by_id("auth_login_password-datum-email").send_keys(username)
        self.driver.find_element_by_id("auth_login_password-datum-password").send_keys(password)
        self.driver.find_element_by_id("auth_login_password_submit").click()

    def click_ok_button(self):
        self.click_button("eventlist-ok-button")
    
    def click_book_place_button(self):
        self.click_button("bookpackage-go-book")

    def click_button(self, button_id):
        button = self.driver.find_element_by_id(button_id)
        button.click()
    
    def select_qubs_dropdown_option(self):
        select = self.get_select_dropdown_options()
        self.find_qubs_index(select)

    def find_qubs_index(self, select):
        self.find_option(select, "Queen University Belfast Snowsports")

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
    
    def refresh_page(self):
        self.driver.refresh()
    
    def click_book_place_or_refresh(self):
        try:
            self.click_book_place_button()
        except Exception:
            self.refresh_page()
            time.sleep(0.2)
            self.click_book_place_or_refresh()
