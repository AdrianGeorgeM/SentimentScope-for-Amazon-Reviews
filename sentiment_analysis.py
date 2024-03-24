# Step 1: Import necessary libraries
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Add SpacyTextBlob to the pipeline
nlp.add_pipe('spacytextblob')


# Step 3: Define the sentiment analysis function
def analyze_sentiment(review_text):
    doc = nlp(review_text)
    return doc._.blob.polarity

# Step 4: Load the dataset
data = pd.read_csv('amazon_reviews.csv')

# Step 5: Preprocess the data
# Selecting 'review.text' column and dropping missing values
reviews_data = data['review.text'].dropna()

# Step 6: Apply sentiment analysis on each review and store results
data['sentiment_score'] = reviews_data.apply(analyze_sentiment)

# Step 7: Testing with a sample review
sample_review = reviews_data.iloc[0]
print(f"Sample Review: {sample_review}")
print(f"Sentiment Score: {analyze_sentiment(sample_review)}")

# Step 8: Save the results to a new CSV file
data.to_csv('amazon_reviews_sentiment_scores.csv', index=False)
