from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOGO = (By.XPATH, "//img[2]")
LINK_MAIN = (By.CSS_SELECTOR, "#menu-item-7921 > a")
LINK_AQUA = (By.CSS_SELECTOR, "#menu-item-7920 > a")
LINK_GL7 = (By.CSS_SELECTOR, "#menu-item-7932 > a")
LINK_GL21 = (By.CSS_SELECTOR, "#menu-item-7938 > a")
LINK_ACP1 = (By.CSS_SELECTOR, "#menu-item-7950 > a")
FOOTER_ABOUT = (By.ID, "page-footer")
UP_BUTTON = (By.CSS_SELECTOR, "body > a.w-toplink.pos_right.active")
VIDEO = (By.XPATH, "//video")


class MainPage(BasePage):
    def click_on_logo(self):
        """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на логотип в хэдере."""
        self.browser.find_element(*LOGO).click()
        assert self.element_is_present(*VIDEO), "Not main page"

    # def go_to_main_page(self):
    #     """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на ссылку Главная в хэдере"""
    #     self.browser.find_element(*LINK_MAIN).click()
    #     assert self.element_is_present(*VIDEO), 'Not main page'

    def go_to_aqua_page(self):
        """Метод перехода на  страницу 'https://epolif.ru/epolif-aqua/' по нажатию на ссылку Epolif Aqua в хэдере"""
        self.browser.find_element(*LINK_AQUA).click()
        assert "epolif-aqua/" in self.browser.current_url, "Wrong page"

    def go_to_gl7_page(self):
        """Метод перехода на  страницу 'https://epolif.ru/epolif-gl-7/' по нажатию на ссылку Epolif GL7 в хэдере"""
        self.browser.find_element(*LINK_GL7).click()
        assert "epolif-gl-7/" in self.browser.current_url, "Wrong page"

    def go_to_gl21_page(self):
        """Метод перехода на  страницу 'https://epolif.ru/epolif-gl-21/' по нажатию на ссылку Epolif GL21 в хэдере"""
        self.browser.find_element(*LINK_GL21).click()
        assert "epolif-gl-21/" in self.browser.current_url, "Wrong page"

    def go_to_ACP1_page(self):
        """Метод перехода на  страницу 'https://epolif.ru/epolif-acp-1/' по нажатию на ссылку Epolif ACP1 в хэдере"""
        self.browser.find_element(*LINK_ACP1).click()
        assert "epolif-acp-1/" in self.browser.current_url, "Wrong page"

    def footer_information(self):
        """Метод нахождения  информации О компании в футере"""
        assert self.element_is_present(*FOOTER_ABOUT), "Element is absent"

    def footer_information_check(self):
        """Метод проверки информации О компании в футере"""
        info = self.browser.find_element(*FOOTER_ABOUT).text
        assert info == "© 2023 ООО «Базис-Инвест» — Все права защищены.", "Wrong info"

    def chains_down(self):
        """Метод прокрутки страницы вниз"""
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def up_button(self):
        """Метод проверки наличия кнопки Вверх в футере"""
        assert self.element_is_present(*UP_BUTTON), "Element is absent"

    def should_be_hover(self):
        """Метод проверки активности кнопки Вверх в футере"""
        cssValue = self.browser.find_element(*UP_BUTTON).value_of_css_property("cursor")
        assert cssValue == "pointer"

    def click_up_button(self):
        """Метод проверки работы кнопки Вверх в футере"""
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
