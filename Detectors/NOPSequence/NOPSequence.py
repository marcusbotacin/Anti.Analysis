  # Implemented by Vitor Falcão da Rocha

class NOPSequence:

    def __init__(self):

        self.counter = 0

    def check(self, section, address, instruction, op1, op2):

        if instruction == 'nop':

            self.counter += 1

            if self.counter is 5:
                self.counter = 0
                print "\"NOPSequence\" Detected! Section: <%s> Address: 0x%s" % (section, address)
        else:
            self.counter = 0

    def clear(self):

        self.counter = 0
