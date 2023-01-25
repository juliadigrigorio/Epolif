from pages.GL21_page import GL21_Page
from pages.main_page import MainPage

link = "https://epolif.ru/"

"""TC-04-01 | Epolif GL21 > Logo in the header"""


def test_click_on_logo_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.click_on_logo()


"""TC-004-02 | Epolif GL21 > link Главная in the header"""


def test_go_to_main_page_from_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.go_to_main_page()


"""TC-004-03 | Epolif GL21 > link Epolif Aqua in the header"""


def test_go_to_aqua_page_from_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.go_to_aqua_page()


"""TC-004-04 | Epolif GL21 > link Epolif GL7 in the header"""


def test_go_to_GL7_from_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.go_to_gl7_page()


"""TC-004-05 | Epolif GL21 > link Epolif GL21 in the header"""


def test_go_to_GL21_from_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.go_to_gl21_page()


"""TC-004-06 | Epolif GL21 > link Epolif ACP1 in the header"""


def test_go_to_ACP1_from_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.go_to_ACP1_page()


"""TC-004-08 | Epolif GL21 > footer > information about company"""


def test_footer_information_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


"""TC-004-09 | Epolif GL21 > footer > Up button"""


def test_up_button_GL21(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()
    page = GL21_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_gl21()
