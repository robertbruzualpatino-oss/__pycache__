# This module provides utilities for password management.
"""
Author: Robert Bruzual

Purpose: Password management utilities.
Creative addition:

"""

import string
import os

# define constants for special characters (as they aren't built-in like the others).
SPECIAL_CHARS = string.punctuation

if not os.path.exists('wordlist.txt'):
    with open('wordlist.txt', 'w') as f:
        f.write("password\n")
        f.write("123456\n")
        f.write("qwerty\n")
        
# Helper function to check if a word exists in a file.       
def word_in_file(word, filename, case_sensitive=False):
    """
    Checks if a word exists in a given file.
    
    Args:
        word (str): The word to search for.
        filename (str): The path to the file.
        case_sensitive (bool): Whether the search should be case_sensitive.
        
    Returns:
        bool: True if the word is found, False otherwise.
    """
    try:
        with open(filename, 'r') as f:
            for line in f:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    return False


# Helper function to check if a word contains at least one character from a list.
def word_has_character(word, character_list):
    """
    Checks if a word contains at least one character from a given list.
    
    Args:
        word (str): The word to check.
        character_list (list): A list of characters to check against.
        
    returns:
        bool: True if the word contains at least one chracter from the list, False otherwise.
    """
    for char in word:
        if char in character_list:
            return True
    return False


# Helper function to calculate word complexity.
def word_complexity(word):
    """
    Calculates the complexity of a word based on character types.
    
    Args:
        word (str): The word to evaluate.
        
    Returns:
        int: A Complexity score (0-4).
    """
    
    complexity_score = 0
    if word_has_character(word, string.ascii_lowercase):
        complexity_score += 1
    if word_has_character(word, string.ascii_uppercase):
        complexity_score += 1
    if word_has_character(word, string.digits):
        complexity_score += 1
    if word_has_character(word, SPECIAL_CHARS):
        complexity_score += 1
    return complexity_score
    
# Helper function to calculate password strength.
def password_strength(password, min_length=10, strong_length=15):

    """
    Evaluates the strength of a password.
    
    Args:
        password (str): The password to evaluate.
        min_length (int): Minimum length for a password to be considered weak.
        strong_length (int): Length for a password to be considered strong.
        
    Returns:
        str: "Weak", "Moderate", or "Strong" based on the evaluation.
    """
    strength = 0
    
    # Check length.
    if len(password) >= strong_length:
        print(f"Password length {len(password)} is strong.")
        strength += 2
    elif len(password) >= min_length:
        print(f"Password length {len(password)} is moderate.")
        strength += 1
    else:
        print(f"Password length {len(password)} is weak.") # Too short.
    
    # Check dictionary/known-passwords (using wordlist.txt as a stand-in).
    if word_in_file(password, 'wordlist.txt'):
        print("Warning: Password found in known passwords list.")
        strength = max(0, strength - 1) # Penalize if found in known passwords.
    else:
        print("Password not found in known passwords list.")
        strength = min(5, strength + 1) # Reward if not found.
        
    # Check complexity.
    complexity_score = word_complexity(password)
    print(f"Password complexity score: {complexity_score}/4")
    strength = min(5, strength + (complexity_score // 2)) # Add complexity score divided by 2.
    
    # Determine final strength category.
    if strength >= 4:
        print("Password strength: Strong")
    elif strength >= 2:
        print("Password strength: Moderate")
    else:
        print("Password strength: Weak")
        
    return min(5, max(0, strength))


# Helper function to run some test cases.
def main():
    """
    Runs test cases for password strength evaluation.
    
    Returns:
        None
    """
    while True:
        password = input("Enter a password to evaluate (or 'quit' to exit): ")  
        if password.lower() == 'quit':
            break
        test_passwords = [
            "password",
            "P@ssw0rd123",
            "123456",
            "StrongPass!2024",
        ] 
        
        strength_score = password_strength(password)
        print(f"Final strength score: {strength_score}\n")
        
        
        
if __name__ == "__main__":
    main()
# End of passwords.py module.   