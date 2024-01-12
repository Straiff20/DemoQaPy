import pytest
import allure

from pages.main_page import MainPage
from pages.res.urls import Urls
from utils.my_asserts import check_current_url


@pytest.mark.main_page
@allure.epic('main_page')
class TestMainPage:

    @allure.story('visible_elements')
    def test_main_page_visible_elements(self, driver):
        main_page: MainPage = MainPage(driver, MainPage.url)
        main_page.open()
        main_page.all_elements_is_visible()

    @allure.story('transit_to_page')
    @pytest.mark.parametrize("case, card_position, exp_url", [
        ("elements_card", 1, Urls.elements_page_url),
        ("forms_card", 2, Urls.forms_page_url),
        ("alerts_card", 3, Urls.alerts_page_url),
        ("widgets_card", 4, Urls.widgets_page_url),
        ("interactions_card", 5, Urls.interactions_page_url),
        ("books_store_card", 6, Urls.books_store_page_url)
    ])
    def test_transit_from_main_page_to_card(self, driver, case, card_position, exp_url):
        main_page: MainPage = MainPage(driver, MainPage.url)
        main_page.open()
        main_page.click_to_card_by_position(card_position)
        check_current_url(current_url=main_page.get_current_url(), exp_url=exp_url)
