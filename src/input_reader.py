import sys

class Reader:
    def __init__(self, levelOfComplexity):
        self.levelOfComplexity = int(levelOfComplexity)

    def readInput(self):
        lines = list[str]

        with open("..\input\SD-" + str(self.levelOfComplexity) + ".txt", "r") as f:
            lines = f.readlines()

        length = int(lines[1])
        seed = int(lines[3])
        targetWeight = int(lines[5])
        matrix = []

        # iterate over matrix rows
        for x in range(7,int(7+(length/2))):
            row = []
            currentRow = lines[x]
            # read a single row
            for i in range(0,int(length/2)):
                row.append(currentRow[i])
            
            # append row to matrix
            matrix.append(row)
        
        syndrome = lines[8 + int(length/2)]

        print(length)
        print(seed)
        print(targetWeight)
        print(matrix)
        print(syndrome)
