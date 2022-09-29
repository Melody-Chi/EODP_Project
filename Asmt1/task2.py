import pandas as pd
import json
import re

def task2():

    # Read the dataset file.
    file_read = pd.read_csv (r'/course/data/dataset.csv')
    
    # Create lists to store messages.
    id_list = []
    category_list = []
    average_score = []
    
    # Loop each reviewlist, define ID, category, and Reviewlist.
    for i, row in file_read.iterrows():
        file_id = row["ID"]
        file_category = row["category"]
        file_review = row["REVIEWLIST"]

        file_review = json.loads(file_review)
        sum_star = 0
        count = 0

        # Iterate the reviews to find the star review and caculate the average stars.
        for review in file_review:
            if(review["review_star"]):
                # Find the number of each review by using re.group method.
                star=int(re.search("\d", review["review_star"]).group())
                sum_star += star
                count += 1
        if(count is not 0):
            # Caculate the average score.
            average = sum_star/count
        else:
            average = 0

        # Each time finish the iteration, put the data into the lists.
        average_score.append(average)
        id_list.append(file_id)
        category_list.append(file_category)
    
    # Build the dataframe.
    task2_df = pd.DataFrame({
        "ID" : id_list,
        "category" : category_list,
         "average_score" : average_score
    })
    
    # Output the csv file by sorting "ID".
    task2_df.sort_values(by = ["ID"])
    task2_df.to_csv("task2.csv", index=False)

    return
