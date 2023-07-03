#Either is passed the output in 1D array form, or reads it from a text file
import brianInputRead




class BrianVerifier: #prompt is orignal set of clauses, verify is output made by heuristic
    def __init__(self, promptFile, verifyFile):
        self.promptFile = promptFile
        self.verifyFile = verifyFile
        self.promptSetup()
        self.readVerifyOutput()
        

    def promptSetup(self):
        originalInputReader = open(self.promptFile)
        originalInputReader.readline()
        self.promptLines = originalInputReader.readlines()
        self.numClauses = len(self.promptLines)


    def readVerifyOutput(self):
        heuristicOutput = open(self.verifyFile)
        self.verifyOutput =  heuristicOutput.readlines() #returns array form of output
        
    def verify(self):
        #promptLines is all lines from prompt file
        #verifyOutput is array of strings to verify, with 0 index being number of clauses claimed, and all others corresponding to true/false for variables
        sumClausesValid = 0

        for x in self.promptLines:
            line = x.split(" ")
            if int(line[0]) < 0:
                if int(self.verifyOutput[abs(int(line[0]))]) == 0:
                    sumClausesValid += 1
                    continue #questonabl whether it sends to right location
            else:
                if int(self.verifyOutput[abs(int(line[0]))]) == 1:
                    sumClausesValid += 1
                    continue 

            if int(line[1]) < 0:
                if int(self.verifyOutput[abs(int(line[1]))]) == 0:
                    sumClausesValid += 1
                    continue
            else:
                if int(self.verifyOutput[abs(int(line[1]))]) == 1:
                    sumClausesValid += 1
                    continue
        
        if sumClausesValid == int(self.verifyOutput[0]):
            return True, sumClausesValid, self.numClauses
        else: 
            return False, sumClausesValid, self.numClauses


