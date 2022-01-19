def my_func(lst):
    a = []
    for i in range(0,(len(lst))-1):
        j = lst[i+1]-lst[i]
        a.append(abs(j))
    if sorted(set(a))==a:
        return True
    else:
        return False
    print(sorted(a))
lst = list(map(int,input().split()))
out = my_func(lst)
print(out)
