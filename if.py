# User authentication example
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Authentication successful. Welcome, admin!")
else:
    print("Authentication failed. Please check your credentials.")
