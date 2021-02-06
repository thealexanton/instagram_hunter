import requests

print("""   _____           _                                    _                 _            
 |_   _|         | |                                  | |               | |           
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |__  _   _ _ __ | |_ ___ _ __ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  | '_ \| | | | '_ \| __/ _ \ '__|
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | | | | |_| | | | | ||  __/ |   
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |_| |_|\__,_|_| |_|\__\___|_|   
                            __/ |                                                     
                           |___/                                                     
                                                                  follow me on github
                                                                     
                           
                           
                            """)


def see_if_username_excists(username):
    username = "thealexanton"
    response = requests.get("https://instagram.com/" + username + "/")
    if response.status_code == 404:
        print(f"The username {username} is not taken")
    else:
        print(f"The username {username} excists")


question1 = input("Do you want to check for a singe username? (y, n)")
if question1 == "y":
    first_name = input("What is the first name?").lower()
    last_name = input("What is the last name?").lower()
    possible_usernames = []

    for step in range(10):
        if step == 0:
            username = first_name + last_name
            possible_usernames.append(username)
            see_if_username_excists(username)
elif question1 == "n":
    single_username = input("Enter username:").lower()
    see_if_username_excists(single_username)
else:
    print("Please enter correct information")
