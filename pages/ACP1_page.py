from pages.base_page import BasePage
from selenium.webdriver.common.by import By

UP_BUTTON = (By.CSS_SELECTOR, "body > a.w-toplink.pos_right.active")


class ACP1_Page(BasePage):
    def click_up_button_acp1(self):
        """Метод проверки работы кнопки Вверх в футере"""
        self.browser.find_element(*UP_BUTTON).click()
        is_up_button_works = self.browser.find_element(*UP_BUTTON).get_attribute("href")
        assert is_up_button_works == "https://epolif.ru/epolif-acp-1/#"
