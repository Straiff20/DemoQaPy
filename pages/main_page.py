from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):

    def main_page_elements_is_visible(self):
        self.element_is_visible(Locators.MAIN_LOGO)
        self.element_is_visible(Locators.MAIN_BANNER)
        self.element_is_visible(Locators.ELEMENTS_CARD)
        self.element_is_visible(Locators.FORMS_CARD)
        self.element_is_visible(Locators.ALERTS_CARD)
        self.element_is_visible(Locators.WIDGETS_CARD)
        self.element_is_visible(Locators.INTERACTIONS_CARD)
        self.element_is_visible(Locators.BOOKS_STORE_CARD)
        self.element_is_visible(Locators.MAIN_FOOTER)
