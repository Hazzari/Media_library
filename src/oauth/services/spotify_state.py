import secrets
import string


def generate_spotify_state(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(secrets.choice(letters_and_digits) for _ in range(length))
