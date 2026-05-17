# The absolute difference between two integers,  and , is written as . 
# The maximum absolute difference between two integers in a set of 
# positive integers, elements, 
# is the largest absolute difference between any two integers in __elements.

# The Difference class is started for you in the editor. 
# It has a private integer array (elements) for storing N non-negative integers, 
# and a public integer (maximumDifference) for storing the maximum absolute difference.
# Maximum Difference in Array


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        if len(self.__elements) < 2:
            self.maximumDifference = 0
        else:
            self.maximumDifference = max(self.__elements) - min(self.__elements)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)


# Find the maximum difference between any two elements in the array

# Alternate solution using sorting
# def computeDiff(arr):
#         arr.sort()
#         maximumDifference = arr[len(arr)-1]-arr[0]
#         return maximumDifference

# if __name__ == '__main__':
#     # Get array input from user
#     arr = list(map(int, input("Enter array elements (space-separated): ").split()))
#     print("Maximum difference:", computeDiff(arr))    