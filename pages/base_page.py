import allure
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from allure_commons.types import AttachmentType


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        allure.step(f"Открыть страницу по ссылке: {self.url}")
        self.driver.get(self.url)

    def wait_element_before_is_visible(self, locator, timeout: float = 1.5) -> WebElement:
        with allure.step(f'Ждем отображения элемента с локатором "{locator}"'):
            try:
                return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                screenshot = self.driver.get_screenshot_as_png()
                allure.attach(screenshot, name=f'не дождались {locator}', attachment_type=allure.attachment_type.PNG)
                raise

    def wait_elements_before_are_visible(self, locator, timeout: float = 1.5) -> list[WebElement]:
        with allure.step(f'Ждем отображения списка элементов "{locator}"'):
            try:
                return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
            except TimeoutException:
                screenshot = self.driver.get_screenshot_as_png()
                allure.attach(screenshot, name=f'не дождались {locator}', attachment_type=allure.attachment_type.PNG)
                raise

    def element_is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            element = self.driver.find_element(*locator)
            with allure.step(f'Элемент с локатором "{locator}" отображается'):
                return element.is_displayed()
        except NoSuchElementException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f'Элемент с локатором "{locator}" не найден',
                attachment_type=AttachmentType.PNG
            )
            raise

    def click_to_visible_element(self, locator: tuple[str, str]) -> None:
        with allure.step(f'Клик на элемент с локатором "{locator}"'):
            self.driver.find_element(*locator).click()

    def get_current_url(self) -> str:
        with allure.step("Получить текущий урл активной страницы"):
            return self.driver.current_url
