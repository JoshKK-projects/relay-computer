import switchboard
class ToggleSwitch:
	def __init__(self,output = None):#take array by default, no singltons, this is dumb as is
		self.output = output
		Switchboard.allSwitches.append(self)
	def display(self):
		if self.output is not None:
			if isinstance(self.output, list):
				string = '|'
				for gate in self.output:
					string+= '| Connection State: ' + str(gate.gate) + ' |'
				string+='|'
				return string
			else:
				return '|| State: ' + str(self.output.gate) + ' ||'
		else:
			return '|| State: unconnected ||'
		
	def toggle(self):
		if self.output is not None:
			toggle = raw_input('Toggle Gate(y/N)')
			if isinstance(self.output, list):
				if toggle == 'y':
					for out in self.output:
						print out.name
						print out.gate
						if out.gate > 0:
							out.gate = 0
						else:
							out.gate = 1
				toggle = raw_input('Run Cycle(y/N)')
				if toggle == 'y':
					self.getAllTasks()
					#for out in self.output:
					#	print 'toggling for ' + out.output.name
					#	if out.output not in Clock.tasksThisCycle:
							#do not run cycle with single switch task, append ALL switches/sources of input
							#Clock.tasksThisCycle.append(out.output)
				Clock.runCycle()
			else:
				if toggle == 'y':
					if self.output.gate > 0:
						self.output.gate = 0
					else:
						self.output.gate = 1
				toggle = raw_input('Run Cycle(y/N)')
				if toggle == 'y':
					if self.output not in Clock.tasksThisCycle:
						Clock.tasksThisCycle.append(self.output)
					Clock.runCycle()
		else:
			print 'Unconnected, cannot toggle'

	def getAllTasks(self):
		switches = Switchboard.allSwitches
		for switch in switches: 
			if isinstance(switch.output, list):
				for out in switch.output:
					Clock.tasksThisCycle.append(out)
			else:
				Clock.tasksThisCycle.append(switch.output)




