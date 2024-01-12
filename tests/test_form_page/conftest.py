import pytest

from dataclasses import dataclass
from tests.help_data.form_page_test_data import DataForForm
from faker import Faker

faker = Faker('Ru')


@pytest.fixture(scope='function')
def form_data():
    _full_form: DataForForm = DataForForm(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        current_address=faker.address(),
        phone_number=faker.numerify(text='##########'),
        subject="Russian"
    )

    @dataclass
    class TestData:
        full_form = _full_form

    yield TestData
