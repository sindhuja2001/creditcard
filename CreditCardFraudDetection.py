import pandas as pd
import numpy as np
import sklearn
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report,accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from pylab import rcParams
import mysql.connector
import imblearn
import joblib
RANDOM_SEED = 42
LABELS = ["Normal", "Fraud"]

db_connect= mysql.connector.connect(host= '127.0.0.1', database= 'credit', user= 'root', password= 'Sindhuja@2001')
# df= pd.read_sql('', con= db_connect)
# df.head()

df = pd.read_csv('creditcard.csv')
# df1= df.sample(frac = 0.1,random_state=1)
Normal = df[df['Class']==0]
Fraud = df[df['Class']==1]
columns = df.columns.tolist()
# Filter the columns to remove data we do not want 
columns = [c for c in columns if c not in ["Class"]]
# Store the variable we are predicting 
target = "Class"
# Define a random state 
# state = np.random.RandomState(42)
X = df[columns]
Y = df[target]


from imblearn.over_sampling import SMOTE
# over_sample = SMOTE()
x_smote, y_smote = SMOTE(k_neighbors = 1).fit_resample(X, Y)
from sklearn.model_selection import train_test_split    
x_train, x_test, y_train, y_test= train_test_split(x_smote,y_smote, test_size= 0.2, random_state=0) 
from sklearn.metrics import classification_report, f1_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
# training
model.fit(x_train, y_train)
# testing
y_pred = model.predict(x_test)

joblib.dump(model, "CreditCardFraudDetection.joblib")