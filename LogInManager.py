username_db = ["ironman"]
pw_database = ["xxx"]

def main():
	response = input("'Logon' or 'create' ?").lower()

	if response == "logon":
		log_on()
	elif response == "create":
		username = input("What is desired username?")	#assigns input to username var
		myUserName(username)

		password = input("Type password. Must have at least 3 characters. ")
		myPassword(password)
		main()
	else:
		print("Invalid response. ")
		main()

def myUserName(username) : #calls func with variable parameter

	if len(username) < 3 :
		print("User name too short")
		main()
	elif username in username_db:
		print("Username already taken. ")
		main()
	else:
		print("Got it! Your username is " + username)
		username_db.append(username)

invalid_input = True #Preset to True. If False, triggers another menu...


def myPassword(password):	#calls func with variable parameter
	while True:
		if len(password) >= 3 :
			matchPass = input("Confirm password ")
			if matchPass == password :
				print("Password recorded successfully. You may log on now. ")
				pw_database.append(password)
				print(pw_database)
			else:
				print("Passwords do not match")
				continue
		else:
			print("Password too weak. Try again. ")
			main() #loops back to square one



def log_on():
	username = input("What is username: ")

	if username in username_db : #searches for input in darabase var
		#invalid_input = False
		print("Account found.") #continues to pw section
	else:
		print("Error 4013")
		main()
	logon_pw = input("Enter password")

	if logon_pw in pw_database:
		print("Success")
		main()
	else:
		print("Incorrect set of parameters entered") #Runs line 63
		invalid_input = True


		while invalid_input :
			count = 1
			while count <= 3 :

			#print("searching records... ") #Runs line 70

					#break? #Otherwise would crash program forever...
					#I need to find a way to loop back to "enter pw" when input is wrong.

				att_pw = input("Enter password...")

				if att_pw in pw_database :
						print("Success. ")
						invalid_input = False
						main()
						#invalid_input = False #Toggle ?
				#elif att_pw not in pw_database:
				#	count +=1
				#	if count == 3 :
				#		print("Max number of attemtps allowed...")
				else:
					count += 1

				if count == 3:
					print("Max number of attemtps allowed...")
					quit("Have a nice day... ")



main()
