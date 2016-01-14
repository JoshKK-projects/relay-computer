import relay
class OR2:
	def __init__ (self, output = None, outputType = None):
		self.r1 = Relay(1,0,output,outputType)
		self.r2 = Relay(1,0,output,outputType)
		self.input1 = self.r1
		self.input2 = self.r2