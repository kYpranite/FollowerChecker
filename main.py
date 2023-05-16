from instagrapi import Client

USERNAME = "USERNAME_HERE"
PASSWORD = "PASSWORD_HERE"


cl = Client()
cl.login(USERNAME, PASSWORD)
userId = cl.user_id

followers = cl.user_followers_v1(userId, 0)
following = cl.user_following_v1(userId, 0)

followersList = [user.username for user in followers]
followingList = [user.username for user in following]

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
        bitch = cl.user_info_by_username(username).dict()
        cl.user_unfollow(bitch["pk"])
