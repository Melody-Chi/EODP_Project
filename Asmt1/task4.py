import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task4():
    # Use the data source from task2 and task3.
    review = pd.read_csv("task2.csv")
    price = pd.read_csv("task3.csv") 
    
    # Combine the reviews and prices make it as a new form.
    # Split "Pet Supplies" out.
    combine = review.merge(price, left_on="ID", right_on="ID")
    combine = combine.where(combine["category_x"] == "Pet Supplies")
    combine = combine.dropna()  # Drop none items.

    # Use scatter to make the plot. 
    plt.scatter(combine["average_score"], combine["average_cost"])

    # Setting the axis name and title.
    plt.xlabel("Average review score of Pet Supplies")
    plt.ylabel("Average price of Pet Supplies")
    plt.title("Average price and average review score for each product in 'Pet Supplies'.")

    # Setting the axis scale
    x_ticks = np.arange(0, 6, 1)
    y_ticks = np.arange(0, 160, 20)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)

    # Save the plot.
    plt.savefig('task4.png')

    return
