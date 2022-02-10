# Implementation of the Binary Search algorihim.
# Finds the index of the value within an array.

class BinarySearch:
  '''
    Implementation of the Binary Search Algortithim.
    Finds the index of the specified value within the array.
    Time complexity of log.
  '''

  def __init__(self, arr, value_search):
    '''
      arr: the array to search
      value_search: the value of the index to find in the array.
      
      => returns the index of the specified value within the array if it exists, else returns None. 
    '''
    
    self.arr = arr
    self.value_search = value_search

    # Step 1: Sort the array in asecending order.
    self.sortArray()

    # Step 2: divide the array and determine which half of the array the value being searched lies in.
    # Continue to divide the array in half until the value is reached or only one value is left.
    # If that one value is not the value, then return none, or else return the index of the value.
    self.binarySearchArray(self.arr)

  
  # Sort the array in ascending order
  def sortArray(self):
    self.arr = sorted(self.arr)

  # Divide the array and determine which half of the array the value being searched lies in.
  def binarySearchArray(self, arr):
    low = 0
    high = len(arr)


    while (high - low != 1):

      midpoint = int((high - low)/2) + low

      
      if (arr[midpoint] == self.value_search):
        print("The value {} occurs in index #{} in the array.".format(self.value_search, midpoint))
        return midpoint
      
      elif (arr[midpoint] > self.value_search):
        high = midpoint
      
      elif (arr[midpoint] < self.value_search):
        low = midpoint

    print('Value does not exist in the array')
    return None

BinarySearch([1,2,3,4,5,6,7,40], 40)


      


      




  
    
