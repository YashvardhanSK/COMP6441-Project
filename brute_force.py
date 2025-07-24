import itertools
import time
from hash_utils import hash_password

def brute_attack(target_hash, hash_algo, charset, max):
    print("\nRunning a Brute-Force Attack")
    start = time.time()
    attempts = 0
    x = 1
    y = max+1
    while x<y:
        for pwd_tuple in itertools.product(charset, repeat=max):
            guess = ''.join(pwd_tuple)
            attempts += 1
            if hash_password(guess, hash_algo) == target_hash:
                print(f"Password got Cracked, It was - {guess}")
                print(f"Total Attempts: {attempts}")
                print(f"Time it Took: {time.time() - start:.2f} s")
                return True
        x=x+1
    print(f"Tried {attempts} combinations. Not found.")
    print(f"Time: {time.time() - start:.2f} s")
    return False
