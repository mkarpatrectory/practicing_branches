import pandas as pd

print("Rizzler is here")

fl=pd.read.csv('customers-100.csv')
cols=fl.columns.tolist()

name=fl[cols[2]].tolist()

class rizz:
	def __init__(self,name):
		self.name=name
		
		
pl =rizz(name[1])

print(pl)
