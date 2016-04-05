class Inverter:
	def __init__(self,power = 1, output = None, outputType = None, name = 'inverter'):
		self.power = power
		self.output = [output]
		self.outputType = outputType
		self.name = name
	
	def setOutput(self):
		onOff = self.state()
		if self.outputType == 'gate':
			for out in self.output:
				out.setGate(onOff)
		else:
			for out in self.output:
				out.setPower(onOff)
		return onOff

	
	def setPower(self, onOff):
		self.power = onOff

	def state(self):
		if self.power == 1:
			return 0
		else:
			return 1