from pages.main_page import MainPage


class TestMainPage:

    def test_main_page(self, driver):
        main_page = MainPage(driver, "https://demoqa.com")
        main_page.open()
        main_page.main_page_elements_is_visible()
