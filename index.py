from __future__ import division

from sympy import *

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

init_printing()



# integral = Integral(sqrt(x/2), x)
print(type(diff(2*(x**2))))
decoration = diff(2*(x**2))
pprint(f'ƒ(x) = {decoration}')

prettyR = pretty(Integral(sqrt(1/x), x), use_unicode=False)
pprint(prettyR)