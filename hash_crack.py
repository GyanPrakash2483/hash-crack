import hashlib
import threading
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("dictionary_path", help="Path to password dictionary")
parser.add_argument("Hash_path", help="Path to hashes to crack")
parser.add_argument("Threads", help="No of threads per hash")

args = parser.parse_args()

dictionary_path = args.dictionary_path
hash_path = args.Hash_path
threads = args.Threads
threads = int(threads)

#get the list of hashes to crack
hashes = []
try:
    with open(hash_path) as file:
        hashes = file.readlines()
        for i in range(len(hashes)):
            hashes[i] = hashes[i].strip()

except Exception as e:
    print(e)

#get the list of passwords
passwords = []
try:
    with open(dictionary_path) as file:
        passwords = file.readlines()
        for i in range(len(passwords)):
            passwords[i] = passwords[i].strip()

except Exception as e:
    print(e)

#divide password files into chunks for each thread

chunk_size = len(passwords) // threads

chunks = []
trav = 0
for i in range(threads):
    chunks.append([])
    chunk = chunks[i]
    for j in range(chunk_size):
        chunk.append(passwords[i*chunk_size + j])
        trav += 1

while trav < len(passwords):
    chunks[0].append(passwords[trav])
    trav += 1
# cracking function
def crack_password(target_hash, dictionary):
    for password in dictionary:
        if hashlib.sha256(password.encode()).hexdigest() == target_hash:
            print("Match found for hash: " + target_hash + ", Password: " + password)
            return 0


# Launch threads for each chunk
for target_hash in hashes:
    for dictionary in chunks:
        thread = threading.Thread(target=crack_password, args=(target_hash, dictionary))
        thread.start()