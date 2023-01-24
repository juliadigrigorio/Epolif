from pages.base_page import BasePage
from selenium.webdriver.common.by import By

LOGO_AQUA = (By.XPATH, "//div/a/img[1]")
VIDEO = (By.XPATH, "//video")
UP_BUTTON = (By.CSS_SELECTOR, "body > a.w-toplink.pos_right.active")


class Aqua_Page(BasePage):
    def click_on_logo_aqua(self):
        """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на логотип в хэдере."""
        self.browser.find_element(*LOGO_AQUA).click()
        assert self.element_is_present(*VIDEO), "Not main page"

    def click_up_button_aqua(self):
        """Метод проверки работы кнопки Вверх в футере"""
        self.browser.find_element(*UP_BUTTON).click()
        is_up_button_works = self.browser.find_element(*UP_BUTTON).get_attribute("href")
        assert is_up_button_works == "https://epolif.ru/epolif-aqua/#"
