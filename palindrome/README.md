# Palindrome Checker

This repository contains a simple Python script to check whether a given word or phrase is a palindrome.

## Description

A palindrome is a word or phrase that reads the same backward as forward, ignoring case, spaces, and punctuation. This script takes user input and determines if the entered text is a palindrome.

## Code Structure

- **main()**: The main function that prompts the user to input a word or phrase and displays whether it is a palindrome.
- **sanitize_string(input)**: A function that removes all non-alphanumeric characters from the input and converts it to lowercase.
- **check_if_is_palindrome(word)**: This function checks if the sanitized text is a palindrome by comparing characters from the beginning and the end of the string.

## Expected Output

Here is an example interaction with the script:

```bash
	Type the word you want to check if is palindrome or not 
	R: A man, a plan, a canal, Panama
The word A man, a plan, a canal, Panama is palindrome
```

or for a non-palindrome:

```bash
	Type the word you want to check if is palindrome or not 
	R: hello
The word hello is NOT palindrome
```

## How to Run

1. Ensure you have [Python](https://www.python.org/downloads/) installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/csantos31/python-algorithms.git
   cd palindrome
   ```
3. Execute the script:
   ```bash
   python3 main.py
   ```

## Logic Explanation

The script checks if a text is a palindrome by:

1. Sanitizing the input to remove spaces, punctuation, and make it case-insensitive.
2. Calculating the middle length of the sanitized text.
3. Comparing each character from the start with its corresponding character from the end.
4. Returning `True` if all pairs match, otherwise `False`.

## Possible Improvements

- Handle edge cases such as empty input gracefully.
- Include automated tests.
- Enhance the user interface for better UX.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with suggestions for improvements.