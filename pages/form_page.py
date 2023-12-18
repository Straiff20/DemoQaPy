from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def check_elements_is_visible(self):
        self.element_is_visible(Locators.TITLE_FORM_PAGE)
        self.element_is_visible(Locators.TITLE_OF_FORM)

        self.element_is_visible(Locators.NAME_LABEL)
        self.element_is_visible(Locators.FIRST_NAME_INPUT)
        self.element_is_visible(Locators.LAST_NAME_INPUT)
