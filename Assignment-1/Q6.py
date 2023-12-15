n=int(input('Enter n: '))
space=2*(n-1)
i=1
for j in range(n):
    print(('*'*i)+(' '*space)+('*'*i))
    space-=2
    i+=1