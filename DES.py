# Nate Kelley
# 2/8/2023

pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 
       34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 
       11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 
       23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 
       61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

pc2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]

ip = [ 58, 50, 42, 34, 26, 18, 10, 2,
       60, 52, 44, 36, 28, 20, 12, 4,
       62, 54, 46, 38, 30, 22, 14, 6,
       64, 56, 48, 40, 32, 24, 16, 8,
       57, 49, 41, 33, 25, 17, 9, 1,
       59, 51, 43, 35, 27, 19, 11, 3,
       61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

e = [ 32, 1, 2, 3, 4, 5,
      4, 5, 6, 7, 8, 9,
      8, 9, 10, 11, 12, 13,
      12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21,
      20, 21, 22, 23, 24, 25,
      24, 25, 26, 27, 28, 29,
      28, 29, 30, 31, 32, 1]


sList = [
    [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],

    [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],

    [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],

    [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],

    [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],

    [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

p = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

ipNeg = [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41, 9, 49, 17, 57, 25]

#splits input string of numbers into two halves
def partition(num):
    half = len(num) // 2
    left = num[0:half]
    right = num[half if len(num)%2 == 0 else ((half)+1):]
    return (left, right)

#shifts strings(x) by desired amounts and places the halves as a tuple in pairs list and the halves together in the full pairs list
def shift(pairs, fullPairs, x, num):
    left = pairs[x][0][num:] + pairs[x][0][0:num]
    right = pairs[x][1][num:] + pairs[x][1][0:num]
    pairs.append((left,right))
    fullPairs.append((left + right))

#uses 32 bit half data input and key to find rows and columns on each graph to create a new binary string
def encode(right, key):
    newRight = ""
    #expand right half of data using e table from 32 bits into 48 bits
    for n in e:
        newRight += right[n-1]
    #XOR data with given subkey
    result = int(newRight, 2)^int(key,2)    
    rightPlus = (bin(result)[2:].zfill(len(newRight)))
    rightPlusPlus = ""
    #split XOR'd data into 6 bit intervals
    for x in range(len(rightPlus)//6):
        y = x * 6
        #for each group of 6 take the outer 2 bits as the row number eg. 100101 = 11
        row = int((rightPlus[y:y+1] + rightPlus[y+5:y+6]),2)
        #and the inner 4 bits as the column number eg. 100101 = 0010
        col = int(rightPlus[y+1:y+5], 2)
        #then create a new binary string using output from row and columns
        rightPlusPlus += str(bin(sList[x][row][col]))[2:].zfill(4)
    
    final = ""
    #permute result with table p
    for n in p:
        final += rightPlusPlus[n-1]
    return final

#encryptes data using the DES encryption algorithm
def encrypt(message, key):
    #first use the key to create 16 subkeys
    bkey = bin(int('1'+ key, 16))[3:]
    keyPlus = ""
    #permute key for the first time with pc1

    # to permute, take first number in pc1 (57), the first bit of the new created key will
    # be the bit in place 57 of the original key. Repeat this for all of the numbers in pc1

    for n in pc1:
        keyPlus += bkey[n-1]

    halves = partition(keyPlus)

    pairs = []
    fullPairs = []

    pairs.append(halves)
    fullPairs.append(halves[0] + halves [1])
    #shift binary over either 1 or 2 times, then add them to list of binary string subkeys
    for x in range(2):
        shift(pairs, fullPairs, x, 1)
  
    for x in range(2,8):
        shift(pairs, fullPairs, x, 2)

    shift(pairs, fullPairs, 8, 1)

    for x in range(9,15):
        shift(pairs, fullPairs, x, 2)

    shift(pairs, fullPairs, 15, 1)

    keyList = []
    #permute each subkey with table pc2
    for i in fullPairs:
        newKey = ''
        for j in pc2:
            newKey += i[j-1]
        keyList.append(newKey) 
    
    #subkey list is done, encode original data
    bmessage = bin(int('1'+ message, 16))[3:]
    mPlus = ""
    #permute data with list ip
    for n in ip:
        mPlus += bmessage[n-1]

    halves = partition(mPlus)

    lh = halves[0]
    rh = halves[1]
    #encode right hand data using s-blocks 16 times, set left hand = right hand
    for x in range(16):
        temp1 = encode(rh, keyList[x+1])
        temp2 = int(temp1, 2)^int(lh,2)
        lh = rh
        rh = bin(temp2)[2:].zfill(len(temp1))
    #revers left and right hand
    rightLeft = rh + lh
    #finally permute binary with list ipNeg
    final = ""
    for n in ipNeg:
        final += rightLeft[n-1]

    final = int(final, 2)
    #output result in hexadecimal
    final = hex(final)[2:]

    print(final)

    

userMessage = input("Input a message:")
userKey = input("Input a key:")


encrypt(userMessage, userKey)