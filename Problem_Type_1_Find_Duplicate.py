#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      psingh
#-------------------------------------------------------------------------------
# Problem Statement 1:
# Inputs: Consider an input array of Size N and can contain only
# values upto N-1. Consider there is only one Duplicate value for this example.
#
# Outputs:  Create As many Algoritms to find the duplicate and explain
# w.r.t Time and Space Comlexity
#-------------------------------------------------------------------------------
import array
import time
class ps1:
    # This is a naive approach, comparing each element of array with
    # the rest to find the duplicate values.
    # This has TC: O(n^2) and SC: O(1)
    def algo1(self, array):
        for i in range(0, len(array)-1):
            for j in range(i+1, len(array)):
                if array[i] == array[j]:
                    return array[i]
    # This is Slightly modified from Algo 1.
    # In this case the array is Sorter first and then comparison
    # is done between the elements.
    # This has TC: O(nlogn) and SC : O(1)
    def algo2(self, array):
        array = sorted(array)
        for i in range (1, len(array)):
            if array[i-1] == array[i]:
                return array[i]
    # This is another way of approaching the same problem but come
    # with compromise on space complexity. An additional set is created
    # if the value found in the hash set than return the duplicate value
    # This has TC: O(N)  SC: O(N)
    def algo3(self, array):
        x =set()
        for i in range (0, len(array)):
            out = array[i] in x
            if out == True:
               return array[i]
            else:
                x.add(array[i])
    # This is nother technigue called negation. The value at each index
    # is read and the corresponding index(Equivalent to value) is multiplied
    # with -1. Finding the negative value will detect the Duplicate Element
    # This has TC: O(N) and SC: (1)
    def algo4(self, array):
        for i in range (0, len(array)):
            val = abs(array[i])
            if array[val] < 0:
                return val
            else:
                array[val] = array[val] * -1


def main():
    # Enter the array Size
    size = raw_input("Enter the size of array: ")

    # Create an array if integers
    arr = array.array('i')

    # Create array for testing the algorithm's worst case time
    # This may be different for different algorithm
    for i in range(0,int(size)-1):
        arr.insert(i, i+1)
    arr.insert(i+1, int(size)-1)

    # Create an object for class
    algo = ps1()

    #print arr
    starttime = time.time()
    result = algo.algo4(arr)
    endtime =  time.time()

    print "The time taken for execution =" + str(endtime - starttime)
    print result

if __name__ == '__main__':
    main()


