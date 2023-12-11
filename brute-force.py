import zipfile
import time
import itertools
import os
import argparse

# Import color codes from the colors module
from colors import RED, GREEN, YELLOW, RESET


# Define the seed to include in the combinations
#seed = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#seed = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$.'
#seed = '0123456789'

# Read arguments from the command line according to the following format:
# python3 dictionary.py -f test.zip -d dictionary.txt
# -f: path to the zip file
# -s: seed to use for the combinations
# -l: length of the password
def main():
    parser = argparse.ArgumentParser(description='Password cracking using a dictionary')
    parser.add_argument('-f', '--zipfile', required=True, help='Path to the ZIP file')
    parser.add_argument('-l', '--length', required=True, help='Length of the password')
    parser.add_argument('-s', '--seed', required=True, help='Seed to use for the combinations')
    args = parser.parse_args()

    zip_file_path = args.zipfile
    max_length = int(args.length)
    seed = args.seed

    if not os.path.exists(zip_file_path):
        print(f'Error: ZIP file not found at {zip_file_path}')
        return

    print(f'Cracking password for {zip_file_path}')
    print(f'Seed: {seed}')
    print(f'Max length: {max_length}')

    start_time = time.time()  # Record the start time
    try:
        run_cracker(zip_file_path, max_length, seed)
    except FileNotFoundError as e:
        print(f'Error: {e}')

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f'Total time: {elapsed_time} seconds')



def generate_combinations(length, seed):
    for combination in itertools.product(seed, repeat=length):
        yield ''.join(combination)


def run_cracker(zip_file_path, max_length, seed):
    is_found = False

    for length_of_combinations in range(1, max_length + 1):
        if (is_found):
            break

        total_combinations = len(seed) ** length_of_combinations
        print(f'\nGenerating combinations of length {length_of_combinations} from {len(seed)} characters')
        print(f'Total possible combinations: {RED}{total_combinations}{RESET}')

        for password in generate_combinations(length_of_combinations, seed):
            try:
                with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                    zip_file.extractall(pwd=password.encode())
                print(f'\n🎉 Success! Password found: {GREEN}{password}{RESET}.')
                is_found = True
                break  # Exit the loop if the correct password is found
            except Exception as e:
                #print(f'Failed with password: {password}')
                pass

    if is_found == False:
        print('\n😳 Sorry I did not find the password')

if __name__ == "__main__":
    main()