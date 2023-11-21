from collections import Counter 
import matplotlib.pyplot as plt

#CONSTANTS

CIPHER = "KHOHGGCSXOQYSFBCDOWOQFRNKCETFRCEGIQJTUBRGCJUOGDOHGJTZFVYSSHDNWONRPNSCVCHOWUQHRUKQDHIIIZZXHPOOZIQOWFVDPGCGGEVYOCVSVHPPONKVSSNUGPGZOWEHYUKYUUQFOOHFKYUCQVSSVUGPNYFQYHCQWZIMDUEVYVVLFMWJLHMKKYSUQFEKCQMWSIQVSSGLNVMQDAEVYBUEFYWESSXLPYSPHTPBXLPRZCQGLZIQIEVYPCCUCQQQOVDAESHWJZIMDPOGUZKLHUJNLBWHVZGMLPRHBHKCVYDFDWHVRCWAKVWMXDPNSNKGHOPHUMSMLFPHBHOOOHFGOPOWVSSSRWERCGVSSMSCCYFLPRKUYGDWHJNPSUSQPHWRWWRHRVMINEGROSLPDIWKCUCWXPOQIPRLBSLILNYGCYRADBPRVXVWWNWNPHBRWRVNZJLHQHCWHBWJPGBRYECGHJLRVUQFUBWHZFIIVHVYQQYASFQFQBLNTSCQXLQUQVZFCQRPBMLXPAIRFEVYBHWOMKWACHWJLHCQYLFXHAPKBLESWMWJPPFLUDCZVQWWNXFPOHGVSSHPASSUUVHWNKRWSUVWCSZLNWGUQFOOHFGDKCWJEVYGCQTIGKWG"

class bcolors:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

# FUNCTIONS

def compute_letters_frequency(input_string):
   """
    Python Program:
    Using a dictionary to store the char frequency in string
    """
   letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
   input_string = input_string.lower()
   chars_in_string = Counter(input_string)
   res = {}
   for letter in letters:
      if(letter in chars_in_string):
         res[letter] = chars_in_string[letter]
      else: 
         res[letter] = 0 
   return res

def plot_letters_frequency_analysis(input_string):
    freq_list = compute_letters_frequency(input_string).values()
    print(freq_list)
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    fig, ax = plt.subplots()
    ax.bar(x = alphabet, height = freq_list)
    plt.ylabel('Frequency')
    plt.xlabel('Alphabet')


def decrypt_vigenere(sk, ct=CIPHER, spaces_and_punctuation = True):
    """Decrypts a Vigenère cipher by applying the key mod 26

    Args:
        ct (str): the ciphertext
        sk (str): the secret key
        spaces_and_punctuation (bool): whether to keep spaces and punctuation

    Returns:
        str: the plaintext
    """
    decrypted_text = ""
    sk_repeated = (sk * (len(ct) // len(sk))) + sk[:len(ct) % len(sk)]
    for cipher_char, key_char in zip(ct, sk_repeated):
        if cipher_char.isalpha():
            shift = ord(key_char.upper()) - ord('A')
            if cipher_char.islower():
                decrypted_char = chr((ord(cipher_char.upper()) - ord('A') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(cipher_char.upper()) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            if(spaces_and_punctuation):
                decrypted_text += cipher_char
    print(decrypted_text)

def extract_characters(input_string, x, n):
    """Extracts characters from a string
    
    Args:
        input_string (str): the string to extract characters from
        x (int): the starting index
        n (int): the step size

    Returns:
        str: the extracted characters
    """
    result = ""
    for i in range(len(input_string)):
        if (i + 1) % n == x:
            result += input_string[i]
    return result

def find_letters_in_string(msg: str, word: str):
    """Finds the indices of the letters in a string

    Args:
        msg (str): the string to search in
        word (str): the word to search for

    Returns:
        print the indices of the letters in the string
    """
    
    word = word.upper()
    
    if word not in msg:
        print(f"Could not find \"{word}\"")
        return
    
    places = []
    for i in range(len(msg) - len(word) + 1):
        if msg[i:i+len(word)] == word:
            places.append(i)
    
    print(f"Found \"{word}\" at positions {places}")
    print(msg.replace(word, bcolors.YELLOW + bcolors.BOLD + word + bcolors.ENDC))
    
