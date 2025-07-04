import random
import string

def random_email(domain="testmail.com"):
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{user}@{domain}"

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
