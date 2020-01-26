#less time cumborsome

print("prime\t\tnot-prime\n")
print(0)
print(1)
for num in range(2,100):
    x=0
    if num > 11:
        for i in range(2,9):
            if num%i==0:
        #if (0==num%int(x) for x in range(2,9)):
                x=1
                break
            else:
                pass
        if x==1:
            print("\t\t{0}".format(num))
        else:
            #print("{0}".format(num))
            print(num)
    else:
        for i in range(2,num):
            if num%i==0:
                x=1
                break
            else:
                pass
        if x==1:
            print("\t\t{0}".format(num))
        else:
            print(num)
