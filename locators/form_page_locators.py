from utils.my_tools import MyCommonTools as Tools
from random import randint


class FormPageLocators:

    TITLE_FORM_PAGE: tuple[str, str] = Tools.set_locator(locator='//div[@class="pattern-backgound playgound-header"]')
    TITLE_OF_FORM: tuple[str, str] = Tools.set_locator(locator='//div[@class="practice-form-wrapper"]/h5')

    NAME_LABEL: tuple[str, str] = Tools.set_locator(locator='#userName-label')
    FIRST_NAME_INPUT: tuple[str, str] = Tools.set_locator(locator='#firstName')
    LAST_NAME_INPUT: tuple[str, str] = Tools.set_locator(locator='#lastName')

    EMAIL_LABEL: tuple[str, str] = Tools.set_locator(locator='#userEmail-label')
    EMAIL_INPUT: tuple[str, str] = Tools.set_locator(locator='#userEmail')

    GENDER_LABEL: tuple[str, str] = \
        Tools.set_locator(locator='//div[@id="genterWrapper"]/div[@class="col-md-3 col-sm-12"]')
    GENDER_SELECT: tuple[str, str] = Tools.set_locator(locator=f'#gender-radio-{randint(1, 3)}]')

    MOBILE_LABEL: tuple[str, str] = Tools.set_locator(locator='#userNumber-label')
    MOBILE_INPUT: tuple[str, str] = Tools.set_locator(locator='#userNumber')

    DATE_BORN_LABEL: tuple[str, str] = Tools.set_locator(locator='#dateOfBirth-label')
    DATE_BORN_INPUT: tuple[str, str] = Tools.set_locator(locator='#dateOfBirth')

    SUBJECT_LABEL: tuple[str, str] = \
        Tools.set_locator(locator='#//div[@id=\"subjectsWrapper\"]/div[@class=\"col-md-3 col-sm-12\"]')
    SUBJECT_INPUT: tuple[str, str] = Tools.set_locator(locator='#subjectsContainer')

    HOBBIES_LABEL: tuple[str, str] = \
        Tools.set_locator(locator='//div[@id=\"hobbiesWrapper\"]//label[@id=\"subjects-label\"]')
    HOBBIES_SELECT: tuple[str, str] = Tools.set_locator(locator=f'#hobbies-checkbox-{randint(1, 3)}')

    PICTURE_LABEL: tuple[str, str] = Tools.set_locator(locator='#subjects-label')
    FILE_INPUT: tuple[str, str] = Tools.set_locator(locator='#uploadPicture')

    CURRENT_ADDRESS_LABEL: tuple[str, str] = Tools.set_locator(locator='#currentAddress-label')
    CURRENT_ADDRESS_INPUT: tuple[str, str] = Tools.set_locator(locator='#currentAddress')

    STATE_AND_CITY_LABEL = Tools.set_locator(locator='#stateCity-label')
    STATE_SELECTOR = Tools.set_locator(locator='#state')
    CITY_SELECTOR = Tools.set_locator(locator='#city')
