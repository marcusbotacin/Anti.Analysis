 # Implemented by Vitor Falcão da Rocha

class GarbageBytes:

    def __init__(self):

        self.found_push = False
        self.found_push_cycle = -1

        self.found_xor = False
        self.found_xor_cycle = -1

        self.found_stc = False
        self.found_stc_cycle = -1

        self.found_clc = False
        self.found_clc_cycle = -1

        self.cycle_counter = 0

    def check(self, section, address, instruction, op1, op2):

        self.cycle_counter += 1

        if instruction == 'push':
            self.found_push = True
            self.found_push_cycle = self.cycle_counter
        elif instruction == 'xor' and op1 == op2:
            self.found_xor = True
            self.found_xor_cycle = self.cycle_counter
        elif instruction == 'stc':
            self.found_stc = True
            self.found_stc_cycle = self.cycle_counter
        elif instruction == 'clc':
            self.found_clc = True
            self.found_clc_cycle = self.cycle_counter

        if self.found_push and instruction == 'ret' and self.cycle_counter == self.found_push_cycle + 1:
            self.clear()
            print "\"GarbageBytes\" Detected! Section: <%s> Address: 0x%s" % (section, address)
        elif self.found_xor and instruction == 'jnz' and self.cycle_counter == self.found_xor_cycle + 1:
            self.clear()
            print "\"GarbageBytes\" Detected! Section: <%s> Address: 0x%s" % (section, address)
        elif self.found_stc and (instruction == 'jnc' or instruction == 'jae') and self.cycle_counter == \
                        self.found_stc_cycle + 1:
            self.clear()
            print "\"GarbageBytes\" Detected! Section: <%s> Address: 0x%s" % (section, address)
        elif self.found_clc and (instruction == 'jc' or instruction == 'jb') and self.cycle_counter == \
                        self.found_clc_cycle + 1:
            self.clear()
            print "\"GarbageBytes\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_push = False
        self.found_push_cycle = -1

        self.found_xor = False
        self.found_xor_cycle = -1

        self.found_stc = False
        self.found_stc_cycle = -1

        self.found_clc = False
        self.found_clc_cycle = -1

        self.cycle_counter = 0
