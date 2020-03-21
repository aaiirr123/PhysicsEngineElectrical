import math






def coulombLaw(charge1, charge2, perm, distance):
    Force = (charge1 * charge2) / (4 * math.pi * perm * (distance**2))

    return Force
    