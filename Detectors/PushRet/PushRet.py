 # Implemented by Marcus Botacin, based on Vitor Falcão da Rocha's implementation.

class PushRet:

    def __init__(self):

        self.found_push = False
        self.found_ret = False

    def check(self, section, address, instruction, op1, op2):

        if 'push' in instruction:
            self.found_push=True
        elif self.found_push==True and 'ret' in instruction:
            self.found_ret=True
        else:
            self.found_push=False

        if self.found_ret:
            self.clear()
            print "\"PushRet\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_push = False
        self.found_ret = False
