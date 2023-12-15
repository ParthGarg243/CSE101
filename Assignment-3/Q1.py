n=int(input('Enter n: '))
up=0
down=n-2

def upper(n,up):
    if n==1:
        line=('* '*n)+('  '*up)+('* '*n)
        return line
    else:
        line=('* '*n)+('  '*up)+('* '*n)+('\n')
        return line + upper(n-1,up+2)

def lower(down):
    if down==0:
        return ('* '*(n-down))+('  '*(2*(down)))+('* '*(n-down))
    else:
        line=('* '*(n-down))+('  '*(2*(down)))+('* '*(n-down))+('\n')
        return line + lower(down-1)

print(upper(n,up))
print(lower(down))