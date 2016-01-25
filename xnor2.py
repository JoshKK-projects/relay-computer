import xor2
import inverter
class XNOR2:
	def __init__(self, output = None, outputType = None):
		self.i = Inverter(1,output,outputType)
		self.xor = XOR2(self.i,'power')
		self.input1 = self.xor.input1
		self.input2 = self.xor.input2