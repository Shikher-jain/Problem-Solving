x = ['foo', 'bar', 'baz'] 
y = ['baz', 'qux', 'quux'] 
x += y 
y += x 
print(y)

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1])

# digits=[]
numbers = [1, 2, 3, 4]
digits = numbers.append(5)
print(digits)


a = [2, 4, 6]
b = a[::-1]
c = list(a)
print(a)
print(b)
print(c)
a is b
print(a is b)


num_list = [3, 1, 5, 4, 6,2] 
# sorted_list = sorted(num_list) 
num_list.sort()
sorted_list = num_list
even_nums = [i for i in sorted_list if i % 2 == 0] 
# even_nums = [i for i in num_list if i % 2 == 0] 
print(even_nums)