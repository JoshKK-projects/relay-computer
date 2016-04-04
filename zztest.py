# b1 = Lightbulb(0,'CARRY')
# b2 = Lightbulb(0,'SUM')
# o2 = OR2(b1, 'power');
# ha1 = HalfAdder(o2.input1,'gate',b2,'power')
# ha2 = HalfAdder(o2.input2,'gate',ha1.input1,'gate')
# t1 = ToggleSwitch(ha1.input2)
# t2 = ToggleSwitch(ha2.input1)
# t3 = ToggleSwitch(ha2.input2)
# print t1.output
# print t2.output
# print t3.output

# adder = FullAdder(b1, 'power', b2, 'power')
# t1 = ToggleSwitch(adder.adder1.input1)
# t2 = ToggleSwitch(adder.adder2.input1)
# t3 = ToggleSwitch(adder.adder2.input2)
# print adder.input1
# print adder.input2
# print adder.input3
####HALF ADDER TESTING
b1 = Lightbulb(0,'CARRY')
b2 = Lightbulb(0,'SUM')
adder = HalfAdder(b1, 'power', b2, 'power')
print adder.input1
print adder.input2
t1 = ToggleSwitch(adder.input1)
t2 = ToggleSwitch(adder.input2)
#########

#####AND TESTING
# b = Lightbulb()
# a2 = AND2(b,'power')
# t1 = ToggleSwitch([a2.input1])
# t2 = ToggleSwitch([a2.input2])
# a2.r1.name = 'AND R1'
# a2.r2.name = 'AND R2'
#######





######XOR TESTING
#b1 = Lightbulb(0,'BULB1')
#xnor = XNOR2(b,'power')
#t1 = ToggleSwitch(xnor.input1)
#t2 = ToggleSwitch(xnor.input2)

# xor.o2.r1.name = 'XOR OR r1' 
# xor.o2.r2.name = 'XOR OR r2'

# xor.na2.a2.r1.name = 'XOR NAND r1'
# xor.na2.a2.r2.name = 'XOR NAND r2 '
# xor.na2.i.name = 'XOR NAND i'

# xor.a2.r1.name = 'XOR AND r1'
# xor.a2.r2.name =  'XOR AND r2'

# print xor.o2.r1.name + ' connected to ' + xor.o2.r1.output.name
# print xor.o2.r2.name + ' connected to ' + xor.o2.r2.output.name

# print xor.na2.a2.r1.name + ' connected to ' + xor.na2.a2.r1.output.name
# print xor.na2.a2.r2.name + ' connected to ' + xor.na2.a2.r2.output.name
# print xor.na2.i.name + ' connected to ' + xor.na2.i.output.name

# print xor.a2.r1.name + ' connected to ' + xor.a2.r1.output.name
# print xor.a2.r2.name + ' connected to ' + xor.a2.r2.output.name
#############
Switchboard.assignKeys()
