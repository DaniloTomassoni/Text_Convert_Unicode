#from binario_decimal import binario_decimal

def binario_hexadecimal(numero_binario, binario_decimal=None):
    
    bin_hex = ""
    bin_str = str(numero_binario)[::-1]
    i = 0
    ii = 4
    for k in range(0, len(bin_str)):
        
        for j in range(1):
            
            if len(bin_str[i:ii]) == 4:
                bin_hex +=str(binario_decimal(bin_str[i:ii][::-1])) 
            else:
                if len(bin_str[i:ii]) == 1:
                    bin_hex += str(binario_decimal('000'+bin_str[i:ii][::-1]))
                if len(bin_str[i:ii]) == 2:
                    bin_hex += str(binario_decimal('00'+bin_str[i:ii][::-1]))
                if len(bin_str[i:ii]) == 3:
                    bin_hex += str(binario_decimal('0'+bin_str[i:ii][::-1]))
            if bin_hex == '15':
                bin_hex = 'F'
            if bin_hex == '14':
                bin_hex = 'E'
            if bin_hex == '13':
                bin_hex = 'D'
            if bin_hex == '12':
                bin_hex = 'C'
            if bin_hex == '11':
                bin_hex = 'B'   
            if bin_hex == '10':
                bin_hex = 'A'
            
        i = ii
        ii += 4
        
    return str(bin_hex)[::-1]