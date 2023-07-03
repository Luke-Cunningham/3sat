#from re import M
from turtle import st

from numpy import var
import brianInputRead
#import brianverifier
import time

#O(n^2) approach (I think)

#call input reader, which creates 2d matrix of clauses as rows and inputs as columns

#set out vector to all zeros, when decision made, 1 is true, -1 is false

#iterate through each column of matrix, determining which column has largest effect (absolute value, delta, maybe smallest effect even)

#set output vector to 1 or -1 for input

#output, run verifier on output


def runHeuristic(fileName): #returns number of clauses met

    #fileName = 'input1.txt'
    reader = brianInputRead.AlgoBowlInputReader(fileName)

    clausesMatrix = reader.parseInFile()

    numVars = len(clausesMatrix[0])
    numClauses = len(clausesMatrix)

    outVector = [-1 for x in range(numVars)]
    numClausesMet = 0
    startTime = time.perf_counter()
    runFinalSimpleAlgo = False

    for idx in range(numVars):
        if idx % 50 == 0:
            print(str(idx) + " " + str(numClauses - numClausesMet))
        
        varNetImpact = []
        for i in range(numVars): #sum over column method to decide, generate output then pass to verifier which returns numClauses met
            sumVarOverClauses = 0
            if outVector[i] != -1:
                varNetImpact.append(0)
                continue
            for j in range(numClauses-numClausesMet): #iterates over rows
                sumVarOverClauses += clausesMatrix[j][i]
            varNetImpact.append(sumVarOverClauses) # varNetImpact holds amount that each clause would impact number of true values, decide which variable to set by abs value

        for x in range(numVars):
            if outVector[x] == -1:
                maxAbsVarImpact = abs(varNetImpact[x])
                maxAbsIndex = x
                break

        
        for x in enumerate(varNetImpact):
            if abs(x[1]) > maxAbsVarImpact:
                maxAbsIndex = x[0]
                maxAbsVarImpact = abs(x[1])
        if varNetImpact[maxAbsIndex] < 0: # outVector is set for this variable, now must update clauses matrix to be all zeros for places where clause is satisfied by value at maxAbsIndex
            outVector[maxAbsIndex] = 0
            numPopped = 0
            for x in range(len(clausesMatrix)):
                if clausesMatrix[x-numPopped][maxAbsIndex] == -1:
                    #clausesMatrix[x] = [0 for i in range(numVars)] #this clause already satisfied, no need to consider it in future
                    clausesMatrix.pop(x-numPopped)
                    numClausesMet +=1
                    numPopped +=1
        else: 
            outVector[maxAbsIndex] = 1 
            numPopped = 0
            for x in range(len(clausesMatrix)):
                if clausesMatrix[x-numPopped][maxAbsIndex] == 1:
                    #clausesMatrix[x] = [0 for i in range(numVars)] #this clause already satisfied, no need to consider it in future
                    clausesMatrix.pop(x-numPopped)
                    numClausesMet +=1
                    numPopped +=1
        timeNow = time.perf_counter()          
        if timeNow - startTime > 1400:
            runFinalSimpleAlgo = True
            break
    if runFinalSimpleAlgo:
        varNetImpact = []
        for i in range(numVars): #sum over column method to decide, generate output then pass to verifier which returns numClauses met
            sumVarOverClauses = 0
            if outVector[i] != -1:
                varNetImpact.append(0)
                continue
            for j in range(numClauses-numClausesMet): #iterates over rows
                sumVarOverClauses += clausesMatrix[j][i]
            varNetImpact.append(sumVarOverClauses) # varNetImpact holds amount that each clause would impact number of true values, decide which variable to set by abs value
        #similar to before, find net impact
        for i in range(numVars):
            if outVector[i] == -1:
                if varNetImpact[i] < 0:
                    outVector[i] = 0
                    
                    for x in range(len(clausesMatrix)):
                        if clausesMatrix[x][i] == -1:
                            clausesMatrix[x] = [0 for j in range(numVars)] #this clause already satisfied, no need to consider it in future
                            #clausesMatrix.pop(x-numPopped)
                            numClausesMet +=1
                            
                if varNetImpact[i] >= 0:
                    outVector[i] = 1
                    
                    for x in range(len(clausesMatrix)):
                        if clausesMatrix[x][i] == 1:
                            clausesMatrix[x] = [0 for j in range(numVars)] #this clause already satisfied, no need to consider it in future
                            #clausesMatrix.pop(x-numPopped)
                            numClausesMet +=1
                            
    writeTo = open("OUT" + fileName[:-4] + 'OUT.txt', 'w')
    strOutVector = [str(x) + '\n' for x in outVector]
    strOutVector = [str(numClausesMet) + '\n'] + strOutVector.copy()
    strOutVector[len(strOutVector)-1] = strOutVector[len(strOutVector)-1][:-1]

    writeTo.writelines(strOutVector)
    return numClausesMet, numClauses, numVars
