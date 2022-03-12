

LIM = 20
#I = 1
J = 2
AMT = 0
C = 0

for I in range(LIM): # 0 - 19 (20 times)
    print("I is: " + str(I))
    if J < I:
        J = J + 1
        print("J is: " + str(J))
        C = C + 2
        print("C is: " + str(C))
        if I >= LIM:
            print("I is > LIM")
            AMT = AMT + I
            print("Hello")
print("AMT is : " + str(AMT))

