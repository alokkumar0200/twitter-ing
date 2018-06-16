import requests
from requests_oauthlib import OAuth1
import json
try:
	#   Place Your Keys Here
	url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
	API_KEY = ''
	API_SECRET = ''
	ACCESS_TOKEN = ''
	ACCESS_TOKEN_SECRET = ''
	auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	requests.get(url, auth=auth)

	def search_by_id():
		id = input('Enter any twitter id to search for: \n')
		r = requests.get('https://api.twitter.com/1.1/users/search.json?q='+id+'&count=5', auth=auth)
		text = json.loads(r.text)
		print("")
		print("[*] Process Completed\n")
		print("[*] Details of Target\n")
		print("Name: "+text[0]['name'])
		print("Profile Description: "+text[0]['description'])
		print("Number of followers: "+str(text[0]['followers_count']))
		print("Number of friends: "+str(text[0]['friends_count']))
		print("Number of tweets: "+str(text[0]['statuses_count']))
		print("Last Tweet: "+text[0]['status']['text'])
		print("Created At: "+text[0]['status']['created_at'])
		print("Location: "+text[0]['location'])
		print("Link to Profile Picture: "+text[0]['profile_image_url'])
		print("")
		input("Press Enter To Continue")
		print("")
		main()

	

	def frnd_lst():
		id = input('Enter any twitter id to list names person is following\n')
		r = requests.get('https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name='+id+'&skip_status=true&include_user_entities=false', auth=auth)
		text = json.loads(r.text)
		if text:
			print("")
			print("[*] Process Completed\n")
			print("[*] List of people to whoom target is following\n")
			for x in text.get('users', []):
				print(x['screen_name']+"	----	"+x['name'])
			while (text.get('next_cursor', [])):
				n = text.get('next_cursor', [])
				r = requests.get('https://api.twitter.com/1.1/friends/list.json?cursor='+str(n)+'&screen_name='+id+'&skip_status=true&include_user_entities=false', auth=auth)
				text = json.loads(r.text)
				try:
					for x in text.get('users', []):
						print(x['screen_name']+"	----	"+x['name'])
				except:
					break
		print("")
		input("Press Enter To Continue")
		print("")
		main()
	

	def main():
		bann = """
				 _            _ _   _                 _             
		| |___      _(_) |_| |_ ___ _ __     (_)_ __   __ _ 
		| __\ \ /\ / / | __| __/ _ \ '__|____| | '_ \ / _` |
		| |_ \ V  V /| | |_| ||  __/ | |_____| | | | | (_| |
		 \__| \_/\_/ |_|\__|\__\___|_|       |_|_| |_|\__, |
        						      |___/ 
		"""
		print(bann)
		print("		Choose any Option\n")
		print("1. View Details About Target\n")
		print("2. View List Of People The Target Is Following\n")
		print("Press Ctrl + C To Exit.")
		inpt = input("->	")
		if inpt == "1":
			search_by_id()
		if inpt == "2":
			frnd_lst()
		else:
			print("Wrong Input.")
			input("Press Enter To Continue\n")
			main()

	if __name__ == "__main__":
		main()


except KeyboardInterrupt:
	print("\nInterrupted By User")
