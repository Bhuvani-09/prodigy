import re

def password_strength_checker(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&#]', password))

    # Count the number of criteria met
    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    # Determine strength based on criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met == 4:
        strength = "Moderate"
    elif criteria_met == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Include at least one special character (e.g., @, $, !, %, *, ?, &, #).")

    return strength, feedback

def main():
    print("Welcome to the Password Complexity Checker!")
    password = input("Enter your password to check its strength: ")

    strength, feedback = password_strength_checker(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
