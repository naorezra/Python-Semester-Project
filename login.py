from hashlib import sha256

# Naor Ezra 205923758 && Shira Alon 316165026 class : 45.2

DATA_PATH = 'credentials.txt'


def encoding(user_password: str) -> str:
	"""
	:param user_password: get user password as a parameter
	:return: user password after encoding in Sha256 encoding
	"""

	# Encrypt password in SHA256 encryption
	return sha256(user_password.encode()).hexdigest()


def login(user_name: str, user_password: str) -> bool:
	"""
	:param user_name: Gets user name as a parameter
	:param user_password: Gets user password as a parameter
	:return: Returns true if username and password are correct (found in file and equal) and false if not correct
	"""

	# Generates an encrypted password using the function
	after_encoding_password = encoding(user_password)

	try:
		with open(DATA_PATH, 'r') as file:  # open file in read mode
			for line in file.readlines():  # Go line by line on the file
				# strip to remove spacing from string and split to split the strings to
				# list line after line no separator because is do it at the default(" ")
				parameter = line.strip().split()

				# check if user name and password correct
				if user_name == parameter[0] and after_encoding_password == parameter[1]:
					return True

		return False

	except PermissionError:
		print("Error. No file access")
	except FileNotFoundError:
		print("Error. File not exists")
