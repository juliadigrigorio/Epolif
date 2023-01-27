from pages.aqua_page import Aqua_Page
from pages.main_page import MainPage
import allure

link = "https://epolif.ru/"


@allure.story("TC-002-01 | Epolif aqua > Logo in the header")
def test_click_on_logo_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.click_on_logo()


@allure.story("TC-002-02 | Epolif aqua > link Главная in the header")
def test_go_to_main_page_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_main_page()


@allure.story("TC-002-03 | Epolif aqua > link Epolif Aqua in the header")
def test_go_to_aqua_page_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_aqua_page()


@allure.story("TC-002-04 | Epolif aqua > link Epolif GL7 in the header")
def test_go_to_gl7_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_gl7_page()


@allure.story("TC-002-05 | Epolif aqua > link Epolif GL21 in the header")
def test_go_to_gl21_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_gl21_page()


@allure.story("TC-002-06 | Epolif aqua > link Epolif ACP1 in the header")
def test_go_to_acp1_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_acp1_page()


@allure.story("TC-002-08 | Epolif aqua > footer > information about company")
def test_footer_information_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


@allure.story("TC-002-09 | Epolif aqua > footer > Up button")
def test_up_button_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_aqua()
