#team20:$1$4fTgjp6q$QhqtcnMK1gPnk0uN3CsyL/:16653:0:99999:7:::
from itertools import product
from time import process_time
import hashlib
import string

def to64(v, n):
    base64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(1, n + 1):
        ret += base64[v & 0x3f]
        v >>= 6
    return ret

def md5crypt(desiredPass, givenSalt):
    password = desiredPass.encode('ascii')
    salt = givenSalt.encode('ascii')
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
    # setting range from 999 to 1000 fixed the matching hash issue
    i = 0
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

    return to64((h[0] << 16) | (h[6] << 8) | (h[12]), 4) +to64((h[1] << 16) | (h[7] << 8) | (h[13]), 4) + to64((h[2] << 16) | (h[8] << 8) | (h[14]), 4) +to64((h[3] << 16) | (h[9] << 8) | (h[15]), 4) + to64((h[4] << 16) | (h[10] << 8) | (h[5]), 4) +to64(h[11], 2)


if __name__ == "__main__":
    
    salt = '4fTgjp6q'
    hashed = 'QhqtcnMK1gPnk0uN3CsyL/'
    tested = 0
    total = 0
    start = process_time()

    possible = string.ascii_lowercase
    for citer in product(possible,repeat = 6):
        if hashed == md5crypt(''.join(citer), salt):
            print('The password is: ' + ''.join(citer))
            print('Finished at: ' + str(total) + ' seconds.')
            quit()
        else:
            current = process_time()
            if (current - start) > 1:
                print(str(tested) + ' tested at ' + str(current) + ' seconds.')
                start = process_time()
                tested = 0
            tested += 1
            total += 1
    print('No matching hash found')
