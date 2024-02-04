import bcrypt
import getpass
def save_login_id(username, password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(f"Login ID saved for user '{username}'.")
def authenticate_user(username, password):
    hashed_password = b'$2b$12$1BsZu.4q0uoY2e0ffwVz9O4CkCL8SWu3/Nb.4IK7tqrhM6ujDhM6K'
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(f"Authentication successful for user '{username}'.")
    else:
        print(f"Authentication failed for user '{username}'.")
if __name__ == "_main_":
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    save_login_id(username, password)
    authenticate_user(username, getpass.getpass("Enter your password for authentication: "))