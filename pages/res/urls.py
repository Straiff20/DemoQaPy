from dataclasses import dataclass


@dataclass
class Urls:
    main_url: str = "https://demoqa.com/"
    alerts_page_url: str = f"{main_url}alertsWindows"
    books_store_page_url: str = f"{main_url}books"
    elements_page_url: str = f"{main_url}elements"
    forms_page_url: str = f"{main_url}forms"
    interactions_page_url: str = f"{main_url}interaction"
    widgets_page_url: str = f"{main_url}widgets"
