from instagrapi import Client
from dotenv import load_dotenv
import os
import csv

load_dotenv()
cl = Client()

USERNAME = os.getenv('ACCOUNT_USERNAME')
PASSWORD = os.getenv('PASSWORD')
cl.login(USERNAME, PASSWORD)
sessions_path = 'sessions/dump.json'
cl.dump_settings('sessions/dump.json')
# use when already ran
cl.load_settings(sessions_path)

username = input("Username to get followers from: ")
amount = input("Amount of followers to extract")
# turn username into id
user_id = cl.user_id_from_username(username=username)
user_followers = cl.user_followers(user_id= str(user_id), amount = 0)

# add users to csv file
with open('followers.csv', 'w') as f: 
    print('Started writing')
    for follower in user_followers:
        username = user_followers[follower].username 
        csvwriter = csv.writer(f)
        csvwriter.writerow([username])

    print('Completed succesfully')
