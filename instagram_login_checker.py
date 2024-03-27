import requests

def check_password(username, passwords):
    for password in passwords:
        # Simulate login attempt with the given username and password
        response = requests.post('https://www.instagram.com/accounts/login/ajax/', 
                                 data={'username': username, 'password': password})
        
        # Check if login attempt was successful
        if 'authenticated": true' in response.text:
            print(f"Password matched: {password}")
            return
    print("No matching password found.")

if __name__ == "__main__":
    username = input("Enter Instagram username: ")
    passwords = []
    for i in range(3):
        password = input(f"Enter password {i+1}: ")
        passwords.append(password)
    
    check_password(username, passwords)
