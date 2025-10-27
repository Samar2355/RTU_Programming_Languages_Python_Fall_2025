"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    return sum(1 for c in text if not c.isspace())

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for token in text.split():
        cleaned = token.strip('.,:;!?"()[]{}')
        if not cleaned:
            continue
        try:
            number = int(cleaned)
            numbers.append(number)
        except ValueError:
            continue
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    nums = extract_numbers(text)
    total = sum(nums)
    average = total / len(nums) if nums else 0
    char_count = count_characters(text)
    word_count = count_words(text)
    return (char_count, word_count, total, average)

if __name__ == "__main__":
    text = input("Enter a text: ")
    char_count, word_count, total, average = analyze_text(text)
    print(f"Characters (non-space): {char_count}")
    print(f"Words: {word_count}")
    print(f"Numbers sum: {total}")
    print(f"Numbers average: {average:.2f}")
    # TODO: read input, call analyze_text(), and print results
    pass
