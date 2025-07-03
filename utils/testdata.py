import random
import string

def random_email(domain="testmail.com"):
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{user}@{domain}"

def random_first_name():
    return ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,7)))

def random_last_name():
    return ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(4,8)))

def random_password(length=12):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    specials = '!@#$%^&*'
    sets = [lowers, uppers, digits, specials]
    chosen_sets = random.sample(sets, 3)
    password = [random.choice(s) for s in chosen_sets]
    all_chosen = ''.join(chosen_sets)
    password += random.choices(all_chosen, k=max(length - len(password), 0))
    random.shuffle(password)
    return ''.join(password)
