#!/usr/bin/env python

''' unit test: tests input files and sees 

'''

import pytest
import sys
import os


from .src.alt_pharm import Pharmacy
from .build_heap import HeapBuilder

@pytest.fixture
def setup_test_data():
	input_file  = os.curdir + "/test_0/input/oneEntry.txt"


	return input_file

inputs = setup_test_data()

class TestGetDate():
    def test_correct(self):
    	'''test input file against output file by instantiating Pharmacy object and 
    	   HeapBuilder object; input file has only one entry 
    	'''

    	test_pharm = Pharmacy()
    	with open(inputs, 'r') as logs:
    		next(logs)
    		for row in logs: 
	            #input data colums: id, last, first, drug, cost      
	            values = row.strip().split(',')
	            if len(values) != 5:
	                pass
	            else:
	                cost = float(values[4] if values[4] else 0)        
	                test_pharm.update_pharm(values[3], values[2], values[1], cost)

        assert test_pharm.print_ouput() == "B,1,10\n"








