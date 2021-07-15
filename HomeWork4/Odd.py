class Odd:
   def __init__(self,it):
       self.oddNum = iter(it)
       self.index = len(it)


   def __iter__(self):
       self.elem = [i for i in self.oddNum if i %2 !=0]
       for el in self.oddNum:
           self.elem.pop(0)
           self.elem.append(el)

       self.iterator_i = 0
       return self

   def __next__(self):
      if self.iterator_i == len(self.elem):
          raise StopIteration
      else:
          ret = self.elem[self.iterator_i]
          self.iterator_i += 1
          return ret




if __name__ == "__main__":
    for i in Odd([6, 7, 8, 9, 10, 11, 12, 13]):
        print(i)




