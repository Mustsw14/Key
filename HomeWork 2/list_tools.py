from functools import reduce

def all_even(lst):
    lst1=[]
    if lst:
        lst1=  [s for s in lst if s % 2 == 0]
        return lst1
    else:
        return lst1


def all_not_multiple(lst, n):
    lst2=[]
    if lst:
        lst2 = [s for s in lst if s % n != 0]
        return lst2
    else:
        return lst2


def max_from_2_tuples(tup):
    lst1= []
    if tup is None or len(tup) <= 1:
        return tup
    return reduce(lambda x, y: (max(x[0], y[0]), max(x[1], y[1])), tup)


def lower_case_words(sentence):
    return [word.lower() for word in sentence.split()]


def baby_names(names,last_name):
    return [i + " " + j + " " + last_name for i in names for j in names if j != i]



#[i + " " + j + " " + baby_names[1] for i in baby_names[0] for j in baby_names[0] if j != i]

'''
 return [sentence.lower().split()]
    list = []
    list1= []
    i = 0
    while i < len(tuples):
        for tuple in tuples:
            list.append(tuple[0])
            list1.append(tuple[1])
            i = i+ 1
    list3 = max(list)
    list4 = max(list1)
    tuple1 = (list3,list4)
    return tuple1
'''



