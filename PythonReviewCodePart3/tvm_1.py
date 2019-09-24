# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:40:15 2019

@author: jahan
"""

import scipy as sp
import numpy.lib.financial as fin

# signature of fv fucntion is (Rate,nper(number of years),pmnt (payment),pv(present value), when='end' )
# the following is for rate = %10, one year, 0 payment and $100 principle 
futVal_1 = fin.fv(0.1,1,0,100)
help(fin.fv)
futVal_2 = fin.fv(0.1,5,0,100)

'''
Here is an example. John is planning to buy a used car with a price tag of $5,000. 
Assume that he would pay $1,000 as the down payment and borrow the rest. 
The annual interest rate for a car load is 1.9% compounded monthly. 
What is his monthly payment if he plans to retire his load in three years? 
We could calculate the monthly payment manually; see the following code:
'''

# manual calculation
r=0.019/12
pv=4000
n=3*12
pymnt = pv*r/(1-1/(1+r)**n)

pymntPermonth = 200

# Using scipy 
sp.pmt(r,n,pv)
sp.rate(n,pymntPermonth,-pv,0) 
round(sp.nper(r,-pymntPermonth,-pv,0))
fin.pmt(r,n,pv)
fin.rate(n,pymntPermonth,-pv,0)
