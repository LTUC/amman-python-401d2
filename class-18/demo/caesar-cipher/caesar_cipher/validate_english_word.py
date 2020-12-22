import nltk
nltk.download('words')

english_words = nltk.corpus.words.words()

print(len(english_words))


def count_valid_english_words(sentence):
    """
    returns number of valid English words in the sentence

    >>> count_valid_english_words('hi fgrt bread ujhgfvsgdvhsdhj jkhyjuhg')
    2
    >>> count_valid_english_words('hi from classs')
    3
    """

    words = sentence.split()
    counter = 0

    for word in words:
        if word in english_words or word.lower() in english_words or word.upper() in english_words:
            counter += 1
    return counter
