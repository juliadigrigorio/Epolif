from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

LINK_MAIN = (By.XPATH, "//span[text()='Главная']")
VIDEO = (By.XPATH, "//video")
LINK_AQUA = (By.XPATH, "//span[text()='Epolif Aqua']")
LINK_GL7 = (By.XPATH, "//span[text()='Epolif GL 7']")
LINK_GL21 = (By.XPATH, "//span[text()='Epolif GL 21']")
LINK_ACP1 = (By.XPATH, "//span[text()='Epolif ACP 1']")
FOOTER_ABOUT = (By.ID, "page-footer")
UP_BUTTON = (By.XPATH, "//a[@title='Наверх']")
LOGO = (By.XPATH, "//a[@aria-label='Ссылка']")


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

    def click_on_logo(self):
        """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на логотип в хэдере."""
        self.browser.find_element(*LOGO).click()
        assert self.element_is_present(*VIDEO), "Not main page"

    def go_to_main_page(self):
        """Метод перехода на главную страницу 'https://epolif.ru/' по нажатию на ссылку Главная в хэдере"""
        self.browser.find_element(*LINK_MAIN).click()
        assert self.element_is_present(*VIDEO), "Not main page"

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

    def go_to_acp1_page(self):
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
