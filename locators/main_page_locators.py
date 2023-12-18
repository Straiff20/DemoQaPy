from selenium.webdriver.common.by import By


class MainPageLocators:
    def _get_category_card(self, position: int = 1) -> tuple[str, str]:
        return By.XPATH, f'//div[@class="card mt-4 top-card"][{position}]'

    MAIN_LOGO: tuple[str, str] = (By.XPATH, '//*[@id="app"]/header/a/img')
    MAIN_BANNER: tuple[str, str] = (By.CSS_SELECTOR, '.home-banner')

    CATEGORY_CARDS: tuple[str, str] = (By.CSS_SELECTOR, '.category-cards')
    ELEMENTS_CARD = _get_category_card(1)
    FORMS_CARD = _get_category_card(2)
    ALERTS_CARD = _get_category_card(3)
    WIDGETS_CARD = _get_category_card(4)
    INTERACTIONS_CARD = _get_category_card(5)
    BOOKS_STORE_CARD = _get_category_card(6)

    MAIN_FOOTER: tuple[str, str] = (By.XPATH, '//div[@id="app"]/footer')
