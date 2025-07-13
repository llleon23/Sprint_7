from faker import Faker
fake = Faker()

def fake_login():
    login_fake = fake.user_name()
    return login_fake

def fake_password():
    password_fake = fake.random_number(4)
    return password_fake

def fake_firstname():
    firstname_fake = fake.first_name()
    return firstname_fake

def fake_lastname():
    lastname_fake = fake.last_name()
    return lastname_fake

def fake_address():
    address_fake = fake.address()
    return address_fake
