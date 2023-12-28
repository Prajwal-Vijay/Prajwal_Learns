import math

cases = int(input("Test Cases"))
max_count = 0
for i in range(cases):
    n = int(input())
    count = 0
    limit = 0
    if (n > 100000):
        limit = int(math.log2(n))
    else:
        limit = n
    for j in range(2,limit): #Notice you do not need to iterate j across all the values 1 < j < n, its better to take it to log(n), so time complexity is O(ln(n))
        if(n % j == 0 and n % (j-1) == 0) :
            count+=1
        else:
            if max_count <= count:
                max_count = count
            count = 0
    print(max_count + 1)
    max_count=0