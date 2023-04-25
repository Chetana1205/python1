# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:52:52 2023

@author: Admin
"""

print("Birge Vieta Method")
n=int(input("Number of iterations required: "))
a0=int(input("a0= "))
a1=int(input("a1= "))
a2=int(input("a2= "))
a3=int(input("a3= "))
p=float(input("p="))

for i in range(1,n+1):
    print("\n iteration Number")
    b0=a0
    b1=a1+p*b0
    b2=a2+b1*p
    b3=a3+b2*p
    print("b0=",b0,"\t b1",b1,"\t b2",b2,"\tb3=",b3)
    c0=b0
    c1=b1+p*c0
    c2=b2+p*c1
    print("c0=",c0,"\t c1=",c1,"\tc2=",c2)
    p=p-(b3/c2)
    print("p",i,"=",p)
    
    