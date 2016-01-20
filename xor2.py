import or2
import nand2
import and2#redundant since nand2 imports but clarity for now
class XOR2:
	def __init__(self, output = None, outputType = None):
		self.a2 = AND2(output, outputType)
		self.na2 = NAND2(self.a2.input1, 'gate')
		self.o2 = OR2(self.a2.input2,'gate')#never getting triggered
		self.input1 = [self.na2.input1, self.o2.input1]
		self.input2 = [self.na2.input2, self.o2.input2]