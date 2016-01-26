import xor2
import and2
class HalfAdder:
	def __init__(self,carry_out = None, carryoutputType = None, sum_out = None, sumoutputType = None):
		self.a2 = AND2(carry_out, carryoutputType)
		self.xor = XOR2(sum_out, sumoutputType)
		self.input1 = self.xor.input1 + [self.a2.input1]
		self.input2 = self.xor.input2 + [self.a2.input2]