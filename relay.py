class relay:
	def __init__(self, power = 0, gate = 0, output = None, outputType = None):
		self.power = power
		self.gate = gate
		self.output = output
		self.outputType = outputType
	
	def setOutput(self):
		if self.power == 1 and self.gate == 1:
			onOff = 1
		else:
			onOff = 0

		if self.outputType == 'gate':
			self.output.setGate(onOff)
		else:
			self.output.setPower(onOff)

	def setGate(self, onOff):
		self.gate = onOff

	def setPower(self, onOff):
		self.power = onOff
