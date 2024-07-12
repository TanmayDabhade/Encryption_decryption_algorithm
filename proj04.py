#Algorithm
#1. Printing the Banner with Intro Message
#2. Ask the user for a rotation(integer), if it is not an integer, print an error message and reprompt for a new rotation
#3. Ask the user for a command(e, d, q) for the intended operation
#4. If the command is e, ask the user for a string to encrypt
#5. If the command is d, ask the user for a string to decrypt
#6. If the command is q, quit the program
#7. If the command is not e, d, or q, print an error message and reprompt for new command
#8. If the string to encrypt or decrypt contains a space, print an error message
#9. If the string to encrypt or decrypt contains a character that is not alphanumeric or punctuation, print an error message
#10 Iterate through all the characters of the string and encrypt using the affine cipher and caesar cipher depending on
#   whether the character is alphanumeric or punctuation
#11. Print the encrypted or the decrypted string with the plain string.
#12. Reprompt for a new command
#13. If the command is q, quit the program
#M - the length of the alphabet
#A - the smallest co-prime number of M
#B - the index of the character in the alphabet
#C - the index of the encrypted character in the alphabet
#D - the index of the decrypted character in the alphabet
#N - the rotation value
#ch - the character in the string
#text - the string to be encrypted or decrypted
#cipher_text - the encrypted string
#decipher_text - the decrypted string
#alphabet - the string containing the alphabet
#alpha - the string containing the alphanumeric characters
#punctuation - the string containing the punctuation characters
#text1 - the string to be encrypted or decrypted
#text - lowered in text1
#i - the index of the character in the string

# Import the string and math modules
import math
import string

# Define constants for punctuation and alphanumeric characters
#  string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
#  except space is not included in this string
PUNCTUATION = string.punctuation
#  string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
#  string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits

BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''

def print_banner(message):
    '''Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()

def multiplicative_inverse(A, M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.
        Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
        Returns:
            int: The multiplicative inverse of A modulo M.
    '''

    for x in range(M):
        if (A * x) % M == 1:
            return x


def check_co_prime(num, M):
    '''Checking co-prime using the GCD function from the math module return true or false based on the condition'''
    if math.gcd(num, M) == 1 and num != M:
        return True
    else:
        return False
def get_smallest_co_prime(M):
    '''Checking for the smallest co-prime number using the check_co_prime function'''
    for num in range(2, M):
        if check_co_prime(num, M):
            return num
    return False

        # delete and replace with your code


def caesar_cipher_encryption(ch, N, alphabet):
    '''Using this function to encrypt the string using the caesar cipher this function returns the encrypted string
    This function only works if the character in the string is a punctuation.
    The character is selected by enumerating the string and then checking if the character is a punctuation or not.'''
    M = len(alphabet)
    B = alphabet.find(ch)
    C = (B + N) % M
    return alphabet[C]
     # delete and replace with your code


def caesar_cipher_decryption(ch, N, alphabet):
    '''Using this function to decrypt the string using the caesar cipher this function returns the decrypted string
    This function only works if the character in the string is a punctuation.
    The character is selected by enumerating the string and then checking if the character is a punctuation or not.'''
    M = len(alphabet)
    B = alphabet.find(ch)
    D =  (B - N) % M
    return alphabet[D]


def affine_cipher_encryption(ch, N, alphabet):
    '''Using this function to encrypt the string using the affine cipher this function returns the encrypted string
    This function only works if the character in the string is an alphanumeric.
    The character is selected by enumerating the string and then checking if the character is an alphanumeric or not.'''
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    B = alphabet.find(ch)
    C = ((A * B) + N) % M
    return alphabet[C]


def affine_cipher_decryption(ch, N, alphabet):
    '''Using this function to decrypt the string using the affine cipher this function returns the decrypted string
    This function only works if the character in the string is an alphanumeric.
    The character is selected by enumerating the string and then checking if the character is an alphanumeric or not.'''
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    B = alphabet.find(ch)
    C = multiplicative_inverse(A, M)
    D = (C * (B - N)) % M
    return alphabet[D]


def main():
    '''This is the main function where the program starts executing
    This function calls all the other functions and prints the banner and the encrypted or decrypted string
    This function also checks for the errors and prints the error message if the string contains a space or a character
    that is not alphanumeric or punctuation'''
    print_banner(BANNER)
    N = input("Input a rotation (int): ")
    while N.isalpha() == True:
        print("\nError; rotation must be an integer.")
        N = input("Input a rotation (int): ")
    else:
        while N.isdigit() == False:
            print("\nError; rotation must be an integer.")
            N = input("Input a rotation (int): ")
        else:
            N = int(N)
            command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            command = command.lower()
            while command != "q":
                if command == "e":
                    alpha = ''
                    a = ''
                    punctuation = ''
                    c = ''
                    cipher_text = ''
                    text1 = input("\nInput a string to encrypt: ")
                    text = text1.lower()
                    for i, ch in enumerate(text):
                        if text[i].isalnum() == True:
                            alphabet = ALPHA_NUM
                            a = affine_cipher_encryption(ch, N, alphabet)
                            cipher_text += a
                        elif text[i].isalnum() == False and text[i].isspace() == False:
                            alphabet = PUNCTUATION
                            c = caesar_cipher_encryption(ch, N, alphabet)
                            cipher_text += c
                        elif text[i].isspace() == True:
                            print("\nError with character:", ch)
                            print("Cannot encrypt this string.")
                            break
                    if text[i].isspace() == False:
                        print("\nPlain text:", text1)
                        print("\nCipher text:", cipher_text)



                    command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")


                elif command == "d":
                    alpha = ''
                    a = ''
                    punctuation = ''
                    c = ''
                    decipher_text = ''
                    text1 = input("\nInput a string to decrypt: ")
                    text = text1.lower()
                    for i, ch in enumerate(text):
                        if text[i].isalnum() == True:
                            alphabet = ALPHA_NUM
                            a = affine_cipher_decryption(ch, N, alphabet)
                            decipher_text += a
                        elif text[i].isalnum() == False:
                            alphabet = PUNCTUATION
                            c = caesar_cipher_decryption(ch, N, alphabet)
                            decipher_text += c
                        elif text[i] == ' ':
                            print("\nError with character:", ch)
                            print("Cannot encrypt this string.")
                    print("\nCipher text:", text1)
                    print("\nPlain text:", decipher_text)
                    command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
                elif command == "q":
                    break
                else:
                    print("\nCommand not recognized.")
                    command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
     # delete and replace with your code




# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()


