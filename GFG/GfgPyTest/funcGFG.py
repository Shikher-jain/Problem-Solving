def magic(numList):

    return [lambda x: i*x for i in numList]


funcs = magic([1, 2, 3]); print([f(2) for f in funcs])

def recursive_function(n):
    if n < 1:
        return [] 
    else:
        return [n**2] + recursive_function(n-1)
n=10
print(recursive_function(n))