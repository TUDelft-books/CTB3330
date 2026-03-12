import sympy as sym

F = sym.symbols('F')

L, f_y, A, E = sym.symbols('L f_y A E')

A = sym.nsimplify(100e-6)
E = sym.nsimplify(200e9)
f_y = sym.nsimplify(275e6)
L = sym.nsimplify(2.8)


EA = sym.nsimplify(E * A)

#EA = sym.symbols('EA')

w_A, w_C = sym.symbols('w_A w_C')

w_B = w_A - (w_A - w_C) / 3 * 2
w_F = (w_A + w_C) / 2

N_AD = EA / L * w_A
N_BE = EA / L * w_B
N_CG = EA / L * w_C

print('N_AD =', N_AD,'approx', N_AD.evalf())
print('N_BE =', N_BE,'approx', N_BE.evalf())
print('N_CG =', N_CG,'approx', N_CG.evalf())

symF = sym.Eq(N_AD + N_BE + N_CG - F, 0)
symT = sym.Eq(N_BE * 4 + N_CG*6 - F * 3, 0)

sol = sym.solve((symF, symT), (w_A, w_C))
w_A_elastic = sol[w_A]
w_C_elastic = sol[w_C]

w_B_elastic = w_A_elastic - (w_A_elastic - w_C_elastic) / 3 * 2

print('w_A =', w_A_elastic*1000000,'approx', (w_A_elastic*1000000).evalf())
print('w_B =', w_B_elastic*1000000,'approx', (w_B_elastic*1000000).evalf())
print('w_C =', w_C_elastic*1000000,'approx', (w_C_elastic*1000000).evalf())

N_AD_elastic = N_AD.subs({w_A: w_A_elastic})
N_BE_elastic = N_BE.subs({w_B: w_B_elastic, w_A: w_A_elastic, w_C: w_C_elastic})
N_CG_elastic = N_CG.subs({w_C: w_C_elastic})
print('N_AD =', N_AD_elastic,'approx', N_AD_elastic.evalf())
print('N_BE =', N_BE_elastic,'approx', N_BE_elastic.evalf())
print('N_CG =', N_CG_elastic,'approx', N_CG_elastic.evalf())

F_p = sym.nsimplify(f_y * A)

print('F_p =', F_p,'approx', F_p.evalf())

elas_end = sym.Eq(F_p, N_AD_elastic)
sol_elas_end = sym.solve(elas_end, F)
F_elas_end = sol_elas_end[0]
print('F_elas_end =', F_elas_end,'approx', F_elas_end.evalf())

print('N_AD_end =',N_AD_elastic.subs(F, F_elas_end),'approx', N_AD_elastic.subs(F, F_elas_end).evalf())
print('N_BE_end =',N_BE_elastic.subs(F, F_elas_end),'approx', N_BE_elastic.subs(F, F_elas_end).evalf())
print('N_CG_end =',N_CG_elastic.subs(F, F_elas_end),'approx', N_CG_elastic.subs(F, F_elas_end).evalf())

w_A_elas_end = w_A_elastic.subs(F, F_elas_end)
w_C_elas_end = w_C_elastic.subs(F, F_elas_end)

print('w_A =', w_A_elas_end*1000,'approx', (w_A_elas_end*1000).evalf())
print('w_C =', w_C_elas_end*1000,'approx', (w_C_elas_end*1000).evalf())

w_F_elastic = w_F.subs({w_A: w_A_elastic, w_C: w_C_elastic}).subs({F: F_elas_end})
print('w_F =', w_F_elastic,'approx', w_F_elastic.evalf())

print('F_p = ', F_p,'approx', F_p.evalf())

N_BE_plastic_expr, N_CG_plastic_expr = sym.symbols('N_BE_plastic N_CG_plastic')
F = sym.symbols('F')

symF = sym.Eq(F_p + N_BE_elastic.subs(F, F_elas_end) + N_BE_plastic_expr + N_CG_elastic.subs(F, F_elas_end) + N_CG_plastic_expr - F_elas_end - F, 0)
symT = sym.Eq((N_BE_plastic_expr + N_BE_elastic.subs(F, F_elas_end)) * 4 + (N_CG_plastic_expr + N_CG_elastic.subs(F, F_elas_end)) * 6 - (F_elas_end + F) * 3, 0)

print('symF =', symF)
print('symT =', symT)

sol = sym.solve((symF, symT), (N_BE_plastic_expr, N_CG_plastic_expr))
N_BE_plastic = sol[N_BE_plastic_expr]
N_CG_plastic = sol[N_CG_plastic_expr]

print('N_BE =', N_BE_plastic,'approx', N_BE_plastic.evalf())
print('N_CG =', N_CG_plastic,'approx', N_CG_plastic.evalf())

F_CG_plastic = sym.Eq(N_CG_elastic.subs(F, F_elas_end) +N_CG_plastic, F_p)
F_BE_plastic = sym.Eq(N_BE_elastic.subs(F, F_elas_end) +N_BE_plastic, F_p)

sol_CG_plastic = sym.solve(F_CG_plastic, F)
sol_BE_plastic = sym.solve(F_BE_plastic, F)
F_CG_plastic = sol_CG_plastic[0]
F_BE_plastic = sol_BE_plastic[0]

print('F_CG_plastic =', F_CG_plastic,'approx', F_CG_plastic.evalf())
print('F_BE_plastic =', F_BE_plastic,'approx', F_BE_plastic.evalf())

F_end = F_elas_end + F_BE_plastic

print('F_end= ',F_end,'approx',F_end.evalf())
print(N_CG_elastic.subs(F, F_elas_end))
N_CG_plastic = N_CG_elastic.subs(F, F_elas_end) + N_CG_plastic.subs(F, F_BE_plastic)
print('N_CG_plastic = ',N_CG_plastic,'approx', N_CG_plastic.evalf())

w_B = sym.symbols('w_B')

w_plastic_eq = sym.Eq(F_p, EA / L * w_B)
w_plastic = sym.solve(w_plastic_eq,w_B)
w_B_plastic = w_plastic[0]
w_plastic_eq2 = sym.Eq(N_CG_plastic, EA / L * w_C)
w_plastic2 = sym.solve(w_plastic_eq2,w_C)
w_C_plastic = w_plastic2[0]

print('w_B_plastic =', w_B_plastic,'approx', w_B_plastic.evalf())
print('w_C_plastic =', w_C_plastic,'approx', w_C_plastic.evalf())

w_end = w_C_plastic + (w_B_plastic - w_C_plastic) / 2 * 3
print('w_end = ', w_end, 'approach', w_end.evalf())

#w_plastic = sym.solve(w_plastic_eq,w)

#w_F_plastic = w_F.subs({w_A: w_A_elastic, w_C: w_C_elastic}).subs({F: F_plas_end})
#print('w_F =', w_F_plastic,'approx', w_F_plastic.evalf())
