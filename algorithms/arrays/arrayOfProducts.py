#---- Solution - 1
# Time : O(n) | Space : O(n)
def arrayOfProducts(array):
    totalProduct = 1
    numOfZeros = 0
    result = [0]*len(array)
    for num in array:
        if num == 0:
            numOfZeros += 1
            continue
        totalProduct *= num

    if numOfZeros == 0:
        for i, num in enumerate(array):
            val = totalProduct // num
            result[i] = val

    elif numOfZeros == 1:
        for i, num in enumerate(array):
            if num == 0:
                result[i] = totalProduct
    else:
        pass

    return result

#---- Solution - 2
# Time : O(n) | Space : O(n)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    
    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningSum = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningSum
        rightRunningSum *= array[i]

    return products

array = [5, 1, 4, 2]
print(arrayOfProducts(array))

array = [5, 1, 0, 2]
print(arrayOfProducts(array))

array = [1, 0, 1, 0]
print(arrayOfProducts(array))

    