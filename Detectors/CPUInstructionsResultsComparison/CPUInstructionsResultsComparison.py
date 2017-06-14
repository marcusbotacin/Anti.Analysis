 # Implemented by Vitor Falcão da Rocha

class CPUInstructionsResultsComparison:

    def __init__(self):
        return

    def check(self, section, address, instruction, op1, op2):

        if instruction.lower() in ['sidt', 'sldt', 'sgdt', 'str']:
            print "\"CPUInstructionsResultsComparison\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):
        return
