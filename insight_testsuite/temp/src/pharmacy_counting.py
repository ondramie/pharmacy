#!/usr/bin/env python

'''Opens file and send inputs to datastructure.'''

import sys                        #argv(), exit(); 
from alt_pharm import Pharmacy    #pharmacy object

def pharm_count():
    new_pharm = Pharmacy() 
    
    # opens input log and output log
    with open(sys.argv[1], 'r') as logs, open(sys.argv[2], 'w') as output:
        next(logs)
        for row in logs: 
            #input data colums: id, last, first, drug, cost      
            values = row.strip().split(',')
            if len(values) != 5:
                pass
            else:
                cost = float(values[4] if values[4] else 0)        
                new_pharm.update_pharm(values[3], values[2], values[1], cost)

        output.write("drug_name,num_prescriber,total_cost\n")
        output.write(new_pharm.print_ouput())
    
def main():
    if sys.version_info[0] == 3 and len(sys.argv) == 3:
        try:
            pharm_count()
        except IOError:
            print(sys.stderr)
            sys.exit(1)  
    
if __name__ == "__main__":
    main()