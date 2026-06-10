import sympy as sym

b, h = sym.symbols('b h')
h = sym.Integer(450)*sym.sqrt(2)
print('h', h, h.evalf())
b = sym.Integer(300)*sym.sqrt(2)
f_y = sym.symbols('f_y')

f_y = sym.Integer(235)

A = b * h / 2

print('A', A)

Np = A * f_y

print('Np', Np)

h_lower = h / sym.sqrt(2)
b_lower = b / sym.sqrt(2)

print('h_lower', h_lower, h_lower.evalf())
print('b_lower', b_lower, b_lower.evalf())

h_upper = h - h_lower

print('h_upper', h_upper, h_upper.evalf())

A_below = h_lower * b_lower / 2
A_upper = (b_lower + b) * h_upper / 2
print('A_below', A_below.simplify())
print('A_upper', A_upper.simplify())

z_upper = h_upper - (b * 2 + b_lower)/(b + b_lower) / 3 * h_upper
print('z_upper', z_upper)
print('z_upper', z_upper.evalf())
z_lower = h_lower  / 3
print('z_lower', z_lower)

M_p = f_y * A_below * (h_upper - z_upper + z_lower)
print('M_p', M_p, M_p.evalf())