import brianheuristic
import brianverifier
import brianInputRead
import random
import timeit
import glob

summaryFile = open("summarizeResults.txt", 'a')

for fileName in glob.glob('inputs/*'):
    genTimeStart = timeit.default_timer()
    
    #with open("input.txt", "w+", encoding='utf-8') as f:
    #    f.write(f"{clauses} {variables}\n")
    #    for clause in range(clauses):
    #        stm_one = random.choice([i for i in range(-1 * variables,variables+1) if i not in [0]])
    #        stm_two = random.choice([i for i in range(-1 * variables,variables+1) if i not in [0, stm_one, -stm_one]])
    #        f.write(f"{stm_one} {stm_two}\n")
    genTimeEnd = timeit.default_timer()
    genTime = genTimeEnd - genTimeStart

    heurTimeStart = timeit.default_timer()
    fileIn = fileName

    fileOut = "OUT" + fileIn[:-4] + 'OUT.txt'

    clausesMet, numClauses, variables = brianheuristic.runHeuristic(fileIn)
    heurTimeEnd = timeit.default_timer()

    #run verifier
    heurTime = heurTimeEnd - heurTimeStart

    verifier = brianverifier.BrianVerifier(fileIn, fileOut)
    outText = fileOut[:-7] + ".txt: " + str(clausesMet) + " / " + str(numClauses) + " = " + str(clausesMet/numClauses) + " -- NumVars: " + str(variables) + ", Verified: " + str(verifier.verify()) + "\n"
    summaryFile.write(outText)
    print(outText)
    #summaryFile.write(" --- Input Gen time: " + str(genTime) + ", Heuristic Time: " + str(heurTime) + "\n")








#fileIn = 'input3.txt'

#fileOut = fileIn[:-4] + 'OUT.txt'

#brianheuristic.runHeuristic(fileIn)

#run verifier

#verifier = brianverifier.BrianVerifier(fileIn, fileOut)
#print(verifier.verify())