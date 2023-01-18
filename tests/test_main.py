import pytest
from pages.main_page import MainPage
import time


link = "https://epolif.ru/"

"""TC-001-02 | Main page > Logo in the header"""


def test_click_on_logo(browser):
    page = MainPage(browser, link)
    page.click_on_logo()


"""TC-001-03 | Main page > link Главная in the header"""


def test_go_to_main_page(browser):
    page = MainPage(browser, link)
    page.go_to_main_page()


"""TC-001-04 | Main page > link Epolif Aqua in the header"""


def test_go_to_aqua_page(browser):
    page = MainPage(browser, link)
    page.go_to_aqua_page()


"""TC-001-05 | Main page > link Epolif GL7 in the header"""


def test_go_to_gl7_page(browser):
    page = MainPage(browser, link)
    page.go_to_gl7_page()


"""TC-001-06 | Main page > link Epolif GL21 in the header"""


def test_go_to_gl21_page(browser):
    page = MainPage(browser, link)
    page.go_to_gl21_page()


"""TC-001-07 | Main page > link Epolif ACP1 in the header"""


def test_go_to_ACP1_page(browser):
    page = MainPage(browser, link)
    page.go_to_ACP1_page()


"""TC-001-10 | Main page > footer > information about company"""


def test_footer_information(browser):
    page = MainPage(browser, link)
    page.footer_information()
    page.footer_information_check()


"""TC-001-11 | Main page > footer > Up button"""


def test_up_button(browser):
    page = MainPage(browser, link)
    page.chains_down()
    page.up_button()
    page.should_be_hover()
    page.click_up_button()


"""TC-001-01 | Main page > Presence of the promo video"""


def test_video(browser):
    page = MainPage(browser, link)
    page.presence_of_the_video()
    page.video_on_repeat()
