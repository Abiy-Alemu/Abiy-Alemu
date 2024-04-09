
if __name__ == '__main__':
    x, y, z = int(input()), int(input()), int(input())
    newlist = [] 
    n = int(input())

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    newlist.append([i, j, k])

    print(newlist)

    
