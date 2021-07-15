class Last:
    def __init__(self, it, count):
        self.last = iter(it)
        self.count = count

    def __iter__(self):
        ''' returns the iterator '''
        # process self.last to get the last
        # count number of elements
        self.elem = [next(self.last) for i in range(self.count)]
        # while there are elements in the list
        # add one element to the last
        # and remove one from front
        for el in self.last:
            self.elem.pop(0)
            self.elem.append(el)

        self.iterator_i = 0
        return self

    def __next__(self):
        # if index in equal to count
        # then raise StopIteration
        if self.iterator_i == self.count:
            raise StopIteration
        else:
            # get element at index - 1
            ret = self.elem[self.iterator_i]
            # increment iterator_i
            self.iterator_i += 1
            return ret

if __name__ == "__main__":

    for i in Last([6, 7, 8, 9, 10, 11, 12, 13], 3):
        print(i)