import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#Read in the loan data and load it into a pandas DataFrame
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#Clean the data
loansData.dropna(inplace=True)

#Box Plot
loansData.boxplot(column='Amount.Requested')
plt.show()

#Histogram
loansData.hist(column='Amount.Requested')
plt.show()

#QQ Plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()

#How the resilts compare to "Amount.Funded.By.Investors":
#Median about the same
#Minimum is higher; maximum value is similar
#Mode still around 5000 with tail to the right
#Both not normally distributed