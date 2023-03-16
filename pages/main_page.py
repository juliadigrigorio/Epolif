from pages.base_page import BasePage
from selenium.webdriver.common.by import By


UP_BUTTON = (By.XPATH, "//a[@title='Наверх']")
VIDEO = (By.XPATH, "//video")


class MainPage(BasePage):
    def click_up_button_main(self):
        """Метод проверки работы кнопки Вверх в футере."""
        self.browser.find_element(*UP_BUTTON).click()
        is_up_button_works = self.browser.find_element(*UP_BUTTON).get_attribute("href")
        assert is_up_button_works == "https://epolif.ru/#"

    def presence_of_the_video(self):
        """Метод проверки наличия промо видео в хэдере главной страницы"""
        assert self.element_is_present(*VIDEO), "Element is absent"

    def video_on_repeat(self):
        """Метод проверки повторяемости промо видео в хэдере  главной страницы"""
        self.browser.find_element(*VIDEO)
        is_video_on_repeat = self.browser.find_element(*VIDEO).get_attribute("loop")
        assert is_video_on_repeat == "true"
