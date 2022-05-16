##### Let's shuffle our data
import numpy
def shuffle_same_way(a, b):
    new_a = []
    new_b = []
    
    indexes = numpy.arange(len(a))
    numpy.random.shuffle(indexes)
    for i in indexes:
        new_a.append(a[i])
        new_b.append(b[i])
   
    return new_a, new_b
