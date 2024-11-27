from typing import List
# Write any import statements here      

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # N = num dishes in a row
    # D = int list of 'dish types' where 1 <= D_i =< 10^6
    # K = number of previous dishes whose types are invalid to eat
    
    w = 0 # write index
    last_types = [0] * K # keep track of last K dishes
    type_set = set() # use a set for faster searching
            
    eaten = 0
    for d in D:
      #search teh set for d
      if d in type_set:
        continue

      #eat the dish
      eaten += 1

      #try to update the set
      try:
        type_set.add(d)
        type_set.remove(last_types[w])
      except:
        pass

      #update the last_types
      last_types[w] = d
      w = (w + 1) % K
        
    return eaten


print(f'test1:')
print(f'expected:5 \treturned:{getMaximumEatenDishCount(6,[1,2,3,3,2,1],1)}')
print(f'test2:')
print(f'\nexpected:4 \treturned:{getMaximumEatenDishCount(6,[1,2,3,3,2,1],2)}')
print(f'test3:')
print(f'\nexpected:2 \treturned:{getMaximumEatenDishCount(7,[1,2,1,2,1,2,1],2)}')