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

    def click_book_place_button(self):
        self.click_button("bookpackage-go-book")

    def click_button(self, button_id):
        button = self.driver.find_element_by_id(button_id)
        button.click()
    
    def refresh_page(self):
        self.driver.refresh()
    
    def click_book_place_or_refresh(self):
        try:
            self.click_book_place_button()
        except Exception:
            print("Button not found, refreshing")
            self.refresh_page()
            time.sleep(0.2)
            self.click_book_place_or_refresh()
