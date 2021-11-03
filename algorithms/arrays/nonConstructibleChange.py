# Time : O(nlog(n)) | Space : O(1)
def nonConstructibleChange(coins):
    coins.sort()

    if not len(coins):
        return 1
    elif coins[0] != 1:
        return 1
    else:
        previous = 1

    for i in range(1, len(coins)):
        if previous + 1 >= coins[i]:
            previous += coins[i]
        else:
            break
    return previous + 1

coins = [1, 2, 5]
print(nonConstructibleChange(coins))

coins = [1, 2, 3]
print(nonConstructibleChange(coins))

coins = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))

coins = []
print(nonConstructibleChange(coins))