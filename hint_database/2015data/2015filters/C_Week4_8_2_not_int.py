def C_Week4_8_2_not_int(params):
  """ Written by yfreund Thu Oct 22 2015 13:28:13 GMT-0700 (PDT)
the size of a set has to be an integer number
  """
  hint=''
  value,classes=classify_final_value(params)
  if 'not int' in classes:
    hint='The value of the expression you entered is %f, but the sze of set has to be a non-negative integer!'%value
    #print hint
  
  return hint