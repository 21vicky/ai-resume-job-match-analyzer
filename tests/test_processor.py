
from text_processor import clean_text, tokenize_text

sample_text = """
I HAVE EXPERIENCE IN Python, SQL,
React.js and Machine Learning!!!
"""

print("Original Text:")
print(sample_text)

cleaned = clean_text(sample_text)

print("\nCleaned Text:")
print(cleaned)

tokens = tokenize_text(cleaned)

print("\nTokenized Words:")
print(tokens)
