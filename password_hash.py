#This script is for testing purpose


import hashlib

password = input("Enter password: ")
hash = hashlib.sha256(password.encode()).hexdigest()

print(hash)