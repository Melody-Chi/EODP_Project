import pandas as pd
import re

def task3():
    # Read the file and set up the lists.
    file_read = pd.read_csv (r'/course/data/dataset.csv')

    id_list = []
    category_list = []
    average_cost = []
    
    # Set the pattern to extract the price figures.
    # Initialize the product cost to 0.
    product_cost = 0
    pattern = r"\d\d*\.\d\d"

    # Iterate the reviewlist, put all product costs into a list.
    for i, row in file_read.iterrows():
        file_id = row["ID"]
        file_category = row["category"]
        cost_list = re.findall(pattern, str(row['cost']))

        # Caculate the cost of each product.
        if len(cost_list) == 0:
            product_cost = 0
        elif len(cost_list) == 1:
            product_cost = float(cost_list[0])
        else:
            product_cost = (float(cost_list[0])+float(cost_list[1]))/2
        
        # Each time finish the iteration, put the data into the lists.
        average_cost.append(product_cost)
        id_list.append(file_id)
        category_list.append(file_category)

    
    # Build the dataframe.
    task3_df = pd.DataFrame({
        "ID" : id_list,
        "category" : category_list,
        "average_cost" : average_cost
    })
    
    # Output the csv file by sorting "ID".
    task3_df.sort_values(by = ["ID"])
    task3_df.to_csv("task3.csv", index=False)


    return
