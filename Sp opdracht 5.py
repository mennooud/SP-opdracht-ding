a = [ 0, 2, 6, 3, 10, 6, 21, 93, 5]

def sorteren(lst):
    a = len(lst)
    for i in range(a):
        for j in range(a - i - 1):
            h = lst[j]-lst[j+1]
            if h > 0:
                g = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = g
    return lst
print(sorteren(a))