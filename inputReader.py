#input reader for my approach

class AlgoBowlInputReader:

    def __init__(self, inFileName):
        self.inFileName = inFileName

    def parseInFile(self):
        inFile = open(self.inFileName)
        line1 = str(inFile.readline()).split(" ")
        numClauses = int(line1[0])
        numVars = int(line1[1])

        clausesMatrix = [[0 for x in range(numVars)] for y in range(numClauses)] #instantiates array of all zeros

        fileLines = inFile.readlines()

        for x in enumerate(fileLines):
            idx = x[0]
            line = x[1].split(" ")
            clausesMatrix[idx][abs(int(line[0]))-1] = int(line[0])/abs(int(line[0]))
            clausesMatrix[idx][abs(int(line[1]))-1] = int(line[1])/abs(int(line[1]))
    
        return clausesMatrix


