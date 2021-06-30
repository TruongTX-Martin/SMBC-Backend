
from ....factories import (UserFactory)
from .base_test_base import ApiBaseTestBase as BaseTestBase


class TestMeController(BaseTestBase):
    def get_me(self, auth_user):
        return self.mock.get(
            '/api/v1/me',
            content_type='application/json',
            headers={"Authorization": "JWT {}".format(auth_user['token'])},
        )

    def test_get_me_success(self, auth_user):
        rv = self.get_me(auth_user)

        assert rv.status_code == 200

        parsed_data = rv.get_json()
        user = auth_user.get('user')
        assert parsed_data['id'] == user.id
        assert parsed_data['email'] == user.email
