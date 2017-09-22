def purify(listOfNums):
  newList = []
  for nums in listOfNums:
    if nums % 2 == 0:
      newList.append(nums)
  return newList
      
purify([1,3,2,4,5,6])
    
