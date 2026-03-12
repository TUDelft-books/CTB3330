import sympy as sym

wS = sym.symbols('wS',real=True,positive=True)
#wS = 0.02
E = sym.nsimplify(200e9)
A1 = sym.nsimplify(10e-6)
A2 = sym.nsimplify(20e-6)
fy = sym.nsimplify(500e6)
wC = wS/2
eps_HC = wC / 10
N_HC = E * A1 * eps_HC
display(N_HC)
sigma_HC = E * eps_HC
display(sigma_HC/1e6)

wB = wS/8*5
N_BG = sym.Piecewise((wB / ( 4 / (E * A2) + 8 / (E * A1) ), wB / ( 4 / (E * A2) + 8 / (E * A1) ) / A1 <= fy), (fy * A1, True))
display(N_BG)
sigma_BE = N_BG / A1
sigma_EG = N_BG / A2
display(sigma_BE/1e6)
display(sigma_EG/1e6)
eps_BE = sigma_BE / E
eps_EG = sigma_EG / E
w_E = eps_EG * 4

Dv = N_HC / 2
Av = N_BG  / 8 * 3
F = N_BG + N_HC - Av - Dv
display(F)

w_1 = sym.solveset(sym.Eq(sigma_BE, sym.nsimplify(500e6)),wS,domain=sym.Reals).args[0]
display(w_1)
print(w_1.evalf())
w_2 = sym.solve(sym.Eq(sigma_HC, sym.nsimplify(500e6)),wS)[0]
display(w_2)
print(w_2.evalf())
#w_3 = sym.solve(sym.Eq(sigma_EG, sym.nsimplify(500e6)),wS)[0]
#display(w_3)
#print(w_3.evalf())
print(F.subs(wS,w_1))
print(F.subs(wS,w_2).evalf())

import matplotlib.pyplot as plt

plt.plot(w_list, F_list)
plt.xlabel('$w_S$')
plt.ylabel('$F$')

plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.grid()
plt.ylim(0, 6e3)
plt.xlim(0, 0.1)
plt.show()
plt.savefig('F_wS.svg')
