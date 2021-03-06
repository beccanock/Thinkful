import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#Frequencies
c = collections.Counter(x)
count_sum = sum(c.values())
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

#Boxplot
plt.boxplot(x)
plt.title('Box Plot')
plt.show()

#Histogram
plt.hist(x, histtype='bar')
plt.title('Histogram')
plt.show()

#QQ Plot
plt.figure()  
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.title('QQ Plot')
plt.show()
