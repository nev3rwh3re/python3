
# goal is to learn how to set and use values in a multi-dimensional array

LIM = 21
#I = 1
J = 2
AMT = 0
C = 0

my_array = [[1 for i in range(21)] for j in range(21)]
# x is now a 10x10 array of 'foo' (which can depend on i and j if you want)

for I in range(LIM): # 0 - 19 (20 times)
    print("I is: " + str(I))
    my_array[I][1] = 1
    while J <= I:
        print("J is: " + str(J))
        print("array 1 is: " + str(my_array[I-1][J-1]))
        print("array 2 is: " + str(my_array[I-1][J]))
        my_array[I][J] += (my_array[I-1][J-1] + my_array[I-1][J])
        print(my_array[I][J])
        print("C is: " + str(C))
        if I >= LIM:
            print("I is > LIM")
            AMT = AMT + my_array[LIM][J]
            print("Hello")
        J = J + 1
print("AMT is : " + str(AMT))
