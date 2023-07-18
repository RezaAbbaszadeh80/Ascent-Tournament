from hashlib import sha256
import subprocess
import os


# Define colors ansi escape codes GLOBALY
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PINK = "\033[95m"
RESET = "\033[0;0m"


def main(file_name):

    # Store all outputs
    outputs = list()

    python_runner_commands = {
        'posix': 'python3',
        'nt': 'py',
    }

    try:
        test_files_directory = './input_files/final'
        test_files = list()
        for test_file in os.listdir(test_files_directory):
            if test_file.startswith('test_') and test_file.endswith('.txt'):
                test_files.append(os.path.join(test_files_directory, test_file))
        test_files.sort()
    except FileNotFoundError:
        # test_files directory must be at the same dir as this file
        print(RED + 'Make sure the directory "test_files/final" exists' + RESET)
        exit(1)

    print('Testing process started...', end='\n\n')
    for test_file in test_files:
        print(YELLOW + test_file + RESET)

        # Just handle any unplanned situation
        try:
            # Read in the input from a file
            with open(test_file) as reader:
                inputs = reader.read()

            # Run the code using subprocess
            process = subprocess.Popen([python_runner_commands[os.name], file_name], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            output, error = process.communicate(inputs.encode())

            # Compare the output to the expected output
            outputs.append(sha256(output.decode().strip().encode()).hexdigest())
            print(GREEN + 'Done!\n' + RESET)

        except:
            ...
    return outputs


if __name__ == '__main__':

    while True:
        file_name = input('Enter your python file: ')
        if os.path.exists(file_name):
            break
        print(RED + 'This file does not exist' + RESET, end='\n\n')

    outputs = main(file_name)

    with open('results.txt', 'w') as writer:
        writer.write('\n'.join(outputs))