"""
Email to name dictionary
Estimate: 30 minutes
Actual:   40 minutes
"""


def extract_name(email):
    """Extract name from email address"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation not in ('', 'y'):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()