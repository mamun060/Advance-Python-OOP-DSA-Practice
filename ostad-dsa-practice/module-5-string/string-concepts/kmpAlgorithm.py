# The KMP (Knuth-Morris-Pratt) algorithm is an efficient string-searching algorithm 
# that finds occurrences of a pattern in a text in O(N) time complexity. 
# It avoids unnecessary comparisons by preprocessing the pattern using the LPS 
# (Longest Prefix Suffix) array.

def computeLPS(pattern):
    lps = [0] * len(pattern)  # LPS array initialization
    j = 0  # Pointer for the longest prefix suffix

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:  
            j = lps[j - 1]  # Backtrack to previous LPS value
        
        if pattern[i] == pattern[j]:  
            j += 1
            lps[i] = j  # Store LPS value
    return lps

def KMP_search(text, pattern):
    lps = computeLPS(pattern)  # Preprocess the pattern
    i, j = 0, 0  # i -> text index, j -> pattern index

    while i < len(text):
        if text[i] == pattern[j]:  # Character match
            i += 1
            j += 1

            if j == len(pattern):  # Pattern found
                print(f"Pattern found at index {i - j}")
                j = lps[j - 1]  # Continue searching for more occurrences

        else:  # Mismatch
            if j > 0:
                j = lps[j - 1]  # Use LPS to skip unnecessary comparisons
            else:
                i += 1  # Move to the next character in the text

# Example Test Case
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMP_search(text, pattern)
