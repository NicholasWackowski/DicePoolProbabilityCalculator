# Nicholas Wackowski, 7/6/2020
# A program to calculate the likelihood of rolling x successes of P(x) chance given y events

# --- Below function was taken from StackOverflow user dheerosaur and l3viathan ---
# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python

# Call the function as "of n possible choices, choose r"
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

# --- End of code taken from StackOverflow

# Iterates through all possible number of successes and sums their likelihoods,
# thereby returning the total chance the dice will hit the target number of
# successes OR greater.
# numTrials = int, how many dice/opportunities for success there are
# difficulty = int, the minimum number which must be rolled (out of 10) for success
# numSuccesses = int, the minimum number of successes desired
def totalProb(numTrials, difficulty, numSuccesses):
    probSuccess = calculateProbSuccess(difficulty)
    total = 0
    for x in range(numSuccesses, numTrials+1):
        total += calcProbability(numTrials, probSuccess, x)
    return total

# Calculates the percent chance of success based on how many dice are being
# rolled and how likely each die is to be successful
# numTrials = int, how many dice/opportunities for success there are
# probSuccess = float, percent chance of success
# numSuccesses = int, the minimum number of successes desired
def calcProbability(numTrials, probSuccess, numSuccesses):
    return ( ncr(numTrials, numSuccesses) * (probSuccess**numSuccesses) 
            * ((1-probSuccess)**(numTrials-numSuccesses)) )

# Calculates the percent chance of success
# difficulty = int, a number from 1-10. Minimum number which needs to be rolled for success.
def calculateProbSuccess(difficulty):
    return 1 - (difficulty-1)/10

def main():
    dicePool = 5
    difficulty = 6
    numSuccesses = 3

    probability = totalProb(numTrials=dicePool, difficulty=difficulty, numSuccesses=numSuccesses)
    print(probability)
main()