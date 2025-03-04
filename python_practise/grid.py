#starts at [1,1]and must reach [m,n]
"""
only move right and left there will be some blocks we can't move
we have to find how many unique path there
There will always be at least one valid path
m=3,n=3,obstacle=[(2,2)]
"""
def solve(m,n,obstacle):
    if(m,n) in obstacle or m<1 or n<1:
        return 0
    if m==1 and n==1:
        return 1
    return solve(m-1,n,obstacle)+solve(m,n-1,obstacle)
m=n=3
obstacle={(2,2)}
print(solve(m,n,obstacle))


def solve(m,n,obstacle,dp={}):
    if(m,n) in obstacle or m<1 or n<1:
        return 0
    if m==1 and n==1:
        return 1
    return solve(m-1,n,obstacle)+solve(m,n-1,obstacle)
m=n=3
obstacle={(2,2)}
print(solve(m,n,obstacle))



