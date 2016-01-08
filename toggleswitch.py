import toggleswitch
class ToggleSwitch:
	def __init__(self,output = None):
		self.output = output
		Switchboard.allSwitches.append(self)
	def display(self):
		print '|| State: ' + str(self.output.gate) + ' ||'
	def toggle(self):
		toggle = raw_input('Toggle Gate(y/N)')
		if toggle == 'y':
			if self.output.gate > 0:
				self.output.gate = 0
			else:
				self.output.gate = 1
		toggle = raw_input('Run Cycle(y/N)')
		if toggle == 'y':
			Clock.tasksThisCycle.append(self.output)
			Clock.runCycle()