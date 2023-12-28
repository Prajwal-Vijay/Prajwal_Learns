pos = input()
count = 0
max_count = 0
for i in range(0,len(pos)):
    if pos[i] == pos[i-1]:
        count+=1
    else:
        count = 0
    if max_count <= count:
        max_count = count
if (max_count+1) >= 7:
    print("Dangerous")
else:
    print("Not Dangerous")
