 # Implemented by Marcus Botacin, based on Vitor Falcão da Rocha's implementation.

class PushPopMath:

    def __init__(self):

        self.found_push = False
        self.found_pop = False
        self.found_op = None
        self.found_comp = False

    def check(self, section, address, instruction, op1, op2):

        if 'push' in instruction and not op1 in ['ax','bx','cx','dx']:
            self.found_push=True
        elif 'pop' in instruction and not 'popf' in instruction and self.found_pop==False:
            self.found_pop=True
            self.found_op=op1
        elif self.found_pop==True and instruction in ['and', 'or','xor']:
            if self.found_op in op1 or self.found_op in op2:
                self.found_comp=True
        else:
            self.clear()

        if self.found_comp==True:
            self.clear()
            print "\"PushPopMath\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_push = False
        self.found_pop = False
        self.found_op = None
        self.found_comp = False
