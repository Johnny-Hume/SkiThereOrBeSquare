from WebProxy import WebProxy
from constants import initial_access_url, booking_url, account_email, account_password


def go_skiing(webProxy):
    webProxy.login(account_email, account_password)
    webProxy.get_webpage(booking_url)
    webProxy.select_qubs_dropdown_option()
    webProxy.click_ok_button()
    webProxy.click_book_place_or_refresh()


if __name__ == "__main__":
    webProxy = WebProxy()
    go_skiing(webProxy)
