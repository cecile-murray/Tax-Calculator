import sys
import csv
sys.path.append("../../")
from taxcalc import *
import pandas as pd
from pandas import DataFrame
import tools

 #=======================================================================================================
 # GLOBALS
 #=======================================================================================================

USEFUL_TPC_BINS =  [-1e14, 9999, 19999, 29999, 39999, 49999, 74999, 99999,
                  199999, 499999, 999999, 1e14]

TPC_BIN_LABELS = {'less_10k': 0, '10-20k': 1, '20-30k': 2, '30-40k': 3, '40-50k': 4, '50-75k': 5, '75-100k': 6, '100-200k': 7, '200-500k': 8, '500-1M': 9, '1M+': 10}
 
 #=======================================================================================================
 # FUNCTIONS
 #=======================================================================================================

# Wrapper for writing pandas to csv
def write_panda(panda, filename):

	panda.to_csv(path_or_buf=filename, sep=',', na_rep='-1', line_terminator='\r\n', chunksize=1)

    #print "File " + str(filename) + "has been written to csv."

	return

# Calculate the share of filers in a bracket with positive income tax
def pos_inc_tax(calc, income_bins):

    rv = []

    pos = (calc.records.s006[(calc.records.e08800 > 0) *(calc.records.c00100 < income_bins[1] )]).sum()
    rv.append(pos)

    for b in range(1,len(income_bins)-1):

        pos = (calc.records.s006[(calc.records.c00100 > income_bins[b]) * (calc.records.c00100 < income_bins[b+1]) * (calc.records.e08800 > 0)]).sum()
        rv.append(pos)

    pos = (calc.records.s006[(calc.records.e08800 > 0) * (calc.records.c00100 > income_bins[len(income_bins)-1])]).sum()    
    rv.append(pos)

    return rv

# Non-functional alternative version of the pos_inc_tax function
def pos_tax(calc, income_bins):

    res = results(calc)

    res['has_tax'] = res['s006'].where((res['e08800'] > 0) & (res['c00100'] <= income_bins[1]), 0)
    print "bin 0 is: " + str(res['has_tax'].sum())

    for b in range(1, len(income_bins)-2):

        res['has_tax'] = res['s006'].where((res['e08800'] > 0) & (res['c00100'] > income_bins[b]) & (res['c00100'] <= income_bins[b+1]), 0)
        print "bin " + str(b) + " is: " + str(res['has_tax'].sum())

    res['has_tax'] = res['s006'].where((res['e08800'] > 0) & (res['c00100'] > income_bins[len(income_bins)-1]), 0)
    print "last bin is: " + str(res['has_tax'].sum())   

    res['has_tax'] = res['s006'].where((res['e08800'] > 0))
    print "Overall number is: " + str(res['has_tax'].sum())   

    return
   
# Calculate the share of filers in each bracket with positive payroll tax
def pos_fica(calc, income_bins):

    rv = []

    pos = (calc.records.s006[(calc.records._fica > 0) * (calc.records.c00100 < income_bins[1] )]).sum()
    rv.append(pos)

    for b in range(1,len(income_bins)-1):

        pos = (calc.records.s006[(calc.records.c00100 > income_bins[b]) * (calc.records.c00100 < income_bins[b+1]) * (calc.records._fica > 0)]).sum()
        rv.append(pos)

    pos = (calc.records.s006[(calc.records._fica > 0) * (calc.records.c00100 > income_bins[len(income_bins)-1])]).sum()    
    rv.append(pos)

    return rv   



 #=======================================================================================================
 # MAIN
 #=======================================================================================================



if __name__ == '__main__':
    print 'glory to AMR'

# Default Plans
#Create a Public Use File object
tax_dta = pd.read_csv("puf.csv")
# Create a default Parameters object
params1 = Parameters(start_year=2014, budget_years=10)
records1 = Records(tax_dta)
# Create a Calculator
calcX = Calculator(records=records1, params=params1)

print "Calculator object created."

calcX.calc_all()

print "Creating distribution table..."

tX = create_distribution_table(calcX, groupby="weighted_deciles", result_type="weighted_sum")


DIST_LABELS = ['Returns', 'has_tax', 'has_payroll', 'e08800', '_earned', 'AGI', 'Standard Deduction Filers',
                'Standard Deduction', 'Itemizers',
                'Itemized Deduction', 'Personal Exemption',
                'Taxable Income', 'Regular Tax', 'AMTI', 'AMT Filers', 'AMT',
                'Tax before Credits', 'Non-refundable Credits',
                'Tax before Refundable Credits', 'Refundable Credits',
                'Revenue']

tX.columns = DIST_LABELS

print "Standard distribution table created."

print "Creating TPC distribution table..."

tC = create_distribution_table(calcX, groupby="useful_tpc_bins", result_type="weighted_avg")

print "TPC-style distribution table created."

# Check for positive income tax and positive payroll tax:
inc_tax = pos_inc_tax(calcX, USEFUL_TPC_BINS)
fica = pos_fica(calcX, USEFUL_TPC_BINS)

#tools.write_nested_list(inc_tax, 'output/income_tax.csv')
#tools.write_nested_list(fica, 'output/fica_tax.csv')
