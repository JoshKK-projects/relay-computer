class Clock:
	tasksThisCycle = []
	tasksNextCycle = []
	taskInputs = []
	toggledGateTasks = []
	toggledPowerTasks = []
	finalOutput = {}
	@classmethod	#if youve turned it on, you cant turn it off until next cycle
	def runCycle(cls):
		print "new program"
		cls.tasksThisCycle = cls.taskInputs[:]
		print 'initial relays:'
		for task in cls.tasksThisCycle:
			print task.name
		while cls.tasksThisCycle:
			print str(len(cls.tasksThisCycle)) + ' tasks this cycle'
			for task in cls.tasksThisCycle:
				cls.doOutputs(task)
			cls.tasksThisCycle = []
			cls.tasksThisCycle = cls.tasksNextCycle[:]
			cls.tasksNextCycle = []
			cls.toggledGateTasks = []
			cls.toggledPowerTasks = []
		print cls.finalOutput

	@classmethod	#if youve turned it on, you cant turn it off until next cycle
	def doOutputs(cls,task):
		print 'gate tasks not to do { ',
		for togs in cls.toggledGateTasks:
			print togs.name,
		print ' }'
		print 'power tasks not to do { ',
		for togs in cls.toggledPowerTasks:
			print togs.name,
		print ' }'
		print 'trying task ' + task.name
		if task.output not in cls.toggledGateTasks and task.outputType == 'gate':#if toggle on power or gate, cant toggle on other, need seperate, ugh
			task.setOutput()
			if not isinstance(task.output, int):
				#print task.output.name + ' added to next tasks'
				if(task.output.gate == 1):
					cls.toggledGateTasks.append(task.output) 
				cls.tasksNextCycle.append(task.output)
		if task.output not in cls.toggledPowerTasks and task.outputType == 'power':
			task.setOutput()
			if not isinstance(task.output, int):
				#print task.output.name + ' added to next tasks'
				if(task.output.power == 1):
					cls.toggledPowerTasks.append(task.output) 
				cls.tasksNextCycle.append(task.output)
		# if(task.output != 0):
		# 	cls.tasksNextCycle.append(task.output)
