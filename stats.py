import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#print the mean
alcohol_mean = df['Alcohol'].mean() 
tobacco_mean = df['Tobacco'].mean() 

print("The mean alcohol consumption is " + str(alcohol_mean))
print("The mean tobacco use is " + str(tobacco_mean))

#print the median
alcohol_median = df['Alcohol'].median() 
tobacco_median = df['Tobacco'].median() 
print("The median alcohol consumption is " + str(alcohol_median))
print("The median tobacoo use is " + str(tobacco_median))

#print the mode
alcohol_mode = stats.mode(df['Alcohol']) 
tobacco_mode = stats.mode(df['Tobacco']) 
print("The alcohol consumption mode is " + str(alcohol_mode))
print("The tobacoo use mode is " + str(tobacco_mode))

#print the range
alcohol_range = max(df['Alcohol']) - min(df['Alcohol'])
tobacco_range = max(df['Tobacco']) - min(df['Tobacco'])
print("The range of alcohol consumption is " + str(alcohol_range))
print("The range of tobacco consumption is " + str(tobacco_range))

#print the variance
alcohol_variance = df['Alcohol'].var()
tobacco_variance = df['Tobacco'].var() 
print("The variance of alcohol consumption is " + str(alcohol_variance))
print("The variance of tobacco use is " + str(tobacco_variance))

#print the standard deviation
alcohol_sd = df['Alcohol'].std() 
tobacco_sd = df['Tobacco'].std()
print("The alcohol consumption standard deviation is " + str(alcohol_sd))
print("The tobacco use standard deviation is " + str(tobacco_sd))

