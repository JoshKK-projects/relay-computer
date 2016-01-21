class Clock:
	tasksThisCycle = []
	tasksNextCycle = []
	taskInputs = []
	toggledTasks = []
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
				print 'tasks not to do { '
				for togs in cls.toggledTasks:
					print togs.name
				print ' }'
				if task.output not in cls.toggledTasks:
					task.setOutput()
					if not isinstance(task.output, int):
						cls.toggledTasks.append(task.output) 
						cls.tasksNextCycle.append(task.output)
				# if(task.output != 0):
				# 	cls.tasksNextCycle.append(task.output)
			cls.tasksThisCycle = []
			cls.tasksThisCycle = cls.tasksNextCycle[:]
			cls.tasksNextCycle = []
			cls.toggledTasks = []