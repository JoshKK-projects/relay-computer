class Clock:
	tasksThisCycle = []
	tasksNextCycle = []
	@classmethod
	def runCycle(cls):
		while cls.tasksThisCycle :
			for task in cls.tasksThisCycle:
				task.setOutput()
				cls.tasksThisCycle.remove(task)
				if(task.output != 0):
					cls.tasksNextCycle.append(task.output)
			cls.tasksThisCycle = cls.tasksNextCycle