from WebProxy import WebProxy
from constants import initial_access_url
if __name__ == "__main__":
    webProxy = WebProxy()
    webProxy.get_webpage(initial_access_url)
    webProxy.select_qubs_dropdown_option()
    webProxy.click_ok_button()
