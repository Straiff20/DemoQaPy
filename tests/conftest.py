import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver_options = Options()

    driver_options.add_argument('--headless')
    driver_options.add_argument('--no-sandbox')
    driver_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=driver_service, options=driver_options)
    driver.maximize_window()

    yield driver
    driver.quit()
