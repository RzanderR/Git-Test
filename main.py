import math

def quadformula(a,b,c):
  try:
    s = math.sqrt((b**2)-(4*a*c))
  except:
    print('no')
  s = math.sqrt((b**2)-(4*a*c))
  x1 = (-b+s)/(2*a)
  x2 = (-b-s)/(2*a)
  print(x1)
  print(x2)

quadformula(1,-4,4)