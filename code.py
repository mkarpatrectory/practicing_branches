import pandas as pd

print("My boy Aidan P. has unlimited rizz.")

fl = pd.read_csv('customers-1000.csv')

cols = fl.columns.tolist()

names = fl[cols[2]].tolist()
cities = fl[cols[5]].tolist()


class facts:
	def __init__(self,name,city):
		self.name = name
		self.city = city
		
p1 = facts(names[1],cities[1])

print(p1.name)
