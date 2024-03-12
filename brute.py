n = 3

for i in range(1, 10**n):
    s = str(i)
    flag = False
    for s_i in range(len(s) - 1):
        if s[s_i] == s[s_i + 1]:
            flag = True
    
    if flag == True:
        print(i)
        c+= 1
print(c)
