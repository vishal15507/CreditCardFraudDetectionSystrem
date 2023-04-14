import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Importing data
df = pd.read_csv('data/Simulation Dataset.csv')


# Data Preprocessing
df = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'isFraud']]
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])

#Importing the pretrained transactions
df2 = pd.read_csv('data/Transactions.csv')

#Preprocessing dataset
df2 = df2[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'isFraud']]
df2['type'] = le.fit_transform(df2['type'])

#Combining the dataframes
df3 = pd.concat([df2,df])

#UnderSampling
fraud_df = df3.loc[df3['isFraud'] == 1]
non_fraud_df = df3.loc[df3['isFraud'] == 0][:150000]

df3 = pd.concat([fraud_df, non_fraud_df])

# Splitting the data frame
X = df3.iloc[:,:-1]
y = df3.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print('Data is split in training and testing set.')

#importing model
rf_clf = pickle.load(open('model/rf_model.pkl', 'rb'))
print('Model has been imported.')

# training the model
rf_clf.fit(X_train, y_train)

# testing the model accuracy
accuracy = accuracy_score(y_test, rf_clf.predict(X_test))

#Saving the model if the accuracy is maintained
if accuracy > 0.9999:
    pickle.dump(rf_clf, open('model/rf_model.pkl', 'wb'))
    print('The model has been saved.')
else:
    print('No changes in the model.')