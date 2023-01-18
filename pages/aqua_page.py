from pages.base_page import BasePage
from selenium.webdriver.common.by import By

LOGO_AQUA = (By.XPATH, "//div/a/img[1]")
VIDEO = (By.XPATH, "//video")


class Aqua_Page(BasePage):
    def click_on_logo_aqua(self):
        """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на логотип в хэдере."""
        self.browser.find_element(*LOGO_AQUA).click()
        assert self.element_is_present(*VIDEO), "Not main page"
