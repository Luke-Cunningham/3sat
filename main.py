import random
import time
import random

from brianverifier import BrianVerifier


class Clause:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.keys = (a, b)

    def key(self, val):
        return abs(self.a) == val or abs(self.b) == val

    def eval(self, one, two):
        if abs(self.a) == one:
            return one == self.a or two == self.b
        else:
            return one == self.b or two == self.a

    def __str__(self):
        return f"({self.a},{self.b})"

    def positive_key(self, key):
        if abs(self.a) == key:
            return self.a > 0
        if abs(self.b) == key:
            return self.b > 0
        return "ERROR"

    def eval_from_dict(self, dictionary):
        return bool(dictionary[abs(self.a)] == self.a or dictionary[abs(self.b)] == self.b)

    def return_other_key(self, key):
        if self.a == key:
            return self.b
        if self.b == key:
            return self.a


class AlgoBowl:
    def __init__(self):
        self.variables = {}
        self.num_clauses = 0
        self.clauses = []

    def read_in_input(self):
        with open("input.txt", encoding='utf-8') as f:
            inpt = f.readlines()
        clause_vars = inpt[0].split(" ")
        self.num_clauses = int(clause_vars[0])
        for i in range(1, int(clause_vars[1]) + 1):
            self.variables[i] = 0
        for line in range(1, len(inpt)):
            a, b = tuple(inpt[line].strip('\n').split(" "))
            self.clauses.append(Clause(int(a), int(b)))

    # generates data using maximum input sizes
    def randomly_gen_inputs(self):
        clause_count = 500
        variable_count = 100
        file_data = []
        for x in range(1, clause_count + 1):
            clause = []
            for y in range(1, variable_count + 1):
                if random.random() < 0.5:
                    clause.append(y)
                else:
                    clause.append(-y)
            file_data.append(clause)
        return file_data, clause_count, variable_count

    def verifier(self):
        variables = {}
        with open("output.txt", encoding='utf-8') as f:
            inpt = f.readlines()
        correct = int(inpt[0])
        for line in range(1, len(inpt)):
            variables[line] = int(inpt[line].strip('\n')) * line
        for clause in self.clauses:
            correct -= clause.eval_from_dict(variables)
        return correct == 0

    def heuristic(self):
        return

    # ed AI code template
    def simulated_annealing(self):
        return
        # initialize current to starting state
        # for i to infinity
        # if T(i) = 0
        # return current
        # next = random successor of current
        # delta = value(next) - value(current)
        # if delta > 0
        # current = next
        # else
        # current = next w/ probability exp( delta/T(i) )

    # Cover cases that don't have high rate of both all pos / neg
    def all_pos_or_neg_heuristic(self, data, c_count, v_count):
        majority_pos_count = 0
        all_neg_count = 0
        all_pos_count = 0
        for c in range(c_count):
            clause_sum = 0
            variable_indexes_sum = 0
            for v in range(v_count):
                clause_sum += (data[c][v] / (v + 1))
                variable_indexes_sum += v
            if clause_sum >= 0:
                majority_pos_count += 1
            if clause_sum == v_count:
                all_pos_count += 1
            if clause_sum == -v_count:
                all_neg_count += 1

        print("The percentage of clauses with more non-negated variables than negated to overall clauses is: %1.5f" %
              (majority_pos_count / c_count))
        print("Number of clauses that consisted of all negated variables: %4d" % all_neg_count)
        print("Number of clauses that contained no negated variables: %4d" % all_pos_count)

        if min(all_neg_count, all_pos_count) == 0:
            return 1
        else:
            return (c_count - min(all_neg_count, all_pos_count)) / c_count

    def output(self):
        satisfied = 0
        for clause in self.clauses:
            satisfied += clause.eval_from_dict(self.variables)
        with open("output.txt", "w+", encoding='utf-8') as f:
            f.write(str(satisfied) + "\n")
            for variables in self.variables.keys():
                f.write(str(int(self.variables[variables] // variables)) + "\n")


def main():
    verifier = BrianVerifier('inputs/input.txt', 'inputs/output_from_466_to_443.txt')
    print(verifier.verify())
    verifier.promptSetup()
    verifier.readVerifyOutput()


if __name__ == "__main__":
    main()
