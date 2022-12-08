# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:33:25 2022

@author: amitk
"""

def prob(expect,total):
  return expect/total
def bayesTheorem(pbook, pBoys, pBoysbook):
    return (pbook * pBoysbook) / pBoys
total=100
boys=40
girls=60
boysBook=5
girlsBook=20
pofbook=prob(25,100)
prob_boys_books=prob(5,25)
prob_boys=prob(40,100)
print(round((25/100)*(5/25)/(40/100),2))
print("probablity oh boys that having book: "+str(round(bayesTheorem(pofbook,prob_boys,prob_boys_books),2)))