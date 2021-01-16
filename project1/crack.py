#team20:$1$4fTgjp6q$QhqtcnMK1gPnk0uN3CsyL/:16653:0:99999:7:::
from itertools import combinations
import hashlib
import string

gpassword = "zhgnnd"
gsalt = 'hfT7jp2q'

def to64(v, n):
    base64 = '/0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(1, n):
        ret += base64[v & 0x3f]
        v >>= 6
    return ret

#TODO: finalization function

def md5crypt():
    global gpassword, gsalt
    password = gpassword.encode("ascii")
    salt = gsalt.encode("ascii")
    magic = "$1$".encode("ascii")
    res = password + magic + salt
    h = hashlib.md5(password + salt + password).digest()
    l = len(password)
    print(h)

    while l > 0:
        # res = res + substr(h, 0, min(16, l))  
        res += h[0:min(16,l)]
        l -= 16
    
    i = len(password)
    while i != 0:
        if i & 1 == 0:
            res += chr(0).encode("ascii")
        else:
            res += password[0:1]
        i >>= 1
    
    h = hashlib.md5(res).digest()
    print(h)
    i= 0
    for i in range(0,999):
        tmp = b""
        if i % 2 != 0:
            tmp += password
        else:
            tmp += h
        if i % 3 != 0:
            tmp += salt
        if i % 7 != 0:
            tmp += password
        if i % 2 != 0:
            tmp += h
        else:
            tmp += password
    
    h = hashlib.md5(tmp).digest()

    print(h)



def getPermutations():
    desired = input('Enter desired string to find with combo: ')
    sz = len(desired)
    # returns a list of all the possible permutations with lowercase letters that are less than or equal to 6 characters
    possible = string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase
    comb_str = []
    for citer in combinations(possible,6):
        temp = ''.join(citer)
        if desired == temp:
            print('found: ' + desired)
            return
        comb_str.append(temp)
        print(temp)
    print('did not find wanted string')
    




if __name__ == "__main__":
    #main function
    passProvided = input("Input password\n")
    saltProvided = input("Input salt\n")
    md5crypt()