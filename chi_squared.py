from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

#Load the data
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#Clean the data
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Amount.Requested'])


#Perform the chi-squared test and print the results
chi, p = stats.chisquare(freq.values())
print(chi, p)
