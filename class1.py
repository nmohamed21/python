import math
x = int (input ("Please enter your 'X' value "))
b = int (input ("Please enter your 'B' value "))
if x <= 0:
    int (input ("Please enter your 'X' value that is greater than 0 "))
if b <= 0:
    int (input ("Please enter your 'B' value that is greater than 0 "))
log_base_X = math.log10 (x) / math.log10 (b) 
print (log_base_X)