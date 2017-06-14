  # Implemented by Vitor Falcão da Rocha

class VMWareINInstruction:

    def __init__(self):
        return

    def check(self, section, address, instruction, op1, op2):

        if instruction == 'in' and ('vx' in op1.lower() or 'vx' in op2.lower()):
            print "\"VMWareINInstruction\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):
        return
