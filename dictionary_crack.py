import time
from hash_utils import hash_password

def dictionary_crack(final, hash_algo, file):
    print("\nRunning a Dictionary Attack")
    start = time.time()
    count = 0
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue
                count += 1
                if hash_password(password, hash_algo) == final:
                    print(f"Cracked the Password: {password}")
                    print(f"Total Attempts: {count}")
                    print(f"Time: {time.time() - start:.2f} s")
                    return True
        print(f"Tried {count} passwords. Not found.")
    except FileNotFoundError:
        print(f"Dictionary file '{file}' not found.")
    print(f"Time: {time.time() - start:.2f} s")    
    return False
