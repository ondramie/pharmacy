#!/usr/bin/env python

'''Heap object used for building a heap and then sorting the heap to print results'''

import math  #ceil()

class HeapBuilder:
    def __init__(self):
        self._size, self._max_size = 0, 0 
        self._data     = [] 
        self._print    = ''
    
    def parent(self, i):      return (i - 1)//2   
    def left_child(self, i):  return 2*i + 1
    def right_child(self, i): return 2*i + 2
    def is_empty(self):       return False if self._data else True
  
    def read_data(self, data):
        self._size = int(len(data))                              
        self._data = [(data[key].get_cost(), key, data[key].get_count()) for key in data]           
        tree_levels = math.ceil(math.log(self._size + 1, 2))
        self._max_size = 2**tree_levels - 1                       
        assert self._size == len(self._data)                
    
    def shift_down(self, i):
        max_index = i
        l = self.left_child(i)
        if l < self._size and self._data[l] > self._data[max_index]:
            max_index = l 
    
        r = self.right_child(i)
        if r < self._size  and self._data[r] > self._data[max_index]:
            max_index = r
    
        if i != max_index:
            self._data[i], self._data[max_index] = self._data[max_index], self._data[i]
            self.shift_down(max_index)

    def extract_max(self):
        result = self._data[0]
        self._data[0] = self._data[self._size - 1]
        self._size -= 1
        self.shift_down(0)
        return result

    def build_heap(self):
        seq = list(range(self._size//2))
        for i in reversed(seq):
            self.shift_down(i)
    
    def print_out(self):
        assert self.is_empty() == False
        for _ in range(self._size):
            v = self.extract_max()
            value = str(int(v[0]) if float(v[0]).is_integer() else round(v[0], 2))
            self._print += str(v[1]) + "," + str(v[2]) + "," + value + "\n"
        return self._print

    def solve(self, data):
        self.read_data(data)    
        self.build_heap()
        return self.print_out()       
