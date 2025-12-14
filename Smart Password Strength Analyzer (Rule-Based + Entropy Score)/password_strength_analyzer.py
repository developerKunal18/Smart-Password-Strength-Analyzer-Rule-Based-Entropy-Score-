import math
import re

def password_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[^a-zA-Z0-9]", password): pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)

def strength_label(entropy):
    if entropy < 28:
        return "Very Weak ❌"
    elif entropy < 36:
        return "Weak ⚠️"
    elif entropy < 60:
        return "Moderate 👍"
    elif entropy < 80:
        return "Strong 🔐"
    else:
        return "Very Strong 🛡️"

def crack_time(entropy):
    guesses_per_sec = 1e9  # 1 billion guesses/sec (modern GPU)
    seconds = (2 ** entropy) / guesses_per_sec

    if seconds < 60:
        return "seconds"
    elif seconds < 3600:
        return "minutes"
    elif seconds < 86400:
        return "hours"
    elif seconds < 31536000:
        return "days"
    else:
        return "years"

def feedback(password):
    tips = []
    if len(password) < 12:
        tips.append("Use at least 12 characters.")
    if not re.search(r"[a-z]", password):
        tips.append("Add lowercase letters.")
    if not re.search(r"[A-Z]", password):
        tips.append("Add uppercase letters.")
    if not re.search(r"[0-9]", password):
        tips.append("Add numbers.")
    if not re.search(r"[^a-zA-Z0-9]", password):
        tips.append("Add special characters.")

    return tips

def main():
    print("🧾 Password Strength Analyzer — Day 62\n")
    password = input("Enter a password to analyze: ")

    entropy = password_entropy(password)
    label = strength_label(entropy)
    time_est = crack_time(entropy)
    tips = feedback(password)

    print("\n📊 Analysis Result")
    print("-" * 30)
    print(f"Strength: {label}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Estimated crack time: {time_est}")

    if tips:
        print("\n⚠️ Suggestions to improve:")
        for t in tips:
            print("•", t)
    else:
        print("\n✅ Excellent password!")

if __name__ == "__main__":
    main()
