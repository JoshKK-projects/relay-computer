class lightbulb:
	def __init__(self, power = 0):
		self.power = 0
	def setOutput(self):
		if self.power == 1:
			print 1
		else:
			print 0

	def setPower(self, onOff):
		self.power = onOff