psquares = set()
for z in range(1,10000000):
    psquares.add(z*z)

def heron(a,b,c):
    s = (a + b + c) / 2.0
    return (s*(s-a)*(s-b)*(s-c))#**(1/2)

for i in range(5,20000):
    area = heron(i,i,i+1)
    if area in psquares:
        print(i,i+1,area**(1/2))
    