#team20:$1$4fTgjp6q$QhqtcnMK1gPnk0uN3CsyL/:16653:0:99999:7:::
from itertools import combinations
import hashlib
import string


def getPermutations():

    desired = input('Enter desired string to find with combo: ')
    sz = len(desired)
    # returns a list of all the possible permutations with lowercase letters that are less than or equal to 6 characters
    possible = string.ascii_lowercase
    comb_str =[]
    for i in range(1,int(sz) + 1):
        for citer in combinations(possible,i):
            temp = ''.join(citer)
            if desired == temp:
                print('found: ' + desired)
                return
            comb_str.append(temp)
            print(temp)
        possible += string.ascii_lowercase
    print('did not find wanted string')
    




if __name__ == "__main__":
    #main function
    getPermutations()