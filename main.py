import zipfile
import time
import itertools

# Define the seed to include in the combinations
#seed = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
seed = '0123456789'

# Define the maximum length of combinations
max_length = 10

def generate_combinations(length):
    for combination in itertools.product(seed, repeat=length):
        yield ''.join(combination)

zip_file_path = 'archive2.zip'

start_time = time.time()  # Record the start time
is_found = False

for password in generate_combinations(5):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(pwd=password.encode())
        print(f'Success! Password found: {password}')
        is_found = True
        break  # Exit the loop if the correct password is found
    except Exception as e:
        #print(f'Failed with password: {password}')
        pass

if is_found == False:
    print('Sorry I did not find the password')


end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time  # Calculate the elapsed time

print(f'Total time: {elapsed_time} seconds')