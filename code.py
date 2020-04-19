# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    def __add__(self,other):
        x = self.real + other.real
        y = self.imag + other.imag
        return complex_numbers(x,y)
    def __sub__(self,other):
        x = self.real - other.real
        y = self.imag - other.imag
        return complex_numbers(x,y)
    def __mul__(self,other):
        x = (self.real*other.real) - (self.imag*other.imag)
        y = (self.imag*other.real) + (self.real*other.imag)
        return complex_numbers(x,y)
    def __truediv__(self,other):
        x = ((self.real*other.real)+(self.imag*other.imag))/(other.real**2 + other.imag**2)
        y = ((self.imag*other.real)-(self.real*other.imag))/(other.real**2 + other.imag**2)
        return complex_numbers(x,y)
    def absolute(self):
        abs_val=((self.real)**2 + (self.imag)**2)**0.5
        return abs_val
    def argument(self):
        argm=np.arctan(self.real/self.imag)
        print(argm)
        angle=math.degrees((math.pi)/2-argm)
        return round(angle,2)
    def conjugate(self):
        r=self.real
        i=(-1)*self.imag
        return complex_numbers(r,i)
       


comp_1 = complex_numbers(3.0, 5.0)
comp_2 = complex_numbers(4.0, 4.0)

print(comp_1)
comp_sum=comp_1.__add__(comp_2)
print(comp_sum)
comp_diff=comp_1.__sub__(comp_2)
print(comp_diff)
comp_prod=comp_1.__mul__(comp_2)
print(comp_diff)
comp_quot=comp_1.__truediv__(comp_2)
print(comp_quot)
comp_abs=comp_1.absolute()
print('Absolute value of complex number 1='+str(comp_abs))
comp_conj=comp_1.conjugate()
print('Conjugate value of complex number 1='+str(comp_conj))
comp_arg=comp_1.argument()
print('Argument value of complex number 1='+str(comp_arg))


