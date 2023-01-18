import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# TestData
link = "https://epolif.ru/"


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    browser.get(link)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
