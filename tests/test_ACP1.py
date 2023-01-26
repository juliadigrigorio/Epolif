from pages.ACP1_page import ACP1_Page
from pages.main_page import MainPage

link = "https://epolif.ru/"

"""TC-005-01 | Epolif ACP1 > Logo in the header"""


def test_click_on_logo_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.click_on_logo()


"""TC-005-02 | Epolif ACP1 > link Главная in the header"""


def test_go_to_main_page_from_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.go_to_main_page()


"""TC-005-03 | Epolif ACP1 > link Epolif Aqua in the header"""


def test_go_to_aqua_page_from_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.go_to_aqua_page()


"""TC-005-04 | Epolif ACP1 > link Epolif GL7 in the header"""


def test_go_to_GL7_from_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.go_to_gl7_page()


"""TC-005-05 | Epolif ACP1 > link Epolif GL21 in the header"""


def test_go_to_GL21_from_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.go_to_gl21_page()


"""TC-005-06 | Epolif ACP1 > link Epolif ACP1 in the header"""


def test_go_to_ACP1_from_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.go_to_ACP1_page()


"""TC-005-08 | Epolif ACP1 > footer > information about company"""


def test_footer_information_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.chains_down()
    page.footer_information()
    page.footer_information_check()


"""TC-005-09 | Epolif ACP1 > footer > Up button"""


def test_up_button_ACP1(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()
    page = ACP1_Page(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button_acp1()
