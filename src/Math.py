from math import *

def calculateOperation(operation : str):
  operations = {"sqrt": sqrt, "^":pow} 
  try:
    result = eval(operation,operations)
    return (True, result)
  except:
    return (False, operation)
