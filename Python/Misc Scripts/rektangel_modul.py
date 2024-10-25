import math as m

def areal_rektangel(l, b):
    areal = l*b
    print("AREAL:", areal, "m2")
    
def diagonal_rektangel(l, b):
    diagonal = m.sqrt(l**2 + b**2)
    print("DIAGONAL:", diagonal, "m")
    
def omkrets_rektangel(l, b):
    omkrets = l + l + b + b
    print("OMKRETS:", omkrets, "m")
    
finstat = "pizdec"