import sympy as sym

b, h, t = sym.symbols('b h t')
b = sym.Integer(200)
h = sym.Integer(300)
t = sym.Integer(8)
f_y = sym.Integer(225)

M_p = f_y * b * t * h #Nmm

print(M_p)