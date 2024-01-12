import pytest
import allure

from pages.form_page import FormPage


@pytest.mark.form_page
@allure.epic("form_page")
class TestFormPage:

    @allure.story("visible elements")
    def test_form_page_visible_elements(self, driver, form_data):
        form_page: FormPage = FormPage(driver, FormPage.url)
        form_page.open()
        form_page.elements_is_visible()
