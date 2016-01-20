class Clock:
	tasksThisCycle = []
	tasksNextCycle = []
	taskInputs = []
	@classmethod	# not calling all inputs properly e.g. XOR OR
	def runCycle(cls):
		print "new cycle"
		cls.tasksThisCycle = cls.taskInputs[:]
		print 'initial relays:'
		for task in cls.tasksThisCycle:
			print task.name
		while cls.tasksThisCycle:
			print str(len(cls.tasksThisCycle)) + ' tasks this cycle'
			for task in cls.tasksThisCycle:
				print 'tasking ' + task.name
				task.setOutput()
				#cls.tasksThisCycle.remove(task)#needs to be movedddd..???
				if(task.output != 0):
					cls.tasksNextCycle.append(task.output)
			cls.tasksThisCycle = []
			cls.tasksThisCycle = cls.tasksNextCycle[:]
			cls.tasksNextCycle = []