from pages.acp1_page import ACP1_Page
from pages.main_page import MainPage
import allure

link = "https://epolif.ru/"


@allure.story("TC-005-01 | Epolif ACP1 > Logo in the header")
def test_click_on_logo_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.click_on_logo()


@allure.story("TC-005-02 | Epolif ACP1 > link Главная in the header")
def test_go_to_main_page_from_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.go_to_main_page()


@allure.story("TC-005-03 | Epolif ACP1 > link Epolif Aqua in the header")
def test_go_to_aqua_page_from_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.go_to_aqua_page()


@allure.story("TC-005-04 | Epolif ACP1 > link Epolif GL7 in the header")
def test_go_to_gl7_from_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.go_to_gl7_page()


@allure.story("TC-005-05 | Epolif ACP1 > link Epolif GL21 in the header")
def test_go_to_gl21_from_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.go_to_gl21_page()


@allure.story("TC-005-06 | Epolif ACP1 > link Epolif ACP1 in the header")
def test_go_to_acp1_from_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.go_to_acp1_page()


@allure.story("TC-005-08 | Epolif ACP1 > footer > information about company")
def test_footer_information_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


@allure.story("TC-005-09 | Epolif ACP1 > footer > Up button")
def test_up_button_acp1(browser):
    page = MainPage(browser, link)
    page.go_to_acp1_page()
    page = ACP1_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_acp1()
