#Importing required packages
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit


#Importing Data
data = pd.read_csv('data/data.csv')
print(data.head())

#Checking the number of fraud and non fraud transactions in the data
print('Number of frauds:', data.isFraud[data['isFraud'] == 1].count())
print('Number of Non frauds:', data.isFraud[data['isFraud'] == 0].count())

#Keeping 5 percent of the transactions for simulation
ss = StratifiedShuffleSplit(n_splits = 1,
                            test_size = 0.05,
                            train_size = 0.95,
                            random_state = 12)


X = data.iloc[:,:-1]
y = data.iloc[:,-1]

for train_index, test_index in ss.split(X, y):
    transactions_df = data.iloc[train_index]
    simulation_df = data.iloc[test_index]

#Saving the transaction_df for training and testing the model
transactions_df.to_csv('data/Transactions.csv', index = False )
print('Transactions csv saved successfully')

# Balancing and shuffling the simulation dataset

# printing the number of fraud and non fraud transactions in simulation dataset
print('Number of frauds in simulation dataset:', simulation_df.isFraud[simulation_df['isFraud'] == 1].count())
print('Number of Non frauds in simulation dataset:', simulation_df.isFraud[simulation_df['isFraud'] == 0].count())

#Under sampling the simulation dataset
fraud_df = simulation_df.loc[simulation_df['isFraud'] == 1]
non_fraud_df = simulation_df.loc[simulation_df['isFraud'] == 0][:500]
balanced_simulation_df = pd.concat([fraud_df, non_fraud_df])

# printing the number of fraud and non fraud transactions in simulation dataset after balancing
print('Number of frauds after balancing simulation dataset:', balanced_simulation_df.isFraud[balanced_simulation_df['isFraud'] == 1].count())
print('Number of Non frauds after balancing simulation dataset:', balanced_simulation_df.isFraud[balanced_simulation_df['isFraud'] == 0].count())

# Shuffling the balanced Dataset
balanced_simulation_df = balanced_simulation_df.sample(frac=1).reset_index(drop=True)

# Saving the simulation dataset after balancing and Shuffling
balanced_simulation_df.to_csv('data/Simulation Dataset.csv', index = False )
print('Simulation csv saved successfully')