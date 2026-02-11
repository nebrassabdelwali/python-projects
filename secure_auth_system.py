import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    password = getpass.getpass("Create a password: ")
    hashed = hash_password(password)
    print("\nUser registered successfully.")
    print("Stored hash:", hashed)
    return hashed

def login(stored_hash):
    password = getpass.getpass("Enter your password: ")
    if hash_password(password) == stored_hash:
        print("\nLogin successful ✅")
    else:
        print("\nLogin failed ❌")

def main():
    stored_hash = register()
    print("\nNow login:")
    login(stored_hash)

if __name__ == "__main__":
    main()
