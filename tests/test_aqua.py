from pages.aqua_page import Aqua_Page
from pages.main_page import MainPage

link = "https://epolif.ru/"

"""TC-002-01 | Epolif aqua > Logo in the header"""


def test_click_on_logo_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.click_on_logo_aqua()


"""TC-002-02 | Epolif aqua > link Главная in the header"""


def test_go_to_main_page_from_aqua(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()
    page = Aqua_Page(browser, link)
    page.go_to_main_page()
