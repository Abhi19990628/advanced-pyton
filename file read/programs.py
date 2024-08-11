def missing_num(array,n):
    expect_Sum = (n*(n+1))//2
    real_sum = sum(array)
    return expect_Sum-real_sum
n=6
array=[1,2,3,4,5]
result = missing_num(array,n)
print(result)


def find_3rd_largest_value(array):
    array.sort()  # Sorts the array in place
    return array[-3]  # Returns the 3rd largest value

array = [1, 33, 421, 34, 21, 34, 2]
print(find_3rd_largest_value(array))


