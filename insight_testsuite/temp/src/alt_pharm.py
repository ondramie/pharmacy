#!/usr/bin/env python

from build_heap import HeapBuilder

class DrugCost(): 
    def __init__(self, drug_name, cost): 
        self._drug_name   = drug_name
        self._accum_cost  = cost 
        self._accum_count = 1
    
    def update_dc(self, cost, patient_exists): 
        self._accum_cost += cost
        if not patient_exists:
            self._accum_count += 1 
    
    def get_cost(self):  return self._accum_cost 
    def get_count(self): return self._accum_count
    def get_drug(self):  return self._drug_name

class Patients():
    def __init__(self): 
        self._drugs = {}
    
    def _exists(self, drug, patient):
        drug_exists, name_exists = False, False
        if drug in self._drugs:
            drug_exists = True 
            if patient in self._drugs[drug]:
                name_exists = True
        
        return (drug_exists, name_exists)
    
    def update_pat(self, drug, patient): 
        check = self._exists(drug, patient)
        
        if all(check):   pass
        elif any(check): self._drugs[drug][patient] = 1
        else:            self._drugs[drug] = {patient: 1}
        
        return check

class Pharmacy():
    def __init__(self):
        self._hp = HeapBuilder()  # used for printing
        self._pt = Patients()     # ref. table of Patients
        self._dt = {}             # ref. table of drugs, counts, costs

    def _fullname(self, first, last): return str(first) + " " + str(last)
    
    def update_pharm(self, drug, first, last, cost): 
        patient = self._fullname(first, last)
        patient_lookup  = self._pt.update_pat(drug, patient)
        
        if all(patient_lookup): 
            self._dt[drug].update_dc(cost, True)    
        elif any(patient_lookup): 
            self._dt[drug].update_dc(cost, False)    
        else:
            new_drug = DrugCost(drug, cost)
            self._dt[drug] = new_drug

    def print_ouput(self): 
        return self._hp.solve(self._dt)