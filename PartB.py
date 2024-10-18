from PartA import tokenize
import sys

def findCommonTokens(text_file1, text_file2):
    tokens_file1 = set(tokenize(text_file1))
    common_token_count = 0
    
    for token in tokenize(text_file2):
        if token in tokens_file1:
            common_token_count += 1
    
    return common_token_count


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 PartB.py file1.txt file2.txt")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    common_tokens = findCommonTokens(file1, file2)
    print(f"Number of common tokens: {common_tokens}")