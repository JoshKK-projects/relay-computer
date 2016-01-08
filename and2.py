import relay
class AND2:
	def __init__(self, output = None, outputType = None):
		self.r1 = Relay(0,0,output,outputType)
		self.r2 = Relay(1,0,self.r1,'power')
