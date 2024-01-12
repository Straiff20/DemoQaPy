from dataclasses import dataclass


@dataclass
class DataForForm:
    first_name: str = None
    last_name: str = None
    email: str = None
    current_address: str = None
    phone_number: str = None
    subject: str = None
