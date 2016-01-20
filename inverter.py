class Inverter:
	def __init__(self,power = 1, output = None, outputType = None, name = None):
		self.power = power
		self.output = output
		self.outputType = outputType
	
	def setOutput(self):
		if self.power:
			onOff = 0
		else:
			onOff = 1
		print self.name	+ ' sent output ' + str(onOff) + ' to ' + self.output.name
		if self.outputType == 'gate':
			self.output.setGate(onOff)
		else:
			self.output.setPower(onOff)

	
	def setPower(self, onOff):
		self.power = onOff