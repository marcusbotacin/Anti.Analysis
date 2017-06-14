  # Implemented by Vitor Falcão da Rocha

class IsDebuggerPresent:

    def __init__(self):

        self.found_op1 = None
        self.found_keyword = False

    def check(self, section, address, instruction, op1, op2):

        if instruction in ['mov', 'movsx', 'movzx'] and 'fs:0x30' in op2:
            self.found_op1 = op1
            self.found_keyword = True
            return

        if self.found_keyword:
            if instruction in ['mov', 'movsx', 'movzx']:

                substring = '[' + self.found_op1 + '+0x2]'

                if substring in op1 or substring in op2:
                    self.clear()
                    print "\"IsDebbugerPresent\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_op1 = None
        self.found_keyword = False
