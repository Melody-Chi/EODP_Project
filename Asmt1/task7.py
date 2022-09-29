import collections
import math
import json
import matplotlib.pyplot as plt
import pandas as pd

def task7():

    json_list = []  # List to store json data.

    # Put the task6.json's data in a list.
    with open('task6.json', 'r') as f:
        json_list = json.load(f)

    posi_lst = []   # Store the positive bigrams.
    nega_lst = []   # Store the negative bigrams.
    
    for star in json_list:
        # Store the 5-star reviews to 'positive' 
        # and store the 1-star reviews to 'negative'.
        if str(star["score"]) == str(5):
            posi_lst.append(star["bigrams"])
        elif str(star["score"]) == str(1):
            nega_lst.append(star["bigrams"])

    # Summarize the bigrams.
    posi_lst = sum(posi_lst, [])
    nega_lst = sum(nega_lst, [])

    # Count the number of occurrences.
    posi_count = collections.Counter(posi_lst)
    nega_count = collections.Counter(nega_lst)

    # Define the probability that 
    # bigrams appear in positive and negative reviews
    # then store the probabilty in a dictionary.
    posi_prob = {}
    nega_prob = {}
    for key, value in posi_count.items():
        if((value/len(posi_lst))!= 0 or (value/len(posi_lst))!= 1):
            posi_prob[key] = value/len(posi_lst)

    for key, value in nega_count.items():
        if((value/len(nega_lst))!= 0 or (value/len(nega_lst))!= 1):
            nega_prob[key] = value/len(nega_lst)

    # Define the odds that bigrams appear in positive and negative reviews.
    posi_odds = {}
    nega_odds = {}
    for key, prob in posi_prob.items():
        posi_odds[key] = prob/(1-prob)

    for key, prob in nega_prob.items():
        nega_odds[key] = prob/(1-prob)

    
    # Define the odds ratio for reviews.
    odds_ratio = {}
    key_odds = set([key for key in posi_odds.keys()] + [key for key in nega_odds.keys()])

    for key in key_odds:
        if key not in posi_odds.keys() or key not in nega_odds.keys():
            pass
        else:
            odds_ratio[key] = posi_odds[key] / nega_odds[key]
    
    # Only keep the comman bigrams, count the log odds ratio.
    log_odds_ratio = {}
    for key, ratio in odds_ratio.items():
        log_odds_ratio[key] = round(math.log10(ratio), 4)

    # Output a csv file called task7a.csv.
    # Each row represents a bigram in the vocabulary 
    # and the log odds ratio for that bigram.
    task7a = pd.DataFrame({"bigram": log_odds_ratio.keys(), 
            "log_odds_ratio": log_odds_ratio.values()})
    task7a = task7a.sort_values(by="log_odds_ratio")
    task7a.to_csv("task7a.csv", index=False)

    # Output a file called task7b.png.
    # A graph showing the distribution of 
    # log_odds_ratio for bigrams in the vocabulary.
    plt.hist(task7a["log_odds_ratio"])
    plt.xlabel("log_odds_ratio")
    plt.ylabel("distribution")
    plt.title("Distribution of log_odds_ratio for bigrams")
    plt.savefig("task7b.png")

    # Output a file called task7c.png.
    # A graph shows the top10 bigrams with the highest odds ratios
    # and the top10 bigrams with the lowest odds ratios. 
    bottom_10 = task7a.sort_values("log_odds_ratio")[:10]
    top_10 = task7a.sort_values("log_odds_ratio", 
                ascending=False)[:10]
    
    plot, axis = plt.subplots(2)
    plot.suptitle('Odds ratios')

    axis[0].bar(top_10["bigram"],  
                bottom_10["log_odds_ratio"])
    axis[1].bar(bottom_10["bigram"], 
                top_10["log_odds_ratio"])

    axis[0].set_xticklabels(top_10["bigram"], rotation=45)
    axis[0].set_title("top 10 bigrams with the highest odds ratio")

    axis[1].set_xticklabels(bottom_10["bigram"], 
                            rotation=45)
    axis[1].set_title("top 10 bigrams with the lowest odds ratio")

    plot.tight_layout()
    plt.savefig("task7c.png")

    return
