import pytest
from contact import Contact


@pytest.fixture()
def valid_name():
    return 'Aecio'


@pytest.fixture()
def invalid_email():
    return 'sda.com'


class TestCreateContact:

    def test_without_any_number(self, valid_name):

        with pytest.raises(ValueError):
            contact = Contact(valid_name)

    def test_with_invalid_country_code(self, valid_name):

        with pytest.raises(ValueError):
            contact = Contact(valid_name, home_phone='+0 56748574')

    def test_with_invalid_email(self, invalid_email):

        contact = Contact(valid_name, home_phone='+372 654773644', email=invalid_email)

        assert contact.email == ''
