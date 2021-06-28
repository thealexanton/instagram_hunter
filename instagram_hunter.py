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


def username_exists(username):
    print(f"[+] - Checking Username: {username} ...")
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        followers = profile.followers
        url = f"https://instagram.com/{username}"
        print(
            f'[+] - The user {username} exists and has {followers} followers. The link is: {url}')
    except:
        print(f"[-] - The username {username} does not exist.")


answer = input(
    "Do you want to check for a username combinations ? (y, n)").lower()

if answer == "y":
    first_name = input("What is the first name? \n").lower()
    last_name = input("What is the last name? \n").lower()
    permutations = [first_name + last_name, '_' + last_name + '_', first_name[0] + '.' + last_name, first_name[0] + '_' + last_name, last_name + 'priv',
                    '_' + last_name, last_name + last_name[-1], '_' + last_name + last_name[-1], first_name[0] + last_name, first_name + '.' + last_name]
    for username in permutations:
        username_exists(username)

elif answer == "n":
    raw_usernames = input(
        "Enter username(s). Use spaces to seperate them: \n").lower()
    splitted_usernames = raw_usernames.split()
    for username in splitted_usernames:
        username_exists(username)

else:
    print("[!] - Error: Invalid Option.")
