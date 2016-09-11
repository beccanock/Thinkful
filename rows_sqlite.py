import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:

	cur = con.cursor()
	#cur.execute("DELETE FROM weather where city = 'Washington'")
	cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
	cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
	cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', '')")
	cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', '')")

cities = (('Las Vegas', 'NV'), ('Atlanta', 'GA'))
weather = (('Las Vegas', 2013, 'July', 'December', ''), ('Atlanta', 2013, 'July', 'January', ''))

with con:

	cur = con.cursor()
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)


