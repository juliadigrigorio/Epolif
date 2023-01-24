from pages.GL7_page import GL7_Page
from pages.main_page import MainPage


link = "https://epolif.ru/"

"""TC-03-01 | Epolif GL7 > Logo in the header"""


def test_click_on_logo_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.click_on_logo()


"""TC-003-02 | Epolif GL7 > link Главная in the header"""


def test_go_to_main_page_from_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_main_page()


"""TC-003-03 | Epolif GL7 > link Epolif Aqua in the header"""


def test_go_to_aqua_page_from_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_aqua_page()


"""TC-003-04 | Epolif GL7 > link Epolif GL7 in the header"""


def test_go_to_GL7_from_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_gl7_page()


"""TC-003-05 | Epolif GL7 > link Epolif GL21 in the header"""


def test_go_to_GL21_from_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_gl21_page()


"""TC-003-06 | Epolif GL7 > link Epolif ACP1 in the header"""


def test_go_to_ACP1_from_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.go_to_ACP1_page()


"""TC-003-08 | Epolif GL7 > footer > information about company"""


def test_footer_information_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


"""TC-003-09 | Epolif GL7 > footer > Up button"""


def test_up_button_GL7(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()
    page = GL7_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_GL7()
