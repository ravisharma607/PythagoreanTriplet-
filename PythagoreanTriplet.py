from  itertools import combinations
def get_triplet(array):
    squared_num = dict((num**2,num) for num in array)
    for x,y in combinations(squared_num,2):
        if(x+y) in squared_num.keys():
            return True
    return False
x = list(map(int,input("Please Enter Value seprated by comma->(,) ").split(",")))
print(get_triplet(x))