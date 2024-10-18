from typing import Generator
import string
from loguru import logger
import re

# TODO: add edge case handing for file input

filepath = "test_file3.txt"


def isValidToken(token: str) -> bool:
    logger.info(f"Processing token: {token}")
    
    # apostrophe handling
    token = token.replace("'", "")

    # URL handling
    if "http" in token or "www" in token:
        url_parts = re.split(r'[/:.?=&]', token)  # split by /, :, ., ?, =, and &
        cleaned_parts = []
        for part in url_parts:
            # Remove punctuation and only keep parts with more than 1 character
            cleaned_part = ''.join(char for char in part if char.isalnum())
            if len(cleaned_part) > 2:  # Ensure the part has more than 1 character
                cleaned_parts.append(cleaned_part)
        return cleaned_parts

    if '-' in token:
        hyphenated_parts = token.split('-')
        # Filter valid alphanumeric parts with more than 1 character
        cleaned_parts = [''.join(char for char in part if char.isalnum()) for part in hyphenated_parts if len(part) > 2]
        if cleaned_parts:
            logger.info(f"Valid hyphenated token parts: {cleaned_parts}")
            return cleaned_parts

    cleaned_token = ''.join(char for char in token if char.isalnum())
    
    if cleaned_token.isascii() and cleaned_token.isalnum() and len(cleaned_token) > 2:
        logger.info(f"Valid token: {cleaned_token}")
        return cleaned_token
    else:
        logger.info(f"Invalid or non-ASCII/alphanumeric token: {cleaned_token}")
        return ""


def tokenize(filepath: str) -> Generator[str, None, None]:
    tokens = []
    try:
        with open(filepath, 'r') as f:
            logger.info("successfully opened file")
            
            lines = f.readlines()
            print(lines)

            # split lines
            for line in lines:
                logger.info(f"Processing line: {line.strip()}")
                
                words = line.split()
                logger.info(f"Words in line: {words}")

                # split words
                for word in words:
                    word = word.lower()
                    logger.info(f"Word before validation: {word}")

                    # if valid token, append to list
                    cleaned_tokens = isValidToken(word)

                    if isinstance(cleaned_tokens, list):  # If it's a list (URL or hyphenated word)
                        for token in cleaned_tokens:
                            yield token
                    elif cleaned_tokens:  # Single valid token
                        yield cleaned_tokens

    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    
    return tokens


def computeWordFrequencies(tokens: Generator[str, None, None]) -> dict:
    frequencyMap = {}

    for token in tokens:
        if token in frequencyMap:
            frequencyMap[token] += 1
        else:
            frequencyMap[token] = 1
    
    return frequencyMap


def printFrequencies(frequencies: dict) -> None:
    sorted_count = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    for token, count in sorted_count:
        print(f"{token} - {count}")



if __name__ == "__main__":
    tokenized_file = tokenize(filepath)
    count = computeWordFrequencies(tokenized_file)
    print(tokenized_file)
    print(count)
    printFrequencies(count)
    print(tokenized_file)
