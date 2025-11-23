import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 1:
        return "Weak"

    elif strength == 2 or strength == 3:
        return "Medium"

    else:
        return "Strong"

def password_guidelines():
    print("\n--- Guidelines to create a strong password ---")
    print("✔ There must be atleast 8 characters")
    print("✔ Both uppercase and lowercase letters should be included in your password.")
    print("✔ There must be present atleast one digit from (0–9)")
    print("✔ At least one special character among (!, @, #, $, %, etc.) must be included\n")
