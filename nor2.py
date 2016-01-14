import or2
import inverter
class NOR2:
	def __init__(self, output = None, outputType = None):
		self.i = Inverter(1,output,outputType)
		self.o2 = OR2(self.i,'power')
		self.input1 = self.o2.r1
		self.input2 = self.o2.r2