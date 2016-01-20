class Clock:
	tasksThisCycle = []
	tasksNextCycle = []
	taskInputs = []#not being properly saved between runs - loosing stuff, this is isssuueee
	@classmethod	#also not calling all inputs properly e.g. XOR OR
	def runCycle(cls):
		cls.tasksThisCycle = cls.taskInputs
		print 'initial relays:'
		for task in cls.tasksThisCycle:
			print task.name
		while cls.tasksThisCycle:
			for task in cls.tasksThisCycle:
				task.setOutput()
				taskInputsHolder = cls.taskInputs
				cls.tasksThisCycle.remove(task)#whatever this removes seems to be gone everywhere in the class ref?????
				taskInputs = taskInputsHolder
				if(task.output != 0):
					cls.tasksNextCycle.append(task.output)
			print "new cycle"
			cls.tasksThisCycle = cls.tasksNextCycle