import string

def check_password_strength(password):
    # Define criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special_char": any(char in string.punctuation for char in password),
    }

    # Determine password strength
    if all(criteria.values()):
        return "Strong password"
    elif sum(criteria.values()) >= 3:
        return "Moderate password"
    else:
        return "Weak password"

try:
    user_password = input("Enter a password: ")
    strength = check_password_strength(user_password)
    print(f"Password strength: {strength}")
except Exception as e:
    print("An error occurred:", e)
