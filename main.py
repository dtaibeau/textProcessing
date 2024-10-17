from typing import List
import string
from loguru import logger
import re


filepath = "test_file2.txt"

def isValidToken(token: str) -> bool:
    logger.info(f"Processing token: {token}")
    
    # apostrophes and hyphens treated as empty str
    token = token.replace("'", "").replace("-", "")

    if "http" in token or "www" in token:
        url_parts = re.split(r'[/:.?=&]', token)  # split by /, :, ., ?, =, and &
        cleaned_parts = []
        for part in url_parts:
            # rm punctuation from each part or url
            cleaned_part = ''.join(char for char in part if char.isalnum())
            if cleaned_part: 
                cleaned_parts.append(cleaned_part)
        return cleaned_parts

    cleaned_token = ''.join(char for char in token if char.isalnum())
    
    if cleaned_token.isdigit():
        return cleaned_token
    
    # validate
    if len(cleaned_token) > 3:
        return cleaned_token
    else:
        logger.info(f"Invalid token (either too short or empty): {cleaned_token}")
        return ""


def tokenize(filepath: str) -> List[str]:
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
                    cleaned_token = isValidToken(word)

                    if cleaned_token:
                        tokens.append(cleaned_token)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    
    return tokens


if __name__ == "__main__":
    tokenized_file = tokenize(filepath)
    print(tokenized_file)