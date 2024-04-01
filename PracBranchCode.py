print('spngebob square pant')
from pandas import *

clt = read_csv('customers-1000.csv')
f = list(clt)
print(clt)

print(f)

class MyClass:
	print('bruh')
	def __init__(self, country):
		self.country = country
	def iffromChina(self):
		countries = []
		for row in clt:
			if row[6] == "China":
				countries.append(row)
		return countries
stuff =clt.MyClass()
print(stuff)
