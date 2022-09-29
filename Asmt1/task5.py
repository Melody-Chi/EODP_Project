import pandas as pd
import matplotlib.pyplot as plt
#from unicodedata import category

def task5():
    # Read the data source from task2.
    review = pd.read_csv("task2.csv")

    # Split out the category.
    # Caculate the means of the average review scores of products in each category.
    review_cate = review.groupby("category")
    category = [i for i, j in review_cate]
    average_review = [j["average_score"].mean() for i, j in review_cate]

    # Set up a new array to sore the values.
    new_array = []
    for num in range(len(category)):
        new_array.append([category[num], average_review[num]])
    new_array.sort(key=new_array[1])

    for num in range(len(new_array)):
        category[num] = new_array[num][0]
        average_review[num] = new_array[num][1]
    
    # Setting the figure size to prevent x and y labels out of the boundary.
    plt.figure(figsize=(20,15), dpi=80)

    # Drawing the plot.
    plt.barh(category, average_review)

    # Setting the axis name and title.
    plt.xlabel("Category")
    plt.ylabel("Average review score")
    plt.title("The means of average review score of products")
    
    # Save the figure.
    plt.savefig('task5.png')
    return
