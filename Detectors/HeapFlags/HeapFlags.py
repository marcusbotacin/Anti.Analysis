 # Implemented by Vitor Falcão da Rocha

class HeapFlags:

    def __init__(self):

        self.found_op = None
        self.found_first = False
        self.found_second = False

    def check(self, section, address, instruction, op1, op2):

        if op1 is not None and 'fs:0x30' in op1:
            self.found_op = op1
            self.found_first = True
            return
        elif op2 is not None and 'fs:0x30' in op2:
            self.found_op = op2
            self.found_first = True
            return

        if self.found_op is not None and ((op1 is not None and '[' + self.found_op + '+0x18]' in op1) or (op2 is not
                                                                        None and'[' + self.found_op + '+0x18]' in op2)):
            self.clear()
            print "\"HeapFlags\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_op = None
        self.found_first = False
        self.found_second = False
