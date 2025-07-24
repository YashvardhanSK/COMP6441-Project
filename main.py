from brute_force import brute_attack
from dictionary_crack import dictionary_crack

def disclaim():
    print("*" * 21)
    print("This tool is only to learn about hashes and algorithms")
    print("*" * 21)
    print()

def main():
    disclaim()
    hash = input("Which hash you want to crack- ").strip()
    algo = input("Available Hashes Algorithms (md5,sha1,sha256)- ").strip().lower()
    if algo not in ['md5', 'sha1', 'sha256']:
        print("Not Eligible")
        return
    print("Which attack method do you want to use:")
    print("1. Brute")
    print("2. Dict")
    method = input("> ").strip()
    solved = False
    if method == '1':
        chars = input("Enter the set of all characters: ").strip()
        max = int(input("Enter max length: "))
        solved = brute_attack(hash, algo, chars, max)
    elif method == '2':
        dict_file = input("Enter dictionary file: ").strip()
        if not dict_file:
            dict_file = "dict.txt"
        solved = dictionary_crack(hash, algo, dict_file)
    else:
        print("Not Valid :/")
    if not solved:
        print("\nPassword Not Found, Unfortunately :)")
        print("The Hash is Strong")

if __name__ == "__main__":
    main()

