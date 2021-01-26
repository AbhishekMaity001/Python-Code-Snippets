# Lambda function : use it untill and unless the expression is only 1 line...it has to have only 1 return parameter!!!
# ananoymns function

func2 = lambda x : x*2
print(func2(10))
func3= (lambda x, y, z : x+y+z)
print(func3(1,2,3))

a = [1,2,3,4,5,6,7,8,9,10]

newlist = list(map(lambda x : x*x, a))
print(newlist)

ab = [1,2,3]
cd = [1,2,3]
print('==', ab==cd)
print('is', ab is cd)
print('their values are equal but ids are different ')
print(id(ab), id(cd))


ab = cd
print('==', ab==cd)
print('is', ab is cd)
print('ab = cd ')
print(id(ab), id(cd))

ab[0] = 'abhi'
print(ab, cd)


