import sympy as sym


EI = sym.symbols('EI')
Bv = sym.symbols('Bv')
F_1, F_2 = sym.symbols('F_1 F_2')
F_2 = F_1 / 24 * 5
L = sym.S(3)
M_p = sym.nsimplify(39*19)
print(M_p)

eq1 = sym.Eq(Bv * (2 * L)**3 / (3 * EI) , F_1 * L **3 / (3 * EI) + F_1 * L **2 / (2 * EI) * L + F_2 * L * (2*L) **2 / (2*EI) + F_2 * (2*L) **3 / (3*EI))
Bv = sym.solve(eq1,Bv)[0]
print(Bv)

M_C = F_2 * L
M_B = F_2 * 2 * L - Bv * L
M_A  = F_2 * 3 * L - Bv * 2*L + F_1 * L

print(M_C)
print(M_B)
print(M_A)

F_1_1 = sym.solve(sym.Eq(M_A,M_p),F_1)[0]
print(F_1_1)
print(F_2.subs(F_1,F_1_1))

w_C = F_1 * L ** 3 / (3 * EI) + F_2 * 2 * L * (L) **2 / (2*EI) + F_2 * (L) **3 / (3*EI) - Bv * (L)**3 / (3 * EI) - Bv * L * L **2 / (2 * EI)
print(w_C.subs(F_1,F_1_1))

w_C.subs(F_1,F_1_1).subs(EI, 121500)

Bv = (L * F_1 + L * 3 * F_2 - M_p) / (2 * L)
print(Bv)
M_C = F_2 * L
M_B = F_2 * 2 * L - Bv * L

print(M_C)
print(M_B)

F_1_2 = sym.solve(sym.Eq(M_C,M_p),F_1)[0]
F_1_3 = sym.solve(sym.Eq(M_B,-M_p),F_1)[0]
print(F_1_2)
print(F_1_3)

5/24*936

Bv.subs(F_1,F_1_3)

w_C = - M_p * (2 * L)**2 / EI / 16 + F_1_3 * (2*L) ** 3 / EI / 48 - F_2.subs(F_1,F_1_3) * L * (2 * L) **2 / EI / 16
print(w_C.subs(EI,121500))
print(w_C.subs(EI,121500).evalf())

M_p
w_list = [0, 9.5, 91/9, 3 * 91/9]
F_list = [0, 912, 936, 936]

import matplotlib.pyplot as plt

fig = plt.figure(facecolor='none')
plt.plot(w_list, F_list)
plt.xlabel('$w_B$')
plt.ylabel('$F$')

plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.grid()
plt.ylim(0, 1000)
plt.xlim(0, 20)
ax = plt.gca()
ax.set_facecolor('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
plt.savefig('figure.svg', format='svg', bbox_inches='tight', facecolor='none')
