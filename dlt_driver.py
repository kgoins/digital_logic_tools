import sys

import dlt_functions
# import argparse

def Menu():
    print("Digital logic tools\nSelect function:")
    print("""
    1. Generate Truth Table
    2. Calculate 2s Compliment
    3. Convert to IEEE Float
    Exit: quit program
          """)
    function =  raw_input("Choose function:")

    return function


def callFunction(function):
    if function is int:
        if function == 1:
            arguments = raw_input()
            genTruthTable(arguments)
    elif function == "Exit":
        sys.exit(0)
    else:
        print("Invalid option")


def driver(argv = None):
    if argv is None:
        while True:
            callFunction( Menu() )
    # else:
        # parse args, callFunction, and return

if __name__ == '__main__':
    driver()
