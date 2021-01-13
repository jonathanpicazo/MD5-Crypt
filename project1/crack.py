#team20:$1$4fTgjp6q$QhqtcnMK1gPnk0uN3CsyL/:16653:0:99999:7:::
from itertools import combinations
from itertools import permutations
import hashlib
import string

#TODO: start combinations

def combo():
    possible = string.ascii_lowercase
    #print(possible)
    for i in range(1,6):
        comb_iter = combinations(possible, i)
        str = [''.join(citer) for citer in permutations(possible,i)] 
        print(str)






if __name__ == "__main__":
    #main function
    combo()