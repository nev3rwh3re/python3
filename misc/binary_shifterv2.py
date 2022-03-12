
storage = list()
counter = 0
debug = 0
outfile = open("/Users/havoc/Downloads/apt/modifiedv2", "wb")
with open("/Users/havoc/Downloads/apt/out", "rb") as f:
    x = 0
    while (two_byte := f.read(2)):
        if debug: x = x + 1
        if debug: print("1")
        if debug: print(two_byte)
        if debug: print(two_byte.hex())
        if debug: print("2")
        if debug: print(bytes([c for t in zip(two_byte[1::2], two_byte[::2]) for c in t]))
        new_bytes = bytes([c for t in zip(two_byte[1::2], two_byte[::2]) for c in t])
        if debug: print("3")
        if debug: print(new_bytes)
        if debug: print(new_bytes.hex())
        storage.append(new_bytes.hex())
        if debug: print("4")
        if debug: print(storage)
        if debug:
            if x > 10:
                break

A = ''.join(storage)

if debug: print(A)
if debug: print(type(A))
f.close()
outfile.write(A.encode('utf_8'))
outfile.close()