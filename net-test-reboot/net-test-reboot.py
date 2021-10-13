import os
import requests
import time

MAX_FAILS = 3 # times
RETRY_INTERVAL = 30 # secs
fails_count = 0

def run():
    connection_on = internet_on()
    global fails_count
    retry_needed = False
    if not connection_on:
        print('Increasing fails count to {}'.format(fails_count+1))
        fails_count += 1
        retry_needed = True
    elif fails_count > 0:
        print('Reseting fails count to 0')
        fails_count = 0

    if fails_count >= MAX_FAILS:
        print('Rebooting system')
        os.system("shutdown -t 0 -r -f")
        retry_needed = False
    
    return retry_needed

def internet_on():
    print('Testing internet connection...')
    try:
        requests.get('https://google.com', timeout=1)
        print('Test PASSED')
        return True
    except (requests.ConnectionError, requests.Timeout) as err:
        print('Test FAILED')
        return False

if __name__ == "__main__":
    print('--- START SCRIPT: Internet connection test ---')
    while run():
        print('Retrying in {} secounds...'.format(RETRY_INTERVAL))
        time.sleep(RETRY_INTERVAL)
        print('Retesting internet connection now.')
    print('--- STOP SCRIPT: Internet connection test ---')
    