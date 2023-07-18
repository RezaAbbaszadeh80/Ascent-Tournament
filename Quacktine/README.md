# Quacktine

quacktine.py is a project developed for the cs50x_iran tournament ascent 1. The program builds a wall to quarantine infected ducks by separating them from healthy ducks.

## Installation

To run this program, you have two options:

1. Online Codespace:
   - Visit the GitHub repository for the project: [https://github.com/RezaAbbaszadeh80/Ascent-Tournament](https://github.com/RezaAbbaszadeh80/Ascent-Tournament)
   - Click on the "Code" button and select "Open with Codespaces" to run the program online. No installation is required in this case.

2. Local System:
   - Ensure that Python is installed on your local system and added to the PATH.
   - Install an IDE like Visual Studio Code.
   - Create an empty folder on your system and open it in Visual Studio Code.
   - Open the terminal in Visual Studio Code.
   - Clone the repository by running the following command: `git clone https://github.com/RezaAbbaszadeh80/Ascent.git`
   - Change to the project directory: `cd Quacktine`
   - Open the `RPL_quacktine.py` file in Visual Studio Code using the command: `code RPL_quacktine.py`
   - Finally, run the program by executing the command: `python RPL_quacktine.py`

## Usage

To use this program, follow the steps below:

1. Method 1 (Online Codespace):
   - Go to the GitHub repository: [https://github.com/RezaAbbaszadeh80/Ascent-Tournament](https://github.com/RezaAbbaszadeh80/Ascent-Tournament)
   - Click on the green "Code" button and select "Open with Codespaces".
   - In the Codespace, open the terminal and run `python quacktine.py`.
   - Provide the required inputs in the format:\
     `4 8`\
     `0 1 0 0 0 0 1 1`\
     `0 1 0 0 0 0 1 1`\
     `0 0 0 0 0 0 1 1`\
     `0 0 0 0 0 0 0 1`

2. Method 2 (Local System):
   - Ensure Python is installed on your local system and added to the PATH.
   - Open the project folder in Visual Studio Code.
   - Open the terminal in Visual Studio Code and run `python RPL_quacktine.py`.
   - Provide the required inputs in the terminal in the same format as mentioned above.

## Project Description

The program takes inputs representing an `n` by `m` table. The first line contains `n` and `m`, which indicate the number of rows and columns of the table, respectively. In the next `n` lines, you are given `m` space-separated values, which can be either 0 or 1. A value of 1 represents an infected duck, while a value of 0 represents a healthy duck. 

The goal of the program is to quarantine the infected ducks by building a wall between the healthy ducks (0) and infected ducks (1).

## Features

The program consists of the following features:

- **Main Functionality**: The main function prompts the user to enter the values of `n` and `m` to create a matrix of size `n` by `m`. It then calls the `create_matrix()` function to generate a transpose matrix. The program then counts the number of times the values change from 0 to 1 or vice versa in both the original and transposed matrices. This count corresponds to the number of walls required to quarantine the infected ducks.

- **Example Execution**: The README provides example inputs and their corresponding outputs to showcase how the program works.

## Example

For the input:
```
4 8
0 1 0 0 0 0 1 1
0 1 0 0 0 0 1 1
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 1
```
The expected output is:
```
The number of walls required to quarantine the infected ducks is: 10
```

For the input:
```
3 3
1 1 1
1 0 1
1 1 1
```
The expected output is:
```
The number of walls required to quarantine the infected ducks is: 4
```

## Future Developments

For future developments, the following enhancements could be considered:

- **Input Validation**: Validate the input to ensure it contains only valid values (0 and 1) and handle invalid inputs gracefully.
- **User-Friendly Input**: Include additional prompts or comments to guide the user while providing inputs.
- **Graphical Output**: Visualize the walls graphically to show their placement on the table for better user understanding.

These enhancements would further improve the usability and functionality of the program. However, the current version is designed to comply with the requirements of the cs50x_iran tournament structure.

## collaborators

- **Reza Abbaszadeh**: https://github.com/RezaAbbaszadeh80
- **Elham Hosseini**: https://github.com/EliFaveen
