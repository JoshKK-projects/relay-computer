import clock
class Relay:
	def __init__(self, power = 0, gate = 0, output = None, outputType = None, name = 'relay', programInput = False):
		self.power = power
		self.gate = gate
		self.output = [output]
		self.name = name
		self.outputType = outputType
		if programInput:
			Clock.taskInputs.append(self)
	
	def setOutput(self):
		onOff = self.state()
		if self.outputType == 'gate':
			for out in self.output:
				out.setGate(onOff)
		else:
			for out in self.output:
				out.setPower(onOff)
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
