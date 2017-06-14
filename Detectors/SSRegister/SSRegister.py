 # Implemented by Marcus Botacin, based on Vitor Falcão da Rocha's implementation.

class SSRegister:

    def __init__(self):

        self.found_ss = False
        self.found_flag = False

    def check(self, section, address, instruction, op1, op2):

        if instruction in ['mov', 'movsx', 'movzx']:
            if 'ss' in op1:
                self.found_ss = True
        elif instruction== 'pop':
            if 'ss' in op1:
                self.found_ss = True
        elif 'pushf' in instruction and self.found_ss==True:
            self.found_flag=True
        else:
            self.clear()

        if self.found_ss==True and self.found_flag==True:
            self.clear()
            print "\"SS Register\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_ss = False
        self.found_flag = False
