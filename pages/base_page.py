from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def element_is_present(self, method, locator):
        """Метод провряет наличие элемента на странице."""
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True
