import half_adder
class FullAdder:
	def __init__(self,carry_out = None, carryoutputType = None, sum_out = None, sumoutputType = None):
		self.o2 = OR2(carry_out,carryoutputType)
		self.adder1 = HalfAdder(self.o2.input1, 'gate', sum_out, sumoutputType)
		self.adder2 = HalfAdder(self.o2.input2, 'gate', self.adder1.input1, 'gate')#issue here, setting carry out - 1 relay - to output to 3 relays
		self.input1 = self.adder2.input1
		self.input2 = self.adder2.input2
		self.input3 = self.adder1.input1#carry in

