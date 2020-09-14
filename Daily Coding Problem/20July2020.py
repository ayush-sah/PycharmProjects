# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# Brute Force Method
# def findk(n, k):
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             if n[i] + n[j] == k:
#                 return True
#     return False

# Best method
def findk(n, k):
    temp = set()
    for i in n:
        if i in temp:
            return True
        temp.add(k-i)
    return False


n = list(map(int, input().split()))
k = int(input())
print(findk(n, k))
