import pandas as pd
import numpy as np 
import statsmodels.api as sm 
import matplotlib.pyplot as plt

df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

#print(year_month_summary.head(20))
#print(loan_count_summary.head(20))

#Plot the loan data
plt.plot(loan_count_summary)
plt.show()

#Is the series stationary? If not, what would you do to transform it into a stationary series?
#The series is not stationary. We could differentiate it.

loan_count_summary_diff = loan_count_summary.diff()
loan_count_summary_diff = loan_count_summary_diff.fillna(0)
#plt.plot(loan_count_summary_diff)

loan_count_summary_diff = loan_count_summary_diff + 316
loan_count_summary_diff = loan_count_summary_diff/max(loan_count_summary_diff)
plt.plot(loan_count_summary_diff)

#Plot out the ACF and PACF
sm.graphics.tsa.plot_acf(loan_count_summary)
sm.graphics.tsa.plot_pacf(loan_count_summary)
plt.show()

sm.graphics.tsa.plot_acf(loan_count_summary_diff)
sm.graphics.tsa.plot_pacf(loan_count_summary_diff)
plt.show()


