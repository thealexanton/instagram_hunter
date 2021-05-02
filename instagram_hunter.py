import instaloader

print("""   _____           _                                    _                 _            
 |_   _|         | |                                  | |               | |           
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |__  _   _ _ __ | |_ ___ _ __ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  | '_ \| | | | '_ \| __/ _ \ '__|
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | | | | |_| | | | | ||  __/ |   
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |_| |_|\__,_|_| |_|\__\___|_|   
                            __/ |                                                     
                           |___/                                                     
                                                    follow theastronomer123 on github
                                                                     
                           
                           
                            """)


def see_if_username_exists(username):
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        followers = profile.followers
        url = f"https://instagram.com/{username}"
        print(
            f'[+] The user {username} exists and has {followers} followers. The link is: {url}')
    except:
        print(f"[-] The username {username} does not exist.")


question1 = input("Do you want to check for a username combinations (y, n)")
if question1 == "y":
    first_name = input("What is the first name? \n").lower()
    last_name = input("What is the last name? \n").lower()
    for step in range(10):
        if step == 0:
            username = first_name + last_name
            see_if_username_exists(username)
        if step == 1:
            username = '_' + last_name + '_'
            see_if_username_exists(username)
        if step == 2:
            username = first_name[0] + '.' + last_name
            see_if_username_exists(username)
        if step == 3:
            username = first_name[0] + '_' + last_name
            see_if_username_exists(username)
        if step == 4:
            username = last_name + 'priv'
            see_if_username_exists(username)
        if step == 5:
            username = '_' + last_name
            see_if_username_exists(username)
        if step == 6:
            username = last_name + last_name[-1]
            see_if_username_exists(username)
        if step == 7:
            username = '_' + last_name + last_name[-1]
            see_if_username_exists(username)
        if step == 8:
            username = first_name[0] + last_name
            see_if_username_exists(username)
elif question1 == "n":
    usernames = input(
        "Enter username(s). Use spaces to seperate them: \n").lower()
    actual_usernames = usernames.split()
    for step in range(len(actual_usernames)):
        see_if_username_exists(actual_usernames[step])

else:
    print("Please enter correct information")
