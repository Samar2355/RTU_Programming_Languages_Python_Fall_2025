"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    word = len(sentence), len(sentence.split()), "python" in sentence.lower()
    return word
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    pass

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(analyze_sentence(sentence))
    # TODO: read sentence from input, call function, and print results
    pass
