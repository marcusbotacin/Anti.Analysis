# Implemented by Marcus Botacin
# Needs to be improved

class StealthImport:

    def __init__(self):

        self.found_seh=False
        self.found_op1 = None
        self.found_handler=False
        self.found_op2 = None
        self.found_cmp = False
        self.found_pe = False
        self.found_img = False

    def check(self, section, address, instruction, op1, op2):

        if self.found_seh==False and instruction in ['mov', 'movsx', 'movzx']:
            if 'fs:0x0' in op2:
                self.found_op1 = op1
                self.found_seh = True

        elif self.found_seh==True and self.found_handler==False and instruction in ['mov', 'movsx', 'movzx']:

            if 'fs:0x30' in op2:
                self.found_seh=False
            elif self.found_op1 + '+0x4' in op2:
                self.found_handler=True
                self.found_op2 = op1

        elif self.found_handler==True and instruction in ['cmp','cmpxchg']:
            if self.found_op2 in op1:
                self.found_cmp=True

        elif self.found_cmp==True and instruction in ['mov','movsx','movzx']:
            if self.found_op2+'+0x3c' in op2:
                self.found_pe=True

        elif self.found_pe==True and instruction in ['and','or','xor','add','sub','cmp']:
            if '0x78' in op1 or '0x78' in op2:
                self.found_img=True

        if self.found_img:
            self.clear()
            print "\"StealthImport\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):
        self.found_seh=False
        self.found_op1 = None
        self.found_handler=False
        self.found_op2 = None
        self.found_cmp = False
        self.found_pe = False
        self.found_img = False

