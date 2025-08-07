
def fib(memo,n):
    if memo[n]!=1:
        return memo[n]
    memo[n]= fib(n-1 ,memo )+fib(n-2,memo )
    return memo[n]

n=60
memo=[-1]*(n-1)
memo[0]=0
memo[1]=1
print( fib( n ,memo ))



