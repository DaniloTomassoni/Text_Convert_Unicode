def decimal_binario(valor_decimal,octal=False, hexadecimal=False):
    
    decimal = int(valor_decimal)
    binario_list = list()
    binario_str = ""
    while True:
        resto = decimal % 2
        
        binario_list.append(resto)
        if decimal < 2:
            break
        
        decimal = decimal // 2
        
    binario_list = binario_list[::-1]
    for i in range(0, len(binario_list)):
            binario_str += str(binario_list[i])
    if octal:
        if len(binario_str) < 3:
            
            if len(binario_str) == 2:
                
                binario_str = f'0{binario_str}'
            if len(binario_str) == 1:
                binario_str = f'00{binario_str}'
    if hexadecimal:
        if len(binario_str) < 4:
            
            if len(binario_str) == 3:
                binario_str = f'0{binario_str}'
            if len(binario_str) == 2:
                binario_str = f'00{binario_str}'
            if len(binario_str) == 1:
                binario_str = f'000{binario_str}'
                
    return str(binario_str)

