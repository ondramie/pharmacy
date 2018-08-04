#!/usr/bin/env python

''' Creates data for challenge based on file: de_cc_data.txt
    run command: python3 input output 10
'''

import sys
import random
import pprint

def sample():
    decimator = int(sys.argv[3])
    drug_name = dict()
    patient_name = dict()
    count = 0
    pp = pprint.PrettyPrinter(indent=4)
    
    # opens, counts number of drugs in big file
    with open(sys.argv[1], 'r') as logs, open(sys.argv[2], 'w') as output:
        #input colums: id, last, first, drug, cost      
        output.write(next(logs))        
        for row in logs:     
            values = row.strip().split(',')  
            if values[3] in drug_name: 
                drug_name[values[3]] += 1 
            else: 
                drug_name[values[3]] = 1
            
            name = values[1] + " " + values[2]
            if name in patient_name: 
                patient_name[name] += 1 
            else: 
                patient_name[name] = 1 
        
            if count % decimator == 0:
                output.write(row)
            
            count += 1

    #pp.pprint(drug_name)

def main():
    if sys.version_info[0] == 3 and len(sys.argv) > 1:
        try:
            sample()
        except IOError:
            print(sys.stderr)
            sys.exit(1)  
    
if __name__ == "__main__":
    main()