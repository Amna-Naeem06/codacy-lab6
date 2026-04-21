import os
import sqlite3
import secrets

# Fix 1: environment variable
DB_PASSWORD = os.environ.get('DB_PASSWORD')

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Fix 2: parameterized query
def get_user(username):
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchone()

# Fix 3: secure OTP
def generate_otp():
    return secrets.randbelow(900000) + 100000

def main():
    user = input("Enter username: ")
    print(get_user(user))
    print("OTP:", generate_otp())

if __name__ == "__main__":
    main()