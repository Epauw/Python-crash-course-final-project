import wordcloud
from matplotlib import pyplot as plt

def generate_wordcloud(filename):
    # List of punctuations and uninteresting words to process the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = [
        "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as",
        "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he",
        "she", "him", "his", "her", "hers", "its", "they", "them", "their",
        "what", "which", "who", "whom", "this", "that", "am", "are", "was",
        "were", "be", "been", "being", "have", "has", "had", "do", "does",
        "did", "but", "at", "by", "with", "from", "here", "when", "where",
        "how", "all", "any", "both", "each", "few", "more", "some", "such",
        "no", "nor", "too", "very", "can", "will", "just", "for", "in", 
        "not", "on"
    ]
    
    word_frequencies = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                word = word.lower()
        
                # Remove punctuations from word
                table = word.maketrans("", "", punctuations)
                word = word.translate(table)

                # Skip uninteresting words and words with non-alphabetical characters
                if word in uninteresting_words or not word.isalpha():
                    continue
                
                # Update frequencies of word
                word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    # Word cloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequencies)
    return cloud.to_array()

# Display the word cloud image
image = generate_wordcloud("The Picture of Dorian Gray - Oscar Wilde.txt")
plt.imshow(image, interpolation = "nearest")
plt.axis("off")
plt.show()