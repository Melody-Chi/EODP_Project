import pandas as pd
import json

def task1():
    # Read the file.
    file_read = pd.read_csv (r'/course/data/dataset.csv')

    # Remove the reduplicate products.
    set1 = set(file_read['category'])
    set2 = set(file_read['ID'])
    
    # Use len() to count the number then put them in a dictionary.
    task1_dict = {"Number of Products:": len(set2),
    "Number of Categories:": len(set1)}
    
    # Output the json file.
    with open("task1.json", "w") as outfile:
        json.dump(task1_dict, outfile)

    return
