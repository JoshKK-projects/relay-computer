class Clock:
	tasksThisCycle = []
	tasksNextCycle = []
	@classmethod
	def runCycle(cls):
		while cls.tasksThisCycle :
			for task in cls.tasksThisCycle:
				print "clock set outout of " + str(task.name)
				task.setOutput()
				cls.tasksThisCycle.remove(task)
				if(task.output != 0):
					cls.tasksNextCycle.append(task.output)
				print "new cycle"
			cls.tasksThisCycle = cls.tasksNextCycle