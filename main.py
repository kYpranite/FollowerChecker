from instagrapi import Client
import configparser

parser = configparser.ConfigParser()
parser.read("config.txt")

USERNAME = parser["Account"]["username"]
PASSWORD = parser["Account"]["password"]

cl = Client()
cl.login(USERNAME, PASSWORD)
userId = cl.user_id

followersList = [user.username for user in cl.user_followers_v1(userId, 0)]
followingList = [user.username for user in cl.user_following_v1(userId, 0)]

result = set(followingList) - set(followersList)

response = input("do you want to export? (y/n): ")

if response.upper() == "Y":
    with open("output.txt", "w") as myfile:
        myfile.write('\n'.join(result))

for username in result:
    print("do you want to unfollow " + username + "? they do not follow you back (y - yes)")
    print("https://www.instagram.com/" + username + "/")
    response = input()
    if response.upper() == "Y":
        user = cl.user_info_by_username(username).dict()
        cl.user_unfollow(user["pk"])
