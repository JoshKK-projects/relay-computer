b = Lightbulb()
#####AND TESTING
# a2 = AND2(b,'power')
# t1 = ToggleSwitch([a2.input1])
# t2 = ToggleSwitch([a2.input2])
# a2.r1.name = 'AND R1'
# a2.r2.name = 'AND R2'
#######





######XOR TESTING
xnor = XNOR2(b,'power')
t1 = ToggleSwitch(xnor.input1)
t2 = ToggleSwitch(xnor.input2)

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
##############
Switchboard.assignKeys()
