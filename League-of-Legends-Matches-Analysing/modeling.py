'''
Analysing data with supervised learning method
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.sparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree

#function make binned data
def binned(cell):
    return equal_width.fit_transform(cell).astype(int)

#discrete data set
def discrete(df, col):
    df[col] = binned(df[[col]])

#apply regression method
def reg(df):
    #getting taining&testing set
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['kda']).values, df['kda'].values, test_size=0.2, random_state=64)
    lm = LinearRegression()
    lm.fit(x_train, y_train)
    y_pred = lm.predict(x_test)
    r2 = lm.score(x_test, y_test)
    mse = mean_squared_error(y_test, y_pred)
    print('R2', r2)
    print('MSE', mse)
    residuals = y_test - y_pred
    return residuals, x_train, x_test, y_train, y_test, y_pred

#apply k-nn method
def nn(df, k):
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['kda']).values, df['kda'].values, test_size=0.2, random_state=64)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    accuracy = knn.score(x_test, y_test)
    print('Accuracy', accuracy)
    return x_train, x_test, y_train, y_test, y_pred

#generating confusion matrix
def c_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Low', 'Medium', 'High'])
    disp.plot()
    plt.title("Confusion Matrix")

#read training dataset that only contains dependent variables with kda
indpt = ['champion','side', 'd_spell', 'f_spell', 'assists', 'deaths', 'kills', 'level', 'server', 'time_cc', 'vision_score']
mj_t = pd.read_csv('wrangled_data/mj_t.csv').drop(indpt, axis=1)
mj_o = pd.read_csv('wrangled_data/mj_o.csv').drop(indpt, axis=1)
mj_t['minions_killed'] = mj_t['minions_killed'].map({'Many':1, 'Few':0})
mj_o['minions_killed'] = mj_o['minions_killed'].map({'Many':1, 'Few':0})

#using regression method and visualise the result
print('Applying regression:')
print('Data of the role Toplane or Jungle:')
res_t, x_train_t, x_test_t, y_train_t, y_test_t, y_pred_t = reg(mj_t)
plt.scatter(y_test_t, y_pred_t, alpha=0.3, label='Toplane or Jungle')
print('Data of the role Other:')
res_o, x_train_o, x_test_o, y_train_o, y_test_o, y_pred_o = reg(mj_o)
plt.scatter(y_test_o, y_pred_o, alpha=0.3, label='Other')
plt.title('Linear Regression (Predict Total)')
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.legend()
plt.savefig('plots/regression.png')
plt.clf()

#visualising the residual of the regression result
plt.scatter(y_pred_t, res_t, alpha=0.3, label='Toplane or Jungle')
plt.scatter(y_pred_o, res_o, alpha=0.3, label='Other')
plt.plot([min(y_pred_t), max(y_pred_t)], [0,0], color='red')
plt.plot([min(y_pred_o), max(y_pred_o)], [0,0], color='red')
plt.title('Residual Plot')
plt.xlabel('Fitted')
plt.ylabel('Residual')
plt.legend()
plt.savefig('plots/regression_res.png')
plt.clf()

#discrete kda and visualise its distribution
equal_width = KBinsDiscretizer(n_bins=3,encode='ordinal', strategy='uniform')
discrete(mj_t, 'kda')
discrete(mj_o, 'kda')
plt.hist(mj_t['kda'], bins=3, alpha=0.3, label='Toplane or Jungle')
plt.hist(mj_o['kda'], bins=3, alpha=0.3, label='Other')
plt.legend()
plt.savefig('plots/ds_kda_dis.png')

#using knn method and visualise the result in confusion matrix
print('Applying knn:')
print('Data of the role Toplane or Jungle:')
x_train_t, x_test_t, y_train_t, y_test_t, y_pred_t = nn(mj_t, 3)
c_matrix(y_test_t, y_pred_t)
plt.savefig('plots/cm_t.png')
print('Data of the role Other:')
x_train_o, x_test_o, y_train_o, y_test_o, y_pred_o = nn(mj_o, 3)
c_matrix(y_test_o, y_pred_o)
plt.savefig('plots/cm_o.png')
