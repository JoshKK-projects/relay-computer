import toggleswitch
class Switchboard:
	allSwitches = []
	asignedSwitches = {}
	@classmethod
	def printSwitchBoard(cls):
		print len(cls.asignedSwitches)
		for key in cls.asignedSwitches:
			print '{{ ' + key + ' ' + cls.asignedSwitches[key].display() + ' }}'
			
	@classmethod
	def assignKeys(cls):
		asciiVals = 65
	 	for switch in cls.allSwitches:
	 		cls.asignedSwitches[chr(asciiVals)] =  switch
			asciiVals+=1
	@classmethod
	def takeKeysInput(cls):
		Switchboard.printSwitchBoard()
		keypress = raw_input('Select A Key:')
		if keypress in cls.asignedSwitches:
			cls.asignedSwitches[keypress].toggle()
		Switchboard.printSwitchBoard(cls)

