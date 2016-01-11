import toggleswitch
class Switchboard:
	allSwitches = []
	asignedSwitches = {}
	@classmethod
	def printSwitchBoard(cls):
		for key in cls.asignedSwitches:
			if cls.asignedSwitches[key] is not None:
				print "{{ " + key + " " + cls.asignedSwitches[key].display() + " }}"
			
	@classmethod
	def assignKeys(cls):
		asciiVals = 65
	 	for switch in cls.allSwitches:
	 		cls.asignedSwitches[chr(asciiVals)] =  switch
			asciiVals+=1
		cls.takeKeysInput()
	@classmethod
	def takeKeysInput(cls):
		go = 1
		while go == 1:
			Switchboard.printSwitchBoard()
			keypress = raw_input('Select A Key:')
			if(keypress == 'end'):
				print 'ending...'
				return 0
			if keypress in cls.asignedSwitches:
				cls.asignedSwitches[keypress].toggle()

