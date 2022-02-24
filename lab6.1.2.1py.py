TAX_RATE = 0.2
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 2000
STANDARD_DEDUCTION = 10000.00
grossincome= input("input gross income: ")
grossincome = float(grossincome)
numberofdependents= input("input number of dependents: ")
numberofdependents= float(numberofdependents)
dependentDeduction= float(numberofdependents * DEPENDENT_DEDUCTION)
grossIncomeAfterDeduction= float(grossincome - (dependentDeduction + STANDARD_DEDUCTION))
incometax= float(incometax)
incometax = float(grossIncomeAfterDeduction * TAX_RATE)
print("the gross income after tax is", incometax, "dollars.")                                 
                                
                                 



