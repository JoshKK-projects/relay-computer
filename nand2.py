import inverter
import and2
class NAND2:
	def __init__(self, output = None, outputType = None):
		self.i = Inverter(1,output,outputType)
		self.a2 = AND2(self.i,'power')
		self.input1 = self.a2.r1
		self.input2 = self.a2.r2