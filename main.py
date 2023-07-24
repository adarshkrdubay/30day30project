import requests
import json
import string
import os
def logo():
	print("""
      _________          __    ___     __________
     /  _____  \        |  |  /  /    |  ______  \ 
    /  /     \  \       |  |_/  /     | |      \   \ 
   /  /_______\  \      |      /      | |       \   \ 
  /  ___________  \     |   _  \      | |       /   / 
 /  /           \  \    |  | \  \     | |______/   / 
/__/             \__\   |__|  \__\    |___________/
                     
""")
def credit():
    print("\n****************************************************************")
    print("\n* Devloped by @adarshkrdubay                                   *")
    print("\n* Copyright of AKD, 2022                                       *")
    print("\n****************************************************************")
    print("_________________________________________________________")
def send_free(phone,message):
	result = requests.post('https://textbelt.com/text', {
	  'phone': f'{phone}',
	  'message': f'{message}',
	  'key': 'textbelt',
	})
	print(result.json())

def send(phone,message,apikey):
	result = requests.post('https://textbelt.com/text', {
	  'phone': f'{phone}',
	  'message': f'{message}',
	  'key': f'{apikey}',
	})
	print(result.json())
def welcome():
	
	print("""This project work on textbelt API.
	So it just provide 1 message per day for free user.
	To send more than 1 message you need to buy key from officle website of TextBelt(https://textbelt.com/). """)
	print("Welcome to the wiz fake.")
	print("You can send custom message to anyone.")
	print("Do not use this for misscellaneous purpose.")

def free_user():
	resever_number=input("Enter the number to which you want to send message( with code ):\n")
	message_send=input("Enter the text which you want to send:\n")
	print(f"Sending message : '{message_send}' to '{resever_number}'")
	send_free(resever_number,message_send)

def user():
	apikey_file = os.path.exists('api.key')
	if apikey_file == True:
			apikey=open("api.key","r")
			apikey=apikey.read()
	else:
		apikey=input("Enter the api key provide by the site:\n")
		option=input("Do you want to store the api key:(y/n)\n").lower()
		if option=="y":
			os.system(f"echo {apikey} > api.key")
			print("we have saved your api to api.key file in same place where this code is saved")
		elif option=="n":
			 return
		else:
			print("Incorrect options so we have saved your api to api.key file in same place where this code is saved")
	resever_number=input("Enter the number to which you want to send message( with code ):\n")
	message_send=input("Enter the text which you want to send:\n")
	print(f"Sending message : '{message_send}' to '{resever_number}'")
	send(resever_number,message_send,apikey)
def option():
		option=input("Input 1 to use free version(One SMS per day).\n2 for use with paid version:\n") 
		if option=="1":
			free_user()
		elif option=="2":
			user()
		else:
			print("Incorrect options")
			option_loop()
			
def option_loop():
	option()
def main():
	logo()
	credit()
	welcome()
	option()
	
if __name__ == '__main__':
	main()
