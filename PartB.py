from PartA import tokenize
import sys

def findCommonTokens(text_file1, text_file2):
    """
    Function Definition:
    Finds common tokens between two files by creating a set of tokens from the first file and checking tokens from the second file against it.

    Time Complexity:
    - Creating the set from the first file: O(T1), where T1 is the number of tokens in the first file.
    - Iterating through the second file and checking for common tokens: O(T2), where T2 is the number of tokens in the second file.
    - Overall: O(T1 + T2), since both files are processed independently.
    """
    # tokenize first file, create set of tokens for faster lookup
    tokens_file1 = set(tokenize(text_file1))

    # initialize set to store common tokens
    common_tokens = set() 

    # iterate through tokens in the second file
    for token in tokenize(text_file2):
        # check if token from 2nd file exists in 1st file's set
        if token in tokens_file1:
            common_tokens.add(token)  # add common token to the set if true

    print("Common tokens:", common_tokens)

    return len(common_tokens)



if __name__ == "__main__":
    """
    Overall Time Complexity:
    - Tokenization: O(N * M * L) for processing tokens from both files.
    - Word Frequency Computation: O(N) for building the frequency map.
    - Finding Common Tokens: O(T1 + T2) for comparing tokens.
    - Sorting Frequencies: O(U log U) for sorting the unique tokens.

    The total complexity is: O(N * M * L + T1 + T2 + U log U).
    """
    # exactly 2 command line args should be provdided
    if len(sys.argv) != 3:
        print("Usage: python3 PartB.py file1.txt file2.txt")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # find common tokens
    common_tokens = findCommonTokens(file1, file2)
    
    print(f"Number of common tokens: {common_tokens}")