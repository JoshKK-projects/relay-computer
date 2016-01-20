import switchboard
class ToggleSwitch:
	def __init__(self,output = None):#flatten array thign or something so all can go in normally?
		self.output = output
		Switchboard.allSwitches.append(self)
		for relay in self.output:
			Clock.taskInputs.append(relay)
	def display(self):
		if self.output is not None:
			string = '|'
			for gate in self.output:
				string+= '| Connection State: ' + str(gate.gate) + ' |'
			string+='|'
			return string
		else:
			return '|| State: unconnected ||'
		
	def toggle(self):
		if self.output is not None:
			toggle = raw_input('Toggle Gate(y/N)')
			if toggle == 'y':
				for out in self.output:
					if out.gate > 0:
						out.gate = 0
					else:
						out.gate = 1
			toggle = raw_input('Run Cycle(y/N)')
			if toggle == 'y':
				Clock.runCycle()
		else:
			print 'Unconnected, cannot toggle'