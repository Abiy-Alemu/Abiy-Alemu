class Solution: 
    def select(self, arr, x):
        mini = x
        for i in range(x+1, len(arr)):
            if arr[i] < arr[mini]:
                mini = i
        arr[x], arr[mini] = arr[mini], arr[x]
    
    def selectionSort(self, arr, n):
        for i in range(n):
            self.select(arr, i)
        return arr
if __name == '__main__':
    t =int(input())
    for _ in range (t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        Solution().selectionSort(arr,n)
        for i in range(n):
            print(arr[i],end = " ")
        print()
