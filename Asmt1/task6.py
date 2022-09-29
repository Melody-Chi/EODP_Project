import pandas as pd
import json
import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.util import ngrams

def task6():
    
    file_read = pd.read_csv (r'/course/data/dataset.csv')

    # Set up the a list to store json file.
    json_list = []

    # Set up the stop word.
    StopWord = list(set(stopwords.words('english')))
    
    # Iterate review and score of each product and store.
    for i, row in file_read.iterrows():

        file_review = row["REVIEWLIST"]
        file_review = json.loads(file_review)

        # Iterate each review in a single product.
        for review in file_review:

            # Setting a dictionary to store the score and bigrams.
            review_dic = {}

            # Determining whether the set is empty, if not, save the star of products.
            if len(review["review_star"]) != 0:
                star = int(re.search("\d", review["review_star"]).group())

            # Save the body.
            body = review["review_body"]

            # Convert all non-alphabetic characters to single-space.
            # Remove the starting and ending space.
            convert_character = re.sub(r'[^A-Za-z]', ' ', body, flags=re.IGNORECASE)

            # Change all uppercase characters to lowercase.
            convert_character = " ".join(convert_character.split()).lower()

            # Remove the stop words.
            # Remove all the one or two characters words.
            word_list = [word for word in convert_character.split() 
                         if not word in StopWord]
            word_list = [word for word in word_list if len(word)>2]

            # Save the filtered data.
            convert_text = " ".join(word_list)

            # Computes bigrams(2-grams) given a tokenized text and save.
            bi_gram = ngrams(convert_text.split(), 2)
            bigram_result = [" ".join([a,b]) for a,b in bi_gram]

            # Save {"score": "bigrams"} in a dictionary.
            review_dic["score"] = star
            review_dic["bigrams"] = bigram_result

            # Put in the json list then convert to json.
            json_list.append(review_dic)
    with open('task6.json', 'w') as file:
        json.dump(json_list, file)

    return
