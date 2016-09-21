import pandas as pd
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt

df = pd.read_csv('loansData_clean.csv')

df['IR_TF'] = map(lambda x: True if x < 12 else False, df['Interest.Rate'])

df[df['Interest.Rate'] == 10].head() # should all be True
df[df['Interest.Rate'].astype(int) == 13].head() # should all be False

df['Intercept'] = 1.0

ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']

logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()
coeff = result.params
print(coeff)

def logistic_function(FICO_Score, Loan_Amount):
	a = (coeff[0] + (coeff[1] * FICO_Score) + (coeff[2] * Loan_Amount))
	p = 1/(1 + math.e**a)
	return p

print(logistic_function(720, 10000))

print(logistic_function(750, 10000))

print(logistic_function(400, 10000))

plt.scatter(df['FICO.Score'], df['IR_TF'])
plt.show()

plt.scatter(df['Amount.Requested'], df['IR_TF'])
plt.show()