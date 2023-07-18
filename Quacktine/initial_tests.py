import subprocess
import os


# Define colors ansi escape codes GLOBALY
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PINK = "\033[95m"
RESET = "\033[0;0m"


def main(file_name):

    # Test result related variables
    passed_tests = int()
    failed_tests = int()

    python_runner_commands = {
        'posix': 'python3',
        'nt': 'py',
    }

    try:
        test_files_directory = './input_files/initial'
        test_files = list()
        for test_file in os.listdir(test_files_directory):
            if test_file.startswith('test_') and test_file.endswith('.txt'):
                test_files.append(os.path.join(test_files_directory, test_file))
        test_files.sort()
    except FileNotFoundError:
        # test_files directory must be at the same dir as this file
        print(RED + 'Make sure the directory "test_files/initial" exists' + RESET)
        exit(1)

    print('Testing process started...', end='\n\n')
    for test_file in test_files:

        # Just handle any unplanned situation
        try:
            # Read in the input from a file
            with open(test_file) as reader:
                expceted_answer = reader.readline().strip()
                inputs = ''.join(reader.readlines())

            # Run the code using subprocess
            process = subprocess.Popen([python_runner_commands[os.name], file_name], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            output, error = process.communicate(inputs.encode())

            # Compare the output to the expected output
            output = output.decode().strip()

            print(YELLOW + f'Your output: {output}' + RESET)
            print(PINK + f'Expected output: {expceted_answer}' + RESET)

            if output.strip() == expceted_answer:
                passed_tests += 1
                print(GREEN + 'Test passed!' + RESET)
            else:
                failed_tests += 1
                print(RED + 'Test failed.' + RESET)
            print('-------', end='\n\n')
        except:
            ...
    return passed_tests, failed_tests


if __name__ == '__main__':

    while True:
        file_name = input('Enter your python file: ')
        if os.path.exists(file_name):
            break
        print(RED + 'This file does not exist' + RESET, end='\n\n')

    passed_tests, failed_tests = main(file_name)

    score_in_percentage = (100 * passed_tests) / (passed_tests + failed_tests)
    score_in_percentage = round(score_in_percentage, 2)

    print(f'Your score: {score_in_percentage}%')