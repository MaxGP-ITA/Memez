import math

def count_vowels(s):
    counter = 0
    for i in range(len(s)):
        if s[i].upper() == "A":
            counter = counter + 1
        elif s[i].upper() == "E":
            counter = counter + 1
        elif s[i].upper() == "I":
            counter = counter + 1
        elif s[i].upper() == "O":
            counter = counter + 1
        elif s[i].upper() == "U":
            counter = counter + 1
    return counter

def vector_product3(a, b):
    return a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]

def seq_mult_scalar(a,s):
    return [a[0] * s, a[1] * s, a[2] * s]

def powers(n,k):
    powers = []
    for i in range(k + 1):
        powers.append(math.pow(n,i))
    return powers

def traffic_light(load):
    if load < 0.7:
        return "Green"
    elif (load >= 0.7) & (load < 0.9):
        return "Amber"
    elif load >= 0.9:
        return "Red"
    
def box_volume_UPS(a = 13 , b = 11, c = 2):  
    return a * b * c
