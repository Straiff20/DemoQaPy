from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators
from pages.res.urls import Urls


class MainPage(BasePage):
    url = Urls.main_url

    def main_page_elements_is_visible(self):
        self.wait_element_before_is_visible(Locators.MAIN_LOGO)
        self.element_is_visible(Locators.MAIN_BANNER)
        self.element_is_visible(Locators.ELEMENTS_CARD)
        self.element_is_visible(Locators.FORMS_CARD)
        self.element_is_visible(Locators.ALERTS_CARD)
        self.element_is_visible(Locators.WIDGETS_CARD)
        self.element_is_visible(Locators.INTERACTIONS_CARD)
        self.element_is_visible(Locators.BOOKS_STORE_CARD)
        self.element_is_visible(Locators.MAIN_FOOTER)

    def main_page_click_to_card_by_position(self, position: int):
        card = Locators.get_category_card(position)
        self.element_is_visible(card)
        self.click_to_visible_element(card)
