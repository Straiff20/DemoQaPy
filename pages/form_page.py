from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from pages.res.urls import Urls


class FormPage(BasePage):
    url = Urls.forms_page_url

    def check_elements_is_visible(self):
        self.wait_element_before_is_visible(Locators.TITLE_FORM_PAGE)
        self.wait_element_before_is_visible(Locators.TITLE_OF_FORM)

        self.wait_element_before_is_visible(Locators.NAME_LABEL)
        self.wait_element_before_is_visible(Locators.FIRST_NAME_INPUT)
        self.wait_element_before_is_visible(Locators.LAST_NAME_INPUT)
