import os
from instagrapi import Client

def main():
    # Prompt for Instagram login credentials
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    
    # Instantiate the Instagram client
    client = Client()
    
    try:
        # Login to Instagram
        client.login(username, password)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")
        return
    
    # File paths
    usernames_file = "username.txt"
    not_exists_file = "not_exists.txt"
    
    # Check if the usernames file exists
    if not os.path.exists(usernames_file):
        print(f"The file '{usernames_file}' does not exist in the script's root directory.")
        return
    
    # Create the not_exists file if it doesn't exist
    if not os.path.exists(not_exists_file):
        open(not_exists_file, "w").close()
        print(f"Created file '{not_exists_file}' for saving unavailable usernames.")
    
    # Read usernames from the file
    with open(usernames_file, "r") as file:
        usernames = [line.strip() for line in file if line.strip()]
    
    # List to store usernames that don't exist
    not_exists = []
    
    # Verify each username
    for user in usernames:
        try:
            user_info = client.user_info_by_username(user)
            print(f"Username '{user}' exists on Instagram.")
        except Exception:
            print(f"Username '{user}' does not exist on Instagram.")
            not_exists.append(user)
    
    # Save unavailable usernames to a file
    with open(not_exists_file, "w") as file:
        file.write("\n".join(not_exists))
    
    print(f"Usernames that do not exist have been saved to '{not_exists_file}'.")

if __name__ == "__main__":
    main()
