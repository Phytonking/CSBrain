import sqlite3
import re
from text import writing
import data

def retrieve(classname):
   f = open(f"{classname}.brain", "r") 
   n = f.readlines()
   lines = {}
   for x in n:
       if "<" in x:
           continue
       else:
           line = x
           if "\t" in line:
               xt = line.split("\t")
           if "\n" in line:
               xn = xt[1].split("\n")    
           xl = xn[0].split(":")
           lines.update({xl[0]:xl[1]})
   f.close()        
   return lines

