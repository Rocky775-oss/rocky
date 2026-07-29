import math
import string

password = input("Enter your password: ")


def show_progress(strength):
    percent = {"Very weak": 20, "Weak": 20, "Medium": 50, "Strong": 100, "Very Strong": 100}[strength]
    filled_blocks = percent // 10
    empty_blocks = 10 - filled_blocks
    bar = "█" * filled_blocks + "░" * empty_blocks
    return f"{bar} {percent}%"


def get_strength_label(score):
    if score <= 1:
        return "🔴 Very Weak"
    elif score <= 2:
        return "🟠 Weak"
    elif score <= 3:
        return "🟡 Medium"
    elif score <= 4:
        return "🟢 Strong"
    else:
        return "🟢 Very Strong"


def estimate_crack_time(password):
    common_passwords = {"password", "123456", "12345", "abcdef", "qwerty", "admin", "letmein", "welcome"}

    if password in common_passwords:
        return "Instantly (very weak)"

    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char in string.punctuation for char in password):
        charset_size += 33

    if charset_size == 0:
        charset_size = 1

    entropy = len(password) * math.log2(charset_size)
    guesses = 2 ** entropy
    seconds = guesses / 1_000_000

    if seconds < 60:
        return f"About {seconds:.0f} seconds"
    if seconds < 3600:
        return f"About {seconds / 60:.1f} minutes"
    if seconds < 86400:
        return f"About {seconds / 3600:.1f} hours"
    if seconds < 31_536_000:
        return f"About {seconds / 86400:.1f} days"
    return f"About {seconds / 31_536_000:.1f} years"


def check_strength(password):
    common_passwords = {"password", "123456", "12345", "abcdef", "qwerty", "admin", "letmein", "welcome"}

    if password in common_passwords:
        label = "🔴 Very Weak"
        print(show_progress("Very weak"))
        print(label)
        print(f"Length: {len(password)}")
        print(f"Uppercase: {'Yes' if any(char.isupper() for char in password) else 'No'}")
        print(f"Lowercase: {'Yes' if any(char.islower() for char in password) else 'No'}")
        print(f"Numbers: {'Yes' if any(char.isdigit() for char in password) else 'No'}")
        print(f"Symbols: {'Yes' if any(char in string.punctuation for char in password) else 'No'}")
        print("Entropy: Low")
        print(f"Estimated crack time: {estimate_crack_time(password)}")
        return "Very weak: this is a commonly used password"

    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 1:
        result = "🔴 Very Weak"
    elif score <= 2:
        result = "🟠 Weak"
    elif score <= 3:
        result = "🟡 Medium"
    elif score <= 4:
        result = "🟢 Strong"
    else:
        result = "🟢 Very Strong"

    if len(password) >= 12:
        entropy = "High"
    elif len(password) >= 8:
        entropy = "Medium"
    else:
        entropy = "Low"

    print(show_progress("Very Strong" if score >= 5 else "Strong" if score == 4 else "Medium" if score == 3 else "Weak" if score == 2 else "Very weak"))
    print(result)
    print(f"Length: {len(password)}")
    print(f"Uppercase: {'Yes' if any(char.isupper() for char in password) else 'No'}")
    print(f"Lowercase: {'Yes' if any(char.islower() for char in password) else 'No'}")
    print(f"Numbers: {'Yes' if any(char.isdigit() for char in password) else 'No'}")
    print(f"Symbols: {'Yes' if any(char in string.punctuation for char in password) else 'No'}")
    print(f"Entropy: {entropy}")
    print(f"Estimated crack time: {estimate_crack_time(password)}")
    return result


check_strength(password)