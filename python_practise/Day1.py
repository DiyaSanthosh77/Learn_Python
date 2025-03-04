#calculate sum of cubes of numbers
#we are provided with range L and R(both inclusive)
"""
if we  provided 2,4 then we have to calculate 2^3+3^3+4^3=99
"""
def cube_sum(low,high):
    sum=0
    for i in range(low,high+1):
        sum+=i**3
    return sum
l=2
r=4
print(cube_sum(l,r))
