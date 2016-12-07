# Exercicio 2 - MS 211 - Turma L
# Fatoracao LU & Metodo de Newton para Sistemas nao-lineares
# Andre Figueiredo de Almeida
# RA: 164047

import math

e = math.exp(1)
pi = math.pi
sin = math.sin
cos = math.cos

Fx = []

def F1(x1, x2, x3):
    f = 3*x1 - cos(x2*x3) - 0.5
    return f

def F2(x1, x2, x3):
    f = x1**2-81*(x2+0.1)**2 + sin(x3) + 1.06
    return f

def F3(x1, x2, x3):
    f = e**(-x1*x2)+20*x3+(10*pi-3)/3
    return f

Fx.append(F1)
Fx.append(F2)
Fx.append(F3)

def J11(x1, x2, x3):
    return 3

def J12(x1, x2, x3):
    return x3*sin(x2*x3)

def J13(x1, x2, x3):
    return x2*sin(x2*x3)

def J21(x1, x2, x3):
    return 2*x1

def J22(x1, x2, x3):
    return -162*(x2+0.1)

def J23(x1, x2, x3):
    return math.cos(x3)

def J31(x1, x2, x3):
    return x2*(-e**(-x1*x2))

def J32(x1, x2, x3):
    return x1*(-e**(-x1*x2))

def J33(x1, x2, x3):
    return 20

def criaMatriz(tam):
    M = []
    for i in range(0, tam):
        M.append([])
    return M

F = criaMatriz(3)
J = criaMatriz(3)
L = criaMatriz(3)
U = criaMatriz(3)
J[0].append(J11)
J[0].append(J12)
J[0].append(J13)
J[1].append(J21)
J[1].append(J22)
J[1].append(J23)
J[2].append(J31)
J[2].append(J32)
J[2].append(J33)

def printM(m):
    s = ""
    for i in range(0, 3):
        for j in range(0, 3):
            s += str(m[i][j]) + " "
        print(s)
        s = ""


def subtrairLinhas(l1, l2, m):
    for i in range(0, 3):
        U[l2][i] -= U[l1][i] * m

def calculaJ(x1, x2, x3):
    for i in range(0, 3):
        for j in range (0, 3):
            J[i][j] = J[i][j](x1, x2, x3)

def calculaF(x1, x2, x3):
    for i in range(0, 3):
        F[i] = Fx[i](x1, x2, x3)

def calculaLU():
    for i in range(0, 3):
        for j in range (0, 3):
            U[i].append(J[i][j])

    for i in range(0, 3):
        for j in range (0, 3):
            if i == j:
                L[i].append(1)
            else:
                L[i].append(0)

    for i in range(0, 2):
        pivo = U[i][i];
        for j in range(i+1, 3):
            m = U[j][i]/pivo
            L[j][i] = m
            for k in range(0, 3):
                U[j][k] -= U[i][k]*m

def resolveS():
    k1 = -F[0];
    k2 = -F[1] - (L[1][0]*k1);
    k3 = -F[2] - (L[2][0]*k1) - (L[2][1]*k2);

    y = []
    y.append(k3 / U[2][2])
    y.append((k2 - y[0]*U[1][2]) / U[1][1])
    y.append((k1 - y[1]*U[0][1] - y[0]*U[0][2]) / U[0][0])
    return y

def calculaPorraToda(x1, x2, x3):
    calculaJ(x1, x2, x3)
    calculaLU()

    for i in range(0, 7):
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
        print("x3 = " + str(x3))
        print()
        calculaF(x1, x2, x3)
        y = resolveS()
        x1 += y[2]
        x2 += y[1]
        x3 += y[0]

calculaPorraToda(0, 0, 0)
