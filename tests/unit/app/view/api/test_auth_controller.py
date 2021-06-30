import pytest

from ....factories import UserFactory
from .base_test_base import ApiBaseTestBase as BaseTestBase


class TestAuthController(BaseTestBase):
    @pytest.fixture(scope='function')
    def prepare_user(self):
        with self.app_context:
            user = UserFactory.create(password='password')
            yield user

    def test_login_success(self, prepare_user):
        rv = self.signin(prepare_user.email, 'password')
        assert rv.status_code == 200
        parsed_data = rv.get_json()
        assert parsed_data['token'], 'login did not succeeded'

    def test_login_fail_invalid_email(self):
        rv = self.signin('not-found@gmail.com', 'password')
        assert rv.status_code == 400
        parsed_data = rv.get_json()
        assert parsed_data['message'] == 'Incorrect username or password'

    def test_login_fail_not_email_address(self):
        rv = self.signin('nexus', 'password')
        assert rv.status_code == 400
        parsed_data = rv.get_json()
        assert parsed_data['message'] == 'Parameter error'

    def test_login_fail_invalid_password(self, prepare_user):
        rv = self.signin(prepare_user.email, 'wrong-password')
        assert rv.status_code == 400
        parsed_data = rv.get_json()
        assert parsed_data['message'] == 'Incorrect username or password'
