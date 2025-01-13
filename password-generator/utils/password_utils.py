import random
import string

def generate_unique_password(characters, length, db_manager):
    """Generate a password and ensure it is unique in the database."""
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if not db_manager.password_exists(password):
            break
    return password

def calculate_password_strength(password):
    """Calculate the strength of the password."""
    length = len(password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"