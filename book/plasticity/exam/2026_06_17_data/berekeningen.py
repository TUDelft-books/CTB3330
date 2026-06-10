import sympy as sym

M_p = sym.symbols('M_p')
M_p = sym.Integer(300)
N_p = sym.symbols('N_p')
N_p = sym.Integer(40)
L_1, L_2, L_3, L_4 = sym.symbols('L_1 L_2 L_3 L_4')
L_1, L_2, L_3 = 2 , 2 , 6
F = sym.symbols('F')
delta_w = sym.symbols('delta_w')

eq1 = sym.Eq(-N_p * delta_w - M_p * delta_w / L_3 - M_p * delta_w / L_3 - M_p * delta_w / (L_1 + L_2) + F * delta_w / (L_1 + L_2) * L_1, 0)
eq2 = sym.Eq( F * delta_w - M_p * delta_w / L_1 - M_p * delta_w / L_2 - M_p * delta_w / L_2, 0)

F_1 = sym.solve(eq1, F)[0]
F_2 = sym.solve(eq2, F)[0]

print('F_1 = ', F_1)
print('F_2 = ', F_2)