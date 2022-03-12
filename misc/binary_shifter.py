
storage = list()
counter = 0
debug = 0
outfile = open("/Users/havoc/Downloads/apt/modified", "wb")
with open("/Users/havoc/Downloads/apt/out", "rb") as f:
    while (byte := f.read(1)):
        if debug:
            print("1")
            print(byte)
            print(byte.hex())
            print(ord(byte))
            print("2")

        number = ord(byte)

        if number == 0:
            if debug: print("null so null")
            storage.append(hex(0))
            counter = counter + 1
            continue
        F = counter % 2
        #print("F is : " + str(F))
        if F == 0:  # 0, 3, 6, 9, 12, 15, 18, 21, 24
            if debug: print("mod 0 so +1")
            x =  number + 1
            storage.append(hex(x))
            if debug: print(hex(x))
            #x = ''
            if debug: print("byte is: " + str(number))
            counter = counter + 1
        elif F == 1:  # F == 2 so 2, 5, 8, 11, 14, 17, 20, 23
            if debug: print("mod 1 so -1")
            x =  number - 1
            storage.append(hex(x))
            if debug: print(hex(x))
            x = ''
            counter = counter + 1
            #if counter > 10: break



A = ''.join(storage)

if debug: print(A)
if debug: print(type(A))
f.close()
outfile.write(A.encode('utf_8'))
outfile.close()
