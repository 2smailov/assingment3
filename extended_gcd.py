def gcdExtended(a, b, x, y):
   if a == 0 :
      x = 0
      y = 1
      return b
   x1 = 1
   y1 = 1 
   gcd = gcdExtended(b%a, a, x1, y1)
   x = y1 - (b/a) * x1
   y = x1
   return gcd
x = 1
y = 1
a = 72
b = 44
g = gcdExtended(a, b, x, y)
print(g)
