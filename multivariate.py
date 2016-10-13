import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

#Load the Lending Club Statistics
df = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

df.dropna(inplace=True)
df['Interest.Rate'] = map(lambda x: x.rstrip('%'), df['Interest.Rate'])

df['Interest.Rate'] = df['Interest.Rate'].astype(float)

df['Intercept'] = 1.0

#Use income (annual_inc) to model interest rates (int_rate)
ind_vars = ['Intercept', 'Monthly.Income']
model_1 = sm.OLS(df['Interest.Rate'], df[ind_vars])
result_1 = model_1.fit()
coeff_1 = result_1.summary()
print(coeff_1)
#Interest.Rate = 12.9929 + 1.363e-05*Monthly.Income

#Add home ownership (hone_ownership) to the model
df['Home.Ownership'] = pd.Categorical(df['Home.Ownership']).labels
#print(df['Home.Ownership'].head())
#house_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in house_ownership]
ind_vars_2 = ['Intercept', 'Monthly.Income', 'Home.Ownership']
model_2 = sm.OLS(df['Interest.Rate'], df[ind_vars_2])
result_2 = model_2.fit()
coeff_2 = result_2.summary()
print(coeff_2)
#Interest.Rate = 12.5221 + 3.225e-05*Monthly.Income + 0.2374*Home.Ownership

#Interaction of home ownership and income
df['Interaction'] = df['Home.Ownership'] * df['Monthly.Income']
ind_vars_3 = ['Intercept', 'Monthly.Income', 'Home.Ownership', 'Interaction']
model_3 = sm.OLS(df['Interest.Rate'], df[ind_vars_3])
result_3 = model_3.fit()
coeff_3 = result_3.summary()
print(coeff_3)
#Interest.Rate = 12.6724 + 9.497e-06*Monthly.Income + 0.0736*Home.Ownership + 3.073e-05*Interaction

