import zipfile
import time
import os
import argparse

# Import color codes from the colors module
from colors import RED, GREEN, YELLOW, RESET

# Uses a dictionary to crack the password The dictionary is a list of words

# Read arguments from the command line according to the following format:
# python3 dictionary.py -f test.zip -d dictionary.txt
# -f: path to the zip file
# -d: path to the dictionary file
def main():
    parser = argparse.ArgumentParser(description='Password cracking using a dictionary')
    parser.add_argument('-f', '--zipfile', required=True, help='Path to the ZIP file')
    parser.add_argument('-d', '--dictionary', required=True, help='Path to the dictionary file')
    args = parser.parse_args()

    zip_file_path = args.zipfile
    dictionary_path = args.dictionary

    if not os.path.exists(zip_file_path):
        print(f'Error: ZIP file not found at {zip_file_path}')
        return

    if not os.path.exists(dictionary_path):
        print(f'Error: Dictionary file not found at {dictionary_path}')
        return

    print(f'Cracking password for {zip_file_path}')
    print(f'Using dictionary: {dictionary_path}')

    start_time = time.time()  # Record the start time

    try:
        run_cracker(zip_file_path, dictionary_path)
    except FileNotFoundError as e:
        print(f'Error: {e}')

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f'Total time: {elapsed_time} seconds')


def run_cracker(zip_file_path, dictionary_path):
    """
    Cracks the password of a ZIP file using a dictionary attack.

    Args:
        zipfile_path (str): The path to the ZIP file to be cracked.
        dictionary_path (str): The path to the dictionary file containing potential passwords.

    Returns:
        None

    Raises:
        FileNotFoundError: If the ZIP file or dictionary file is not found.
    """
    is_found = False

    with open(dictionary_path, 'r', encoding='latin-1') as dictionary_file:
        for line in dictionary_file.readlines():
            password = line.strip('\n')
            try:
                # print(f'Trying password: {password}')
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