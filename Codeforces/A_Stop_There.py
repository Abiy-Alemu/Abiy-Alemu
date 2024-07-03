t = int(input().strip())
for i in range(t):
    n, c = input().strip().split(' ')
    s = input().strip()
    if c == 'g':
        print(0)
    else:
        index_g = s.index('g')
        index_r = s.rindex('r')
        if c == 'r':
            print(index_g - index_r + 1)
        else:
            if index_r < index_g:
                print(index_g - index_r)
            else:
                print(index_g)