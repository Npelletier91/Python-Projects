# Assuming you have the following paragraph
paragraph = "Hello, this is an example paragraph because I love to code!"

# Tokenize into words using Python's split() method
word_tokens = paragraph.split()

# Tokenize into words using NLTK
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
word_tokens_nltk = word_tokenize(paragraph)

# Tokenize into characters
char_tokens = [char for char in paragraph]

# Print results
print("Word Tokens (split):", word_tokens)
print("Word Tokens (NLTK):", word_tokens_nltk)
print("Character Tokens:", char_tokens)

from textblob import TextBlob

# Create a TextBlob object
blob = TextBlob(paragraph)

# Get the sentiment
sentiment = blob.sentiment.polarity  # Ranges from -1 to 1

print("Sentiment Score:", sentiment)
