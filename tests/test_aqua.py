from pages.aqua_page import Aqua_Page
from pages.main_page import MainPage

link = "https://epolif.ru/"

"""TC-002-01 | Epolif aqua > Logo in the header"""


def test_click_on_logo_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.click_on_logo()


"""TC-002-02 | Epolif aqua > link Главная in the header"""


def test_go_to_main_page_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_main_page()


"""TC-002-03 | Epolif aqua > link Epolif Aqua in the header"""


def test_go_to_aqua_page_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_aqua_page()


"""TC-002-04 | Epolif aqua > link Epolif GL7 in the header"""


def test_go_to_GL7_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_gl7_page()


"""TC-002-05 | Epolif aqua > link Epolif GL21 in the header"""


def test_go_to_GL21_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_gl21_page()


"""TC-002-06 | Epolif aqua > link Epolif ACP1 in the header"""


def test_go_to_ACP1_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_ACP1_page()


"""TC-002-08 | Epolif aqua > footer > information about company"""


def test_footer_information_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


"""TC-002-09 | Epolif aqua > footer > Up button"""


def test_up_button_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_aqua()
