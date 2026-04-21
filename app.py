import sqlite3
import random

# ❌ Hardcoded password (vulnerability)
DB_PASSWORD = "12345"

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def get_user(username):
    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# ❌ Insecure random
def generate_otp():
    return random.randint(100000, 999999)

# ❌ Unused variable
unused_count = 0

def main():
    user = input("Enter username: ")
    print(get_user(user))
    print("OTP:", generate_otp())

if __name__ == "__main__":
    main()