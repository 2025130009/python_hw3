hap = 0
x=int(input())

while x>0:
    hap += x%10
    x //= 10
    
print(hap)
