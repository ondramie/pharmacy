#!/usr/bin/env python

''' unit test: tests input files and asserts output 
'''

import pytest
import os, sys

os.chdir(os.getcwd() + "/src/")
from alt_pharm import Pharmacy
from build_heap import HeapBuilder

@pytest.fixture
def setup_test_data():
	input_file_one  = "../insight_testsuite/tests/test_0/input/oneEntry.txt"
	input_file_two  = "../insight_testsuite/tests/test_0/input/missingComa.txt"
	return input_file_one, input_file_two

input_one, input_two = setup_test_data()

class TestGetDate():
    def test_correct(self):
    	'''test input file against output file by instantiating Pharmacy object and 
    	   HeapBuilder object; input file has only one entry 
    	'''
    	def testing(inputs): 
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

			
	assert testing(input_one) == "B,1,10\n"
	assert testing(input_two) == "B,2,70\n"
