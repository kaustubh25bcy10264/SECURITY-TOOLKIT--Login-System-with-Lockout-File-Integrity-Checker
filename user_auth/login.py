import time
import logging
import data.users as data_of_users  

def login(username, password):
    if username not in data_of_users.users:
        logging.warning(f"Login failed: This '{username}' not available in registered users.")
        print(f"Your login is failed. This {username} is not registered! Please Enter correct username!")
        return False

    
    if time.time() < data_of_users.lockout_time.get(username, 0):
        remaining = int(data_of_users.lockout_time[username] - time.time())
        logging.warning(f"user {username} attempted a login during lockout. User {username} can login again after {remaining} seconds.")
        print("---------------------------------")
        print(f"⚠️ Account locked! Due to multiple failures of your login attempts, your account is locked. Try again after {remaining} seconds.")
        print("---------------------------------")
        return False

    
    if data_of_users.users[username] == password:
        logging.info(f"{username} logged in successfully.")
        print("✅ Login successful!")
        data_of_users.failed_attempts[username] = 0
        data_of_users.user_logged_in = username  
        return True
    else:
        data_of_users.failed_attempts[username] += 1
        logging.warning(f"{username} failed login attempt {data_of_users.failed_attempts[username]}")
        print(f"❌ Wrong password! Password you entered is wrong. Please try again. Attempt {data_of_users.failed_attempts[username]}")
        
        
        if data_of_users.failed_attempts[username] >= 3:
            data_of_users.lockout_time[username] = time.time() + data_of_users.LOCK_DURATION
            logging.error(f"User {username} account is locked for {data_of_users.LOCK_DURATION} seconds due to his multiple failed attempts.")
            print("---------------------------------")
            print(f"⚠️ Too many failed attempts. Your Account is locked for {data_of_users.LOCK_DURATION} seconds.")
            print("---------------------------------")
            data_of_users.failed_attempts[username] = 0
        return False

