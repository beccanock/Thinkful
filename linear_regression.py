import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

#Import Data
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#Explore Data
loansData['Interest.Rate'][0:5]
loansData['Loan.Length'][0:5] 
loansData['FICO.Range'][0:5] 

#Clean Data
loansData['Interest.Rate'] = map(lambda x: x.rstrip('%'), loansData['Interest.Rate'])
loansData['Loan.Length'] = map(lambda x: x.rstrip(' months'), loansData['Loan.Length'])

loansData['FICO.Score'] = loansData['FICO.Range'].astype(str)
loansData['FICO.Score'] = map(lambda x: x.split('-'), loansData['FICO.Score'])
loansData['FICO.Score'] = map(lambda x : x[0], loansData['FICO.Score'])
loansData['FICO.Score'] = loansData['FICO.Score'].astype(float)

#Histogram
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#Scatterplot Matrix
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

#Extract Columns
intrate = loansData['Interest.Rate'].astype(float)
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score'].astype(int)

#Reshape the Data
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
f.summary()

print(f.summary())

loansData.to_csv('loansData_clean.csv', header=True, index=False)
