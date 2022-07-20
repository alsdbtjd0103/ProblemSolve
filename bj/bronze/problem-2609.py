a,b=map(int,input().split())

def gcd(a,b):
    a,b=max(a,b),min(a,b)
    if a%b==0:
        return b
    return gcd(b,a%b)


def lcm(c,a,b):
    return c*(a//c)*(b//c)

x= gcd(a,b)
y=lcm(x,a,b)
print(x)
print(y)


