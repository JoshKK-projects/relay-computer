import clock
class Relay:
	def __init__(self, power = 0, gate = 0, output = None, outputType = None, name = None, programInput = False):
		self.power = power
		self.gate = gate
		self.output = output
		self.name = name
		self.outputType = outputType
		if programInput:
			Clock.taskInputs.append(self)
	
	def setOutput(self):
		onOff = self.state()
		
		print self.name	+ ' sent output ' + str(onOff) + ' to ' + self.output.name
		if self.outputType == 'gate':
			self.output.setGate(onOff)
		else:
			self.output.setPower(onOff)
		return onOff

	def setGate(self, onOff):
		self.gate = onOff
		

	def setPower(self, onOff):
		self.power = onOff

	def state(self):
		if self.power == 1 and self.gate == 1:
			onOff = 1
		else:
			onOff = 0
		return onOff
