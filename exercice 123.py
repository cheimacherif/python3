# exercice 1
# def max_of_two(y:int,z)->int:
#     if y<z :
#         return z
#     else :
#         return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(20, 35, 19))


# exercice 2
# s=lambda a,b: {a+b , a-b}
# print ( s(10,5))


# exercice 3
def sum(list):
    s = 0
    for i in list:
        s = s+i
    return (s)


print(sum([1, 2, 3]))


def multi(list):
    s = 1
    for i in list:
        s = s*i
    return (s)


print(multi([1, 2, 3]))

if __name__ == "__main__":
    print (sum([1, 2, 3]))
    print (multi([1, 2, 3]))