import clock
class Lightbulb:
	def __init__(self, power = 0, name = 'bulb'):
		self.power = 0
		self.output = 0
		self.name = name
	def setOutput(self):
		if self.power == 1:
			print 1
		else:
			print 0

	def setPower(self, onOff):
		self.power = onOff