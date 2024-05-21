# Exponential Backoff
# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries

import time

wait_time = 1
max_retries = 2
attempts  = 0
password = 'password'

while True:
    user_input = input('Please enter the password: ').strip()
    
    if attempts < max_retries:
        if password == user_input:
            print('Logged in Successfully')
            break
        else:
            print('wrong password')
            print(f'Attempt {attempts+1} - wait time {wait_time}s')
            time.sleep(wait_time)
            wait_time*=2
            attempts+=1
    else:
        print('You are blocked. Please contact our customer care.') 
        break

