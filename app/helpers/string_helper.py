import random
import string


class StringHelper(object):
    @classmethod
    def random_string(self, string_length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))

    @classmethod
    def is_validate_password(cls, password, min_: int = 8, max_: int = 30):
        """
        Password must contain between 8 and 30 characters,
         at least one capital letter,
         at least one numeric digit,
         and at least one special character (such as $ or !)

        """

        symbols = [
            '[', '$', '&', '+', ',', ':', ';', '=', '?', '@', '#', '|', '<',
            '>', '.', '-', '^', '*', '(', ')', '%', '!', ']', '"'
        ]

        if len(password) < min_:
            return False

        if len(password) > max_:
            return False

        if not any(char.islower() for char in password):
            return False

        if not any(char.isupper() for char in password):
            return False

        if not any(char.isdigit() for char in password):
            return False

        if not any(char in symbols for char in password):
            return False

        return True
