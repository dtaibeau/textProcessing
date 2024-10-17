from typing import List
import string
from loguru import logger

filepath = "test_file1.txt"

def isValidToken(token: str) -> bool:
    logger.info(f"Processing token: {token}")
    # apostrophes treated as empty str
    token = token.replace("'", "")

    # hyphens treated as empty str to append second word to first
    token = token.replace("-", "")

    if token.isalnum() and len(token) > 3:
        logger.info(f"Valid token: {token}")
        return token
    else:
        logger.info(f"Invalid token: {token}")
        return ""


def tokenize(filepath: str) -> List[str]:
    tokens = []

    try:
        with open (filepath, 'r') as f:
            logger.info("successfully opened file")
            logger.info(f"File content:\n{f.read()}")

            # split lines
            for line in f:
                logger.info(f"Processing line: {line.strip()}")
                if not line.strip():
                    logger.info("Empty line found, skipping.")
                    continue
                
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
    
    logger.info(f"Final tokens: {tokens}")
    return tokens

if __name__ == "__main__":
    tokenized_file = tokenize(filepath="test_file1.txt")
    print(tokenized_file)


    