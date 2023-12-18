from selenium.webdriver.common.by import By


class MyCommonTools:

    @staticmethod
    def set_locator(locator_type: str = By.CSS_SELECTOR, locator: str = "") -> tuple[str, str]:
        return locator_type, locator
