# QF TO CANONICAL FORM

import numpy as np
from sympy import *

sym_list = []
vars = int(input("Enter the number of variables : "))

if vars == 2:
  l, x, y = symbols('l x y')
  sym_list.append("x")
  sym_list.append("y")
  
elif vars == 3:
  l, x, y, z = symbols('l x y z')
  sym_list.append("x")
  sym_list.append("y")
  sym_list.append("z")

if(vars == 2):
    coeff_x2 = int(input("Enter the coefficient of x^2: "))
    coeff_xy = int(input("Enter the coefficient of xy: "))
    coeff_y2 = int(input("Enter the coefficient of y^2: "))

    # Create the matrix with the given coefficients
    coefficient_matrix = Matrix([[coeff_x2, Rational(coeff_xy, 2)], [Rational(coeff_xy, 2), coeff_y2]])
    print(coefficient_matrix)

if(vars == 3):
    coeff_x2 = int(input("Enter the coefficient of x^2: "))
    coeff_xy = int(input("Enter the coefficient of xy: "))
    coeff_y2 = int(input("Enter the coefficient of y^2: "))
    coeff_xz = int(input("Enter the coefficient of xz: "))
    coeff_yz = int(input("Enter the coefficient of yz: "))
    coeff_z2 = int(input("Enter the coefficient of z^2: "))

    # Create the matrix with the given coefficients
    coefficient_matrix = Matrix([[coeff_x2, Rational(coeff_xy, 2), Rational(coeff_xz, 2)],
                                 [Rational(coeff_xy, 2), coeff_y2, Rational(coeff_yz, 2)],
                                 [Rational(coeff_xz, 2), Rational(coeff_yz, 2), coeff_z2]])
    print(coefficient_matrix)
    
eg_value = []
X = []
Z = []

if vars == 2:
    row_vector = [x, y]
    X1 = np.array(row_vector).reshape(1, -1)
    column_vector = [x, y]
    X2 = np.array(column_vector).reshape(-1, 1)
    Z = Matrix([0,0])
    
if vars == 3:
    row_vector = [x, y, z]
    X1 = np.array(row_vector).reshape(1, -1)
    column_vector = [x,y,z]
    X2 = np.array(column_vector).reshape(-1, 1)
    Z = Matrix([0,0,0])
    
identity_matrix = np.eye(vars)
mat1 = Matrix(coefficient_matrix - l*identity_matrix)
eq1 = Eq(mat1.det(), 0)
eg_value.extend(solve(eq1, l))
diagnol_matrix = np.diag(eg_value)
first = X1 * diagnol_matrix
can_form = first * X2

print("Canonical form:")
for i in range(vars):
  if(i == vars - 1):
    print(can_form[i][i])
  else:
    print("{0} + ".format(can_form[i][i]) , end=' ')