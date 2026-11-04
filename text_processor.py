
import re


def clean_text(text):

    # Step 1: Convert text to lowercase
    text = text.lower()

    # Step 2: Remove unnecessary punctuation
    text = re.sub(r'[^\w\s]', ' ', text)

    # Step 3: Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Step 4: Remove spaces at beginning and end
    text = text.strip()

    return text


def tokenize_text(text):

    # Split text into individual words
    words = text.split()

    return words
