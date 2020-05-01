if __name__ == '__main__':
    a = int(input())
    m = set(map(int, input().split()))
    b = int(input())
    n = set(map(int, input().split()))

    u = m.union(n)
    r = m.intersection(n)
    r = sorted(list(u.difference(r)))
    #r = sorted(list(u^r)) This the same


    for elem in r:
        print(elem)