#team20:$1$4fTgjp6q$QhqtcnMK1gPnk0uN3CsyL/:16653:0:99999:7:::
from itertools import product
import hashlib
import string

gpassword = "zhgnnd"
gsalt = 'hfT7jp2q'

def to64(v, n):
    base64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(1, n + 1):
        ret += base64[v & 0x3f]
        v >>= 6
    return ret

def md5crypt():
    global gpassword, gsalt
    password = gpassword.encode('ascii')
    salt = gsalt.encode('ascii')
    magic = '$1$'.encode('ascii')
    res = password + magic + salt
    h = hashlib.md5(password + salt + password).digest()
    l = len(password)

    while l > 0:
        res += h[0:min(16,l)]
        l -= 16
    
    i = len(password)
    while i != 0:
        if i & 1:
            res += chr(0).encode("ascii")
        else:
            res += password[0:1]
        i >>= 1
    
    h = hashlib.md5(res).digest()
    i = 0
    # setting range from 999 to 1000 fixed the matching hash issue
    for i in range(0,1000):
        tmp = b''
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

    
    print('wPwz7GC6xLt9eQZ9eJkaq.')

    answer = to64((h[0] << 16) | (h[6] << 8) | (h[12]), 4) +to64((h[1] << 16) | (h[7] << 8) | (h[13]), 4) + to64((h[2] << 16) | (h[8] << 8) | (h[14]), 4) +to64((h[3] << 16) | (h[9] << 8) | (h[15]), 4) + to64((h[4] << 16) | (h[10] << 8) | (h[5]), 4) +to64(h[11], 2)

    print (answer)



def getPermutations():
    desired = input('Enter desired string to find with combo: ')
    # returns a list of all the possible permutations with lowercase letters equal to 6 characters
    # reverse ascii to make the cracking slightly faster, doubt the password will start with a letter that comes early in the alphabet

    possible = string.ascii_lowercase[::-1]
    for citer in product(possible,repeat = 6):
        temp = ''.join(citer)
        print(temp)




if __name__ == "__main__":
    #main function
    # passProvided = input("Input password\n")
    # saltProvided = input("Input salt\n")
    #getPermutations()
    md5crypt()