import re

def assess_password_strength(password):
    # Initialize variables
    strength = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        strength += 2  # Bonus points for length
        feedback.append("Good length! Longer passwords are more secure.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter for better security.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter for better security.")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number for better security.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Use at least one special character (e.g., @, #, $).")

    # Evaluate overall strength
    if strength <= 2:
        feedback.insert(0, "Weak password. Improve the criteria below.")
    elif strength == 3 or strength == 4:
        feedback.insert(0, "Moderate password. Could be stronger.")
    else:
        feedback.insert(0, "Strong password!")

    return feedback

# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
print("\n".join(result))
