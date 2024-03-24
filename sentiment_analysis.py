import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Initializing spaCy with the English model and adding TextBlob for sentiment analysis.
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Function to analyze sentiment of a given text. 
# Utilizes spaCy's NLP capabilities and TextBlob's sentiment polarity.
def analyze_sentiment(review_text):
    doc = nlp(review_text)
    return doc._.blob.polarity

# Loading a subset of the dataset for initial testing. 
# This helps in quicker testing and debugging.
data = pd.read_csv('amazon_product_reviews.csv', low_memory=False, nrows=1000)

# Preprocessing the data:
# - Converting review text data to string type.
# - Dropping rows where review text is missing to ensure data quality.
data['reviews.text'] = data['reviews.text'].astype(str)
data_clean = data.dropna(subset=['reviews.text'])

# Applying the sentiment analysis function to the preprocessed review texts.
# This will add a new column 'sentiment_score' with the sentiment score for each review.
data_clean['sentiment_score'] = data_clean['reviews.text'].apply(analyze_sentiment)

# Optionally, saving the processed data with sentiment scores to a new CSV file.
# This can be used for further analysis or reporting.
data_clean.to_csv('sentiment_analysis_output.csv', index=False)

# Testing the script with a sample review from the dataset.
# This helps in quickly verifying the functioning of the sentiment analysis.
sample_review = data_clean['reviews.text'].iloc[0]
print(f"Sample Review: {sample_review}")
print(f"Sentiment Score: {analyze_sentiment(sample_review)}")
