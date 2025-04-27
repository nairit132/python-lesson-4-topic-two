string = input("please put in your word")
char = input("please enter your own character")
i = 0 
count = 0
while(i < len(string)):
    if(string [i] == char):
        count = count + 1
    i = i + 1
print("The total number of times ", char , "as occoured is ", count)