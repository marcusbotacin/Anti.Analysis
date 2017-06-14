  # Implemented by Vitor Falcão da Rocha

class HookDetection:

    def __init__(self):
        return

    def check(self, section, address, instruction, op1, op2):

        if instruction == 'cmp' and ('0xe9' in op1.lower() or '0xe9' in op2.lower()):
            print "\"HookDetection\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):
        return
