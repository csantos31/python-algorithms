def main(): 
    word = input('\n\tType the word you want to check if is palindrome or not \n\tR: ')
    result = check_if_is_palindrome(sanitize_string(word))
    if(result):
        print(f'The word {word} is palindrome')
    else:
        print(f'The word {word} is NOT palindrome')

def sanitize_string(input):
    return (''.join(e for e in input if e.isalnum())).lower()

def check_if_is_palindrome(word):
    middle_len = len(word) // 2
    is_equal = True

    for i in range(middle_len):
        if(word[i] != word[len(word)-i-1]):
            is_equal = False

    return is_equal


main()

