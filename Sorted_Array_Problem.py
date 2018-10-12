#-------------------------------------------------------------------------------
#
# Author:      Prabhjeet Singh
#
#-------------------------------------------------------------------------------
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements
# of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
#
# Problem Reference :
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
##############################################################################
import time
import array
class solution:
    def RemoveDuplicate(self, array):
        j=0
        for i in range(1, len(array)):
            if array[i-1] != array[i]:
                j=j+1
                array[j] = array[i]
        return j+1

def main():
    # Create input array
    arr = array.array('i')
    # Create class object
    obj = solution()

    # Test case 1
    for k in range(0, 10000001):
        arr.append(k/10)
    starttime = time.time()
    num = obj.RemoveDuplicate(arr)
    endtime = time.time()
    print 'The time taken for Test case 1 = '+str(endtime - starttime)
    print 'The new length of array = '+ str(num)

    # Test case 2
    arr = [1,1,2]
    starttime = time.time()
    num = obj.RemoveDuplicate(arr)
    endtime = time.time()
    print 'The time taken for Test case 2 = '+str(endtime - starttime)
    print 'The new length of array = '+ str(num)

    # Test case 3
    arr = [1,2,3,4,5]
    starttime = time.time()
    num = obj.RemoveDuplicate(arr)
    endtime = time.time()
    print 'The time taken for Test case 3 = '+str(endtime - starttime)
    print 'The new length of array = '+ str(num)


    # Test case 4
    arr = [1,1,1,1,1]
    starttime = time.time()
    num = obj.RemoveDuplicate(arr)
    endtime = time.time()
    print 'The time taken for Test case 4 = '+str(endtime - starttime)
    print 'The new length of array = '+ str(num)

if __name__ == '__main__':
    main()
