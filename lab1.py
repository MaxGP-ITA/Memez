import math

def distance(number1, number2):
    try:
        output = math.sqrt(math.square(number1 - number2))        
           
        return(output)
    except:
        print("Invalid input")    
    
    
    
def geometric_mean(number1, number2):
    try:        
        output = math.sqrt(number1 * number2)     
        return(output)
    except:
        print("Invalid input")
        
        
        
def pyramid_volume(area, height):
    try:
        output = 1/3 * area * height        
        return(output)
    except:
        print("Invalid input")