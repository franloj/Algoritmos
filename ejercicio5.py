# 5.Desarrollar una función que permita convertir un número romano en un número decimal.

def romanoadecimal(romano: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(romano) == 0:  
        return 0            
    elif len(romano) == 1:       
        return valores[romano]  
    else:
        valor_actual = valores[romano[0]]
        valor_siguiente = valores[romano[1]]
    
        if valor_actual >= valor_siguiente:
            return valor_actual + romanoadecimal(romano[1:])
        else:
            return -valor_actual + romanoadecimal(romano[1:])

print(romanoadecimal("X"))    # Debería dar 10
print(romanoadecimal("XIV"))  # Debería dar 14
print(romanoadecimal("MCMXCVI")) # Debería dar 1996