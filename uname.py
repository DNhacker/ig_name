import os
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, UserNotFound, CollectionError

def read_usernames(file_path):
    """Read usernames from a specified file and return a list of usernames."""
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return []
    
    with open(file_path, 'r') as file:
        usernames = [line.strip() for line in file if line.strip()]
    return usernames

def check_username_availability(client, username):
    """Check if a username exists on Instagram."""
    try:
        client.user_info_by_username(username)
        return True  # Username exists
    except UserNotFound:
        return False  # Username does not exist
    except (LoginRequired, CollectionError) as e:
        print(f"Error while checking username '{username}': {e}")
        return None  # Indicate an error occurred

def main():
    # Initialize the Instagrapi client
    client = Client()
    
    # Replace with your own Instagram credentials
    username = 'hr20.noname'
    password = 'Mesher@123'
    client.login(username, password)

    # Read usernames from file
    usernames = read_usernames('username.txt')
    unavailable_usernames = []
    checked_count = 0

    # Check each username for availability
    for username in usernames:
        checked_count += 1
        print(f"Checking username: {username}")
        is_available = check_username_availability(client, username)

        if is_available is False:
            unavailable_usernames.append(username)

    # Write unavailable usernames to find.txt
    with open('find.txt', 'w') as file:
        for username in unavailable_usernames:
            file.write(username + '\n')

    # Summary of results
    print(f"\nSummary of results:")
    print(f"Total usernames checked: {checked_count}")
    print(f"Unavailable usernames found: {len(unavailable_usernames)}")

if __name__ == "__main__":
    main()