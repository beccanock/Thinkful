import sqlite3 as lite
import pandas as pd

#Connect to the database
con = lite.connect('cities_database.db')

#Create the cities and weather tables
with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

#Insert data into the two tables

	cities = (('New York City', 'NY'),
		('Boston', 'MA'),
		('Chicago', 'IL'),
		('Miami', 'FL'),
		('Dallas', 'TX'),
		('Seattle', 'WA'),
		('Portland', 'OR'),
		('San Francisco', 'CA'),
		('Los Angeles', 'CA'),
		('Washington', 'DC'),
		('Houston', 'TX'),
		('Las Vegas', 'NV'),
		('Atlanta', 'GA'))

	weather = (('New York City', 2013, 'July', 'January', 62),
		('Boston', 2013, 'July', 'January', 59),
		('Chicago', 2013, 'July', 'January', 59),
		('Miami', 2013, 'July', 'January', 84),
		('Dallas', 2013, 'July', 'January', 77),
		('Seattle', 2013, 'July', 'January', 61),
		('Portland', 2013, 'July', 'December', 63),
		('San Francisco', 2013, 'September', 'December', 64),
		('Los Angeles', 2013, 'September', 'December', 75),
		('Washington', 2013, 'July', 'January', ''),
		('Houston', 2013, 'July', 'January', ''),
		('Las Vegas', 2013, 'July', 'December', ''),
		('Atlanta', 2013, 'July', 'January', ''))

	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

#Join the data together
	cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July'")	


#Load into a pandas DataFrame
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns = cols)

	warmest_July = []
	for i in range(0,10):
		warmest_July.append(df.loc[i,'name'])

#Print out the resulting city and state in a full sentence

#"The cities that are warmest in July are:" + 
print("The cities that are warmest in July are:" + str(warmest_July))



