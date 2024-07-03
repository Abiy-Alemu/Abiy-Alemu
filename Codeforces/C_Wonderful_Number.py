# wonderful number
# iwn = is_wonderful_number
#l = length
# r = result of number
def iwn(n):
    i = 0
    l = len(n)
    
    while i < l:
        if n[i:i+3] == "144":
            i += 3
        elif n[i:i+2] == "14":
            i += 2
        elif n[i:i+1] == "1":
            i += 1
        else:
            return "NO"
    return "YES"


n = input().strip()
r = iwn(n)
print(r)
