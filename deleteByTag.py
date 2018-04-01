# Alex Luckerman, 4/1/18
# Deletes Pocket articles by a specific tag

from pocket import Pocket
import webbrowser

# Consumer key for the desktop application
consumer_key=

#Check to see if authorization has already been completed
token_file = open("access_token.txt", 'a')
token_file.close()
token_file = open("access_token.txt", 'r')
if token_file.mode == "r":
    print("Access token file opened successfully")
    access_token = token_file.read()
    print(access_token)
    

#Authorize the app and obtain the access token
if access_token == "":
    request_token = Pocket.get_request_token(consumer_key=consumer_key, redirect_uri='https://alexlucky.me/')
    auth_url = Pocket.get_auth_url(code=request_token, redirect_uri='https://alexlucky.me/')
    
    print("Opening your browser to continue authorization...")
    webbrowser.open(auth_url, new=2, autoraise=True)
    print("If that failed, you can open the URL manually:")
    print(auth_url)
    
    done = raw_input("Once you're finished with that, come back and press enter\n")
    
    user_credentials = Pocket.get_credentials(consumer_key=consumer_key, code=request_token)
    access_token = user_credentials['access_token']
    print(access_token)
    token_file.close()
    token_file = open("access_token.txt", "a")
    token_file.write(access_token)
    token_file.close()
else:
    print('Found existing authorization code')

# Prompt user about the tag whose articles must be deleted
tag = raw_input('What tag do you want to delete everything for?\n')

pocket_instance = Pocket(consumer_key, access_token)
get_return = pocket_instance.get(consumer_key, access_token, tag=tag)

print("This is as far as I got, here's what Pocket sent back for that tag")
items = get_return[0][u'list'].keys()

print(items)
for item_id in items:
    pocket_instance.delete(item_id)
pocket_instance.commit()

print("Done. All items for that tag should now be deleted.")