#!/usr/bin/env python

# Implemented by Vitor Falcão da Rocha

from sys import argv, path
from os import listdir, getcwd
from os.path import isfile, join

from disassembler import Disassembler


class Analyzer:

    def __init__(self, n):  # n -> Max number of instructions

        self.detectors = []
        self.import_detectors()
        self.max_number_of_instructions = n
        self.number_of_instructions_counter = 0

    def evasion_detector(self, section, address, instruction, op1, op2):

        self.number_of_instructions_counter += 1

        if self.number_of_instructions_counter < self.max_number_of_instructions:
            for detector in self.detectors:
                detector.check(section, address, instruction, op1, op2)
        else:
            for detector in self.detectors:
                detector.clear()

    def import_detectors(self):

        detectors = [f for f in listdir('Detectors') if not isfile(join('Detectors', f))]
        for detector in detectors:
            path.append(getcwd() + '/Detectors/' + '/' + detector)
            module = __import__(detector)
            detector = getattr(module, detector)
            self.detectors.append(detector())  # Here we save an actual instance of the class


def main():

    if len(argv) < 3:
        print "Usage : %s <number of instrucitons> <filename>" % argv[0]
        return

    analyzer = Analyzer(argv[1])

    da = Disassembler()
    da.disassemble(analyzer, argv[2])

if __name__ == "__main__":
    try:
        main()
    except Exception, err:
        #print_exc()
        print "Exception : %s" % err
