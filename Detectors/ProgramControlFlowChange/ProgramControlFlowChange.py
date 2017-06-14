  # Implemented by Vitor Falcão da Rocha

class ProgramControlFlowChange:

    def __init__(self):

        self.found = False
        self.found_cycle = 0
        self.cycle_counter = 0

    def check(self, section, address, instruction, op1, op2):

        self.cycle_counter += 1

        if instruction == 'push':
            self.found = True
            self.found_cycle = self.cycle_counter
            return

        if self.found and instruction == 'ret' and self.cycle_counter == self.found_cycle + 1:
            self.clear()
            print "\"ProgramControlFlowChange\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found = False
        self.cycle_counter = 0
        self.found_cycle=0
