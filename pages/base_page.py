from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

LINK_MAIN = (By.CSS_SELECTOR, "#menu-item-7921 > a")
VIDEO = (By.XPATH, "//video")


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

    def go_to_main_page(self):
        """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на ссылку Главная в хэдере"""
        self.browser.find_element(*LINK_MAIN).click()
        assert self.element_is_present(*VIDEO), "Not main page"
