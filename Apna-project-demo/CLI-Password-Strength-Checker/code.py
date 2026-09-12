import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1    
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^Z&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special charecter.")

    print(f"\n---- Password Analysis ----")
    if score == 5:
        print("Strength: Strong") 
    elif score >= 3:
        print("Strength: Medium")
    else:
        print("Strength: Week")
    if feedback:    
        print("\nSuggestion to improve:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__ main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)       
