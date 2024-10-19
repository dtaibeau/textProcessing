from typing import Generator
import mimetypes
import re
import sys

# TODO: add edge case handing for file input

def isValidToken(token: str) -> bool:
    """
    Function Definition:
    Validates and processes a token, handling apostrophes, URLs, and hyphenated words.
    Returns cleaned tokens or token parts if valid; otherwise, it returns an empty string.

    Time Complexity:
    - Best Case: O(M), where M is the length of the token (for processing the string and removing punctuation).
    - Worst Case: O(M), where M is the length of the token (for handling more complex cases like URLs and hyphenated words).
    - Overall: O(M) since it iterates through the token or its parts a constant number of times.
    """
    # bad input handling 
    if not isinstance(token, str):
        return None
    
    if token == '_':
        return None
    
    # apostrophe handling
    token = token.replace("'", "")

    # URL handling: split by /, :, ., ?, =, and &
    if "http" in token or "www" in token:
        url_parts = re.split(r'[/:.?=&]', token)
        cleaned_parts = [''.join(char for char in part if char.isalnum()) for part in url_parts if part]
        return cleaned_parts if cleaned_parts else None

    # hyphen handling: split hyphenated words, clean each part to retain only alphanumeric chars
    if '-' in token:
        hyphenated_parts = token.split('-')
        cleaned_parts = [''.join(char for char in part if char.isalnum()) for part in hyphenated_parts if part]
        return cleaned_parts if cleaned_parts else None
    
    # natch word characters excluding standalone underscores as tokens
    potential_words = re.findall(r'\b(?!_+\b)\w+\b', token)
    if len(potential_words) >= 1:
        return potential_words

    # cleaned token handling
    cleaned_token = ''.join(char for char in token if char.isalnum())
    
    return cleaned_token if cleaned_token else None


def tokenize(filepath: str) -> Generator[str, None, None]:
    """
    Function Definition:
    Reads a file line by line, splits each line into words, validates each word using `isValidToken`, and yields valid tokens.

    Time Complexity:
    - Best Case: O(N * M), where N is the number of lines in the file, and M is the average number of words per line.
    - Worst Case: O(N * M * L), where L is the length of each word (due to the validation process in `isValidToken`).
    - Overall: O(N * M * L) since proportional to the size of the file, as each word in the file is processed.
    """

    try:
        with open(filepath, 'r') as f:
            # iterate over lines in the file
            for line in f:
                # split each line into words
                words = line.split()
                
                # iterate over words in line
                for word in words:
                    # convert to lowercase for uniformity and check if valid
                    cleaned_tokens = isValidToken(word.lower())
                    
                    if isinstance(cleaned_tokens, list):  # if it's a list (URL or hyphenated word)
                        for token in cleaned_tokens:
                            yield token
                    elif cleaned_tokens:  # single valid token
                        yield cleaned_tokens
    # file handling 
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    except PermissionError:
        print(f"Error: Permission denied for file {filepath}.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


def computeWordFrequencies(tokens: Generator[str, None, None]) -> dict:
    """
    Function Definition:
    Computes the frequency of each token in the given generator of tokens.

    Time Complexity:
    - Best Case: O(T), where T is the number of tokens (assuming most tokens are already present in the dictionary).
    - Worst Case: O(T), where T is the number of tokens (as each token insertion and lookup in the dictionary takes constant time).
    - Overall: O(T) since each token is processed once.
    """
    # initialize empty token-count dictionary
    frequencyMap = {}

    # iterated through each token in generator
    for token in tokens:
        # if token already in dict, increment count by 1
        if token in frequencyMap:
            frequencyMap[token] += 1
        # if not present, add it with count of 1
        else:
            frequencyMap[token] = 1
    
    return frequencyMap


def printFrequencies(frequencies: dict) -> None:
    """
    Function Definition:
    Sorts and prints the frequency map, showing tokens in alphabetical, descending order of frequency.

    Time Complexity:
    - Sorting: O(U log U), where U is the number of unique tokens.
    - Printing: O(U), where U is the number of unique tokens.
    - Overall: O(U log U) due to the sorting step.
    """
    # sort dict items by frequency in descending, alphabetical order 
    # (-item[1]) = descending order
    # (item[0]) = alphabetical order
    sorted_count = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))

    # iterate through sorted list of tuples, print each token with its frequency
    for token, count in sorted_count:
        print(f"{token} - {count}")



if __name__ == "__main__":
    # check if correct num args (should be 2)
    if len(sys.argv) != 2:
        # redirect user to correct usage info if not provided
        print("Usage: python PartA.py <filename>")
        sys.exit(1)

    # retrieve filepath
    filepath = sys.argv[1]

    # generate tokens
    tokenized_file = tokenize(filepath)

    # compute frequency
    count = computeWordFrequencies(tokenized_file)

    # print sorted frequencies of tokens
    printFrequencies(count)
