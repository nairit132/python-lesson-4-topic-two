lower = int(input("Enter your lower range number"))
upper = int(input("Enter your upper range number"))
print("Prime number/s between ", lower ,"and ", upper , "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0 :
                break
        else:
                print (num)