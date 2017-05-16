# main body of functional program
#
# String Parse -- parse.py
#
# created: 2017.05.15
# 2017.05.15 -- last edited
#
# ::Functional process description::
# Get input from String[]
# Foreach s in S[]
#   Identify Data Type
#   print line with type and val
# return
# END # exit code 0
#
import sys, msvcrt, getopt, fileinput, re


class AppError:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return `self.value`


def FatalError(message):
    print message, "\nPress any key."
    msvcrt.getch()
    Usage()


def Usage():
    sys.exit("Required Parameter:\n"
             "\t decimal integer (e.g., 65536)")


def main():
    try:
        (options, arguments) = getopt.getopt(sys.argv[1:], '')
    except getopt.error:
        FatalError("Unknown input parameter.")

    if [] == arguments:
        Usage()
    try:
        inpValInDec = int(sys.argv[1])
        print ("0x%X" % (inpValInDec))
    except AppError, exc:
        FatalError(exc)


if __name__ == '__main__':
    main()


