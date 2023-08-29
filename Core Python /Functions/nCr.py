#nCr
n=int(input())
r=int(input())

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

nfact=fact(n)
rfact=fact(r)
nrfact=fact(n-r)
ans=(nfact)//(rfact*nrfact)
print(ans)
