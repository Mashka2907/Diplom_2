from faker import Faker

fake = Faker()

class Data:
    UPDATE_EMAIL = {'email': 'update_email@example.com'}
    UPDATE_NAME = {'name': 'update_name'}
    INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6c"]
    }
    INVALID_HASH_INGREDIENTS = {
        "ingredients": ["invalid_hash"]
    }

    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
