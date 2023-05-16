F = G m^1m^2/r^2

def gravforce(m1, m2, r):
  G = 6.673*(10**(-11))
  force = (G(m1*m2))/(r**2)
  print(force)

gravforce(14,222, 2)