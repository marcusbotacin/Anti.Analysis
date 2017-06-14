 # Implemented by Vitor Falcão da Rocha

class FakeConditionalJumps:

    def __init__(self):

        self.found_xor = False
        self.xor_cycle = 0

        self.found_stc = False
        self.stc_cycle = 0

        self.found_clc = False
        self.clc_cycle = 0

        self.cycle_count = 0

    def check(self, section, address, instruction, op1, op2):

        self.cycle_count += 1

        if instruction == 'xor' and op1 == op2:
            self.found_xor = True
            self.xor_cycle = self.cycle_count
            return
        elif instruction == 'stc':
            self.found_stc = True
            self.stc_cycle = self.cycle_count
            return
        elif instruction == 'clc':
            self.found_clc = True
            self.clc_cycle = self.cycle_count
            return

        if (instruction == 'jnz' or instruction == 'jne') and self.found_xor and self.cycle_count == self.xor_cycle + 1:
            self.clear()
            print "\"FakeConditionalJumps\" Detected! Section: <%s> Address: 0x%s" % (section, address)
        elif (instruction == 'jnc' or instruction == 'jae') and self.found_stc and self.cycle_count == self.stc_cycle + 1:
            self.clear()
            print "\"FakeConditionalJumps\" Detected! Section: <%s> Address: 0x%s" % (section, address)
        elif (instruction == 'jc' or instruction == 'jb') and self.found_clc and self.cycle_count == self.clc_cycle + 1:
            self.clear()
            print "\"FakeConditionalJumps\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_xor = False
        self.xor_cycle = 0

        self.found_stc = False
        self.stc_cycle = 0

        self.found_clc = False
        self.clc_cycle = 0

        self.cycle_count = 0
