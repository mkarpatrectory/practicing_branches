print("whats the word slim")
import pandas as pd

fl = pd.read.csv ('customer-1000.csv')
f = list(fl)
cols = fl.columns.tolist()

n = fl[cols[2]].tolist()
ci = fl[cols[5]].tolist()


print(f)

class APsClass:
	def__init__(self,country):
		self.country = country
	def ifChina(self):
		countries = []
		for row in clt:
			if row(6) == "China":
				countries.append(row)	
		return countries
	
