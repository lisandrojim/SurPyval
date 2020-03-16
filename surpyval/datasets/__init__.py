import pandas as pd

class BoforsSteel_():
	def __init__(self):
		self.df = pd.read_csv('surpyval/datasets/bofors_steel.csv')

class Bearing_():
	def __init__(self):
		x = [17.88, 28.92, 33, 41.52, 42.12, 45.6, 48.4, 51.84, 
     		51.96, 54.12, 55.56, 67.8, 68.64, 68.64, 68.88, 84.12, 
     		93.12, 98.64, 105.12, 105.84, 127.92, 128.04, 173.4]
		self.df = pd.DataFrame({'x' : x})

BoforsSteel = BoforsSteel_()
Bearing = Bearing_()