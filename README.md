A python script to crack hashed passwords (SHA256), using dictionary attack method.
Additional features:
    1. Can check for multiple hashes at once.
    2. Can run multiple threads.

**How to use**

1. Enter all you hashed passwords in a file or use the provided one.
2. Get a password dictionary file or use the provided one.
3. Run hash_crack.py
    ```python hash_crack.py```
4. Enter path to password dictionary file.
5. Enter path to hashed passwords file.
6. Enter number of threads to launch per hash.
    If you hashed password file contains 5 hashed passwords and you enter 3 as number of threads, 3 threads for each hash will be launched, launching a total of 5 x 3 = 15 threads. Large number of threads is useful only when the dictionary.txt file is too big.
7. If a password is cracked successfully, the program will output it in the format:
    Match found for hash: <hash of the password>, Password: <password>

    No output means none of the hashes could be cracked.
