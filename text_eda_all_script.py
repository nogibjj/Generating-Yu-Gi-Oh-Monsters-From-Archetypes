import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag
from collections import Counter
import warnings

warnings.filterwarnings("ignore")

# Download NLTK resources if not already downloaded
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("vader_lexicon")

def comprehensive_eda(data):
    # Define custom stopwords
    custom_stopwords = set(stopwords.words("english")) | {"1", ".", ","}

    # Function to count meaningful words, excluding stopwords and digits
    def count_meaningful_words(column, stopwords):
        word_count = Counter()
        for text in column:
            words = word_tokenize(text.lower())
            filtered_words = [word for word in words if word not in stopwords and word.isalpha()]
            for word in filtered_words:
                word_count[word] += 1
        return word_count

    # Count meaningful words in 'name' and 'desc' columns
    meaningful_name_word_count = count_meaningful_words(data["name"], custom_stopwords)
    meaningful_desc_word_count = count_meaningful_words(data["desc"], custom_stopwords)

    # Plot top meaningful words in 'name' and 'desc' columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Top meaningful words in 'name'
    top_meaningful_name_words = meaningful_name_word_count.most_common(10)
    names, name_counts = zip(*top_meaningful_name_words)
    ax1.bar(names, name_counts)
    ax1.set_title('Top 10 Meaningful Words in "name" Column')
    ax1.set_ylabel("Frequency")
    ax1.set_xticklabels(names, rotation=45, ha="right")

    # Top meaningful words in 'desc'
    top_meaningful_desc_words = meaningful_desc_word_count.most_common(10)
    descs, desc_counts = zip(*top_meaningful_desc_words)
    ax2.bar(descs, desc_counts)
    ax2.set_title('Top 10 Meaningful Words in "desc" Column')
    ax2.set_ylabel("Frequency")
    ax2.set_xticklabels(descs, rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

    # Function to count meaningful words, excluding manual stopwords and digits
    def count_meaningful_words_manual_stopwords(column):
        manual_stopwords = {
            "the", "of", "and", "a", "to", "in", "is", "you", "that", "it",
            "he", "was", "for", "on", "are", "as", "with", "his", "they", "I",
            "at", "be", "this", "have", "from", "or", "1", ".", ","
        }
        word_count = Counter()
        for text in column:
            words = text.split()
            filtered_words = [word.lower() for word in words if word.lower() not in manual_stopwords and word.isalpha()]
            for word in filtered_words:
                word_count[word] += 1
        return word_count

    # Count meaningful words in 'name' and 'desc' columns with manual stopwords
    meaningful_name_word_count_manual = count_meaningful_words_manual_stopwords(data["name"])
    meaningful_desc_word_count_manual = count_meaningful_words_manual_stopwords(data["desc"])

    # Function to count frequencies of values in a given column
    def count_frequencies(column):
        return column.value_counts()

    # Count frequencies for 'type', 'atk', 'def', 'level', 'race', 'attribute'
    type_frequencies = count_frequencies(data["type"])
    atk_frequencies = count_frequencies(data["atk"])
    def_frequencies = count_frequencies(data["def"])
    level_frequencies = count_frequencies(data["level"])
    race_frequencies = count_frequencies(data["race"])
    attribute_frequencies = count_frequencies(data["attribute"])

    # Plot frequencies
    fig, axes = plt.subplots(3, 2, figsize=(14, 18))
    fig.subplots_adjust(hspace=0.5)

    # Type
    axes[0, 0].bar(type_frequencies.index[:10], type_frequencies.values[:10])
    axes[0, 0].set_title("Top 10 Types")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].tick_params(axis="x", rotation=45)

    # ATK
    axes[0, 1].bar(atk_frequencies.index[:10].astype(str), atk_frequencies.values[:10])
    axes[0, 1].set_title("Top 10 ATK Values")
    axes[0, 1].set_ylabel("Frequency")
    axes[0, 1].tick_params(axis="x", rotation=45)

    # DEF
    axes[1, 0].bar(def_frequencies.index[:10].astype(str), def_frequencies.values[:10])
    axes[1, 0].set_title("Top 10 DEF Values")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].tick_params(axis="x", rotation=45)

    # Level
    axes[1, 1].bar(level_frequencies.index[:10].astype(str), level_frequencies.values[:10])
    axes[1, 1].set_title("Top 10 Levels")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].tick_params(axis="x", rotation=45)

    # Race
    axes[2, 0].bar(race_frequencies.index[:10], race_frequencies.values[:10])
    axes[2, 0].set_title("Top 10 Races")
    axes[2, 0].set_ylabel("Frequency")
    axes[2, 0].tick_params(axis="x", rotation=45)

    # Attribute
    axes[2, 1].bar(attribute_frequencies.index[:10], attribute_frequencies.values[:10])
    axes[2, 1].set_title("Top 10 Attributes")
    axes[2, 1].set_ylabel("Frequency")
    axes[2, 1].tick_params(axis="x", rotation=45)

    plt.show()

    # Apply POS tagging to each description
    def pos_tagging(text):
        tokens = word_tokenize(text.lower())
        return pos_tag(tokens)

    tagged_descriptions = data["desc"].apply(pos_tagging)
    all_tags = [tag for sublist in tagged_descriptions for _, tag in sublist]
    pos_counts = Counter(all_tags)
    top_tags = pos_counts.most_common(10)
    tags, counts = zip(*top_tags)

    plt.figure(figsize=(10, 6))
    plt.bar(tags, counts, color="skyblue")
    plt.title("Top 10 POS Tags in Descriptions")
    plt.xlabel("POS Tags")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

    # Apply sentiment analysis to each description
    sia = SentimentIntensityAnalyzer()
    data["sentiment"] = data["desc"].apply(lambda x: sia.polarity_scores(x)["compound"])

    # Plot the distribution of sentiment scores
    plt.figure(figsize=(10, 6))
    plt.hist(data["sentiment"], bins=50, color="skyblue")
    plt.title("Distribution of Sentiment Scores")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

data = pd.read_csv("C:/Users/wonny/Downloads/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/training_data_final/all_training_cards.csv")
comprehensive_eda(data)
