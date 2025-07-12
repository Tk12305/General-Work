import itertools
import string
import time

def brute_force_crack(target_password, max_length=8, verbose=False):
    characters = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)

            if verbose:
                print("Trying:", guess_password)

            if guess_password == target_password:
                end_time = time.time()
                print("Password found:", guess_password)
                print("Attempts:", attempts)
                print("Time taken: {:.2f} seconds".format(end_time - start_time))
                return guess_password

    print("Password not found.")
    return None

# Entry point
if __name__ == "__main__":
    password_to_crack = "1234"  # Up to 8 characters
    brute_force_crack(password_to_crack, max_length=8, verbose=False)
