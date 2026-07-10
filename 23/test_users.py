import unittest


def get_allowed_users():
    return ["john", "jane", "bob", "alice"]


def register_user(username):
    return username.lower()


class TestUsers(unittest.TestCase):
    def test_registered_user_is_allowed(self):
        result = register_user("John")
        self.assertIn(result, get_allowed_users())

    def test_allowed_users_list(self):
        allowed_users = get_allowed_users()

        self.assertIn("john", allowed_users)
        self.assertIn("alice", allowed_users)
        self.assertNotIn("dato", allowed_users)


if __name__ == "__main__":
    unittest.main()
