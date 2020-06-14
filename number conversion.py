s=0
m=1
#s=int(s)
n=int(input("\nEnter a number:-"))
while n!=0:
    r = n % 2
    s = s+m* r
    m = m * 10
    n=n//2
print(s)