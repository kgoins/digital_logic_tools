import itertools

def genTruthTable(number, format):
    charTable = []
    if format == "bin":
        charTable = [0, 1]

    elif format == "char":
        charTable = ['F', 'T']

    # itertools.product returns the cartesian product of charTables
    table = list( itertools.product(charTable, repeat=number) )
    print table

    return table

# function test
if __name__ == '__main__':
    genTruthTable(3, "bin")
