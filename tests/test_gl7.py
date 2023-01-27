from pages.gl7_page import GL7_Page
from pages.main_page import MainPage
import allure

link = "https://epolif.ru/"


@allure.story("TC-03-01 | Epolif GL7 > Logo in the header")
def test_click_on_logo_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.click_on_logo()


@allure.story("TC-003-02 | Epolif GL7 > link Главная in the header")
def test_go_to_main_page_from_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_main_page()


@allure.story("TC-003-03 | Epolif GL7 > link Epolif Aqua in the header")
def test_go_to_aqua_page_from_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_aqua_page()


@allure.story("TC-003-04 | Epolif GL7 > link Epolif GL7 in the header")
def test_go_to_gl7_from_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_gl7_page()


@allure.story("TC-003-05 | Epolif GL7 > link Epolif GL21 in the header")
def test_go_to_gl21_from_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_gl21_page()


@allure.story("TC-003-06 | Epolif GL7 > link Epolif ACP1 in the header")
def test_go_to_acp1_from_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_acp1_page()


@allure.story("TC-003-08 | Epolif GL7 > footer > information about company")
def test_footer_information_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


@allure.story("TC-003-09 | Epolif GL7 > footer > Up button")
def test_up_button_gl7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_gl7()
