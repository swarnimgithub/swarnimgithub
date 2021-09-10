from sympy import *
x, y, z, i = symbols('x y z i')
#expr = x**2 + x*y +log(z)+ (1+ exp(x))
str_expr = "x**2 + x*y +log(z)+ (1+ exp(x))"
str_exp= input("enter the expression")

expr = sympify(str_exp)
#expr
#z**2 + 3*z - 1/2
expr.subs(x, i)


#print(expr)				
