import clock
class Lightbulb:
	def __init__(self, power = 0, name = 'BULB'):
		self.power = 0
		self.output = 0
		self.name = name
		self.outputType = 'power'

	def setOutput(self):
		if self.power == 1:
			print self.name + ' 1'
		else:
			print  self.name + ' 0'

	def setPower(self, onOff):
		self.power = onOff

	def state(self):
		return self.power