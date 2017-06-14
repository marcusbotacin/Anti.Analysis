 # Implemented by Marcus Botacin, based on Vitor Falcão da Rocha's implementation.

class SoftwareBreakpoint:

    def __init__(self):

        self.found_cmp = False

    def check(self, section, address, instruction, op1, op2):

        if 'cmp' in instruction:
            if '0xcc' in op1 or '0xcc' in op2:
                self.found_cmp = True

        if self.found_cmp==True:
            self.clear()
            print "\"Software Breakpoint\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_cmp = False
