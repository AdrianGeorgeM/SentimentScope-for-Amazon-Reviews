# SentimentScope for Amazon Reviews 🌟

## Introduction 📘
Welcome to "SentimentScope for Amazon Reviews"! This project harnesses the power of Natural Language Processing (NLP) to analyze sentiments in Amazon product reviews. It uses Python libraries like `spaCy` and `TextBlob` to understand customer emotions, categorizing them as positive, negative, or neutral.

## Features 🛠
- **Sentiment Analysis**: Analyzes sentiments expressed in Amazon product reviews.
- **NLP with spaCy**: Employs `spaCy` for efficient language processing.
- **Sentiment Polarity with TextBlob**: Integrates `TextBlob` to compute sentiment polarity.
- **Large Dataset Processing**: Capable of handling extensive datasets effectively.

## Installation 💻
To get started with this project, clone the repository and install the required packages:

```bash
git clone https://github.com/AdrianGeorgeM/SentimentScope-for-Amazon-Reviews.git
cd SentimentScope-for-Amazon-Reviews
pip install -r requirements.txt
```

## How to Use 🔍
Run the sentiment analysis with the following command:

```python
python sentiment_analysis.py
```

## Data 📈
The script processes `amazon_product_reviews.csv`, which contains an array of product reviews, focusing particularly on the `reviews.text` field for sentiment analysis. Note: The dataset is not included in this repository due to privacy and size considerations.

## Output 📊
The output is a CSV file named `sentiment_analysis_output.csv`, containing the original reviews and their respective sentiment scores.

## Contributing 🤝
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. Feel free to fork the project, submit pull requests, or send suggestions to enhance the functionality or efficiency.

## License 📜
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 💐
- Heartfelt thanks to the creators of `spaCy` and `TextBlob` for their outstanding work in NLP.
- Inspired by the collaborative spirit of the Python open-source community.

