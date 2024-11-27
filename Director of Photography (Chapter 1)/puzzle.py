# Write any import statements here
from typing import List

class AP:
  
  @classmethod
  def init_valid_range(cls, low, high):
    cls.vrange = range(low,high+1) # +1 for inclusivity
  
  def __init__(self, startindex:int):
    self.start = startindex
    self.mids = []
        
  def add_mid(self,midindex:int):
    if midindex - self.start in AP.vrange:
      self.mids.append(midindex)

  def add_end(self, stopindex:int)-> int:
    if len(self.mids) == 0:
      return 0
    score = 0
    for mid in self.mids:
      if stopindex - mid in AP.vrange:
        print(f'start:{self.start},\tmid:{mid},\tstopindex:{stopindex}')
        score += 1

    print(score)
    return score

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  pab:List[AP] = []
  bap:List[AP] = []

  AP.init_valid_range(X,Y)
  total = 0

  for i in range(0,len(C)):
    print(f'char: {C[i]}\tindex: {i}')
    if C[i] == '.':
      continue

    if C[i] == 'P':
      pab.append(AP(i))
      
      for b in bap:
        total += b.add_end(i)        
      continue

    if C[i] == 'A':
      for p in pab:
        p.add_mid(i)

      for b in bap:
        b.add_mid(i)

      continue

    if C[i] == 'B':
      for p in pab:
        total += p.add_end(i)
        
      bap.append(AP(i))

      continue

  return total

print(f'test1: N=5 APABA X=1 Y=2 Expected:1 actual: {getArtisticPhotographCount(5,'APABA',1,2)}')
print(f'test2: N=5 APABA X=2 Y=3 Expected:0 actual: {getArtisticPhotographCount(5,'APABA',2,3)}')
print(f'test3: N=8 .PBAAP.B X=1 Y=3 Expected:3 actual: {getArtisticPhotographCount(8,'.PBAAP.B',1,3)}')
