
#file = open("/Users/havoc/Downloads/test.txt","r")
file = open("/Users/havoc/Downloads/base64-to-hex-from-hex-to-decimal.txt","r")
wfile = open("/Users/havoc/Downloads/updated4.txt","w")

firstLine = file.readline()
numbers = firstLine.split() # same as firstLine.split(" ")

#A = list(input('Enter your input:\n'))
#B = ''

A = numbers
B = ''

# for testing
# 79 41 35 42 31 71 6e 46 6d 63 48 34 70 38 37 46 32 6a 73 4a 2f 34 48 34 70 6c 34 0a 46 6c 44 73 4a 2f 34 48 34 70 6c 34 62 74 61 6e 46 6d 4c 69 69 55
#print(B)

for E in range(len(A)):
    print("aE is :" + str(A[E]))
    if A[E] == str(0):
        print("Hi there")
        A[E] = str(0)
        continue
    F = E % 2
    #print("F is : " + str(F))
    if F == 0:  # 0, 3, 6, 9, 12, 15, 18, 21, 24
        x =  A[E]
        A[E] = str(int(x) + 1)
        x = ''
    elif F == 1:  # F == 2 so 2, 5, 8, 11, 14, 17, 20, 23
        x =  A[E]
        A[E] = str(int(x) - 1)
        x = ''

# join it all together into one
#B = ''.join(B)
A = ' '.join(A)

print(B)
print(A)
wfile.write(A)
wfile.close()

# ord() function returns the Unicode code from a given character.
# returns the character that represents the specific unicode
