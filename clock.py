class clock:
	tasksThisCycle = []
	tasksNextCycle = []
	@staticmethod
	def runCycle():
		for task in tasksThisCycle:
			task.setOutput()
			method = getattr(task, 'output', None)
			if method != None
				tasksNextCycle.append(task.output)
		tasksThisCycle = tasksNextCycle
		if len(tasksThisCycle) != 0
			runCycle()