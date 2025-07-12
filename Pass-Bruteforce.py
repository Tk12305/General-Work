import itertools
import string
import time

def brute_force_crack(target_password, max_length=5):
    characters = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            print("Trying:", guess_password)

            if guess_password == target_password:
                end_time = time.time()
                print("Password found:", guess_password)
                print("Attempts:", attempts)
                print("Time taken:",(end_time - start_time),"seconds")
                return guess_password

    print("Password not found.")
    return None

#input password
if __name__ == "__main__":
    password_to_crack = "19681"  # Set the password here max 5 characters or int
    brute_force_crack(password_to_crack, max_length=5)