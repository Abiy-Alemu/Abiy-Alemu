t = int(input()) # t = test case

for _ in range(t):
    n = int(input())
    count = 0
    a = list(map(int, input().split())) # a = current difficlty
    b = list(map(int,input().split()))  # b =  exepcted difficalty

    for i in range(n):
        if a[count] <= b[i]:
            count += 1

    print(n-count)



  				  			       		 	  				 	