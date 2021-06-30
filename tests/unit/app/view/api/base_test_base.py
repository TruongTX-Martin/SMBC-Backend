import pytest

from ....factories import UserFactory
from ..base_test_base import BaseTestBase


class ApiBaseTestBase(BaseTestBase):
    @pytest.fixture(scope='function')
    def auth_user(self):
        with self.app_context:
            user = UserFactory.create(password='password')

            rv = self.signin(user.email, 'password')
            parsed_data = rv.get_json()
            yield {'user': user, 'token': parsed_data['token']}

    def signin(self, email, password):
        return self.mock.post(
            '/api/v1/auth/signin',
            json={
                'email': email,
                'password': password,
            },
            content_type='application/json',
        )
