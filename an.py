finalList = [0, 0, 9, 180, 2619, 33570, 402129, 4619160, 51572439, 564151950, 6077367549, 64696307940, 682266771459, 7140400943130, 74263608488169]

def compute(ord, pr):
    return (pr + 11 * 10**(ord - 3))*9 + (10**(ord - 3) - 1)

#print(compute(3, 9))
#print(compute(2, 0))
#print(compute(4, 180))


def rc(ord):
    if ord == 1:
        return 0
    return int((rc(ord - 1) + 11 * 10**(ord - 3))*9 + (10**(ord - 3) - 1))

def rc1(ord):
    if ord == 1:
        return 0
    return int(9 * rc1(ord - 1) + 10**(ord - 1) - 1)

out = []
for i in range(13):
    print(i, rc(i) == rc1(i), rc(i), rc1(i))
    out.append(rc1(i))
    
print(out)

