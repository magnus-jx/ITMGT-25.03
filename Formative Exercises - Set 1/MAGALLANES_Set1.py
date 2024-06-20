#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Savings Problem

def savings(gross_pay, tax_rate, expenses):
    if tax_rate <= 0 or tax_rate >= 1:
        return "Your tax rate is out of normal bounds."
    else: 
        for_savings = int((gross_pay * (1 - tax_rate)) - expenses)
        return for_savings

# Material Waste Problem

def material_waste(total_material, material_units, num_jobs, job_consumption):
    remaining_material = total_material - (num_jobs * job_consumption)
    return str(remaining_material) + material_units

# Interest Problem

def interest(principal, rate, periods):
    earnings = principal + (principal * (rate * periods))
    return int(earnings)

