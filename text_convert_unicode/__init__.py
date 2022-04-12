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

def binario_decimal(numero_binario):
    #bin_str_list = str(valor_binario).strip().replace(""," ").split()
    bin_str_list = [*str(numero_binario)]
    potencia = len(bin_str_list)
    decimal = 0
    for i in range(0, len(bin_str_list)):
        potencia -= 1
        decimal += int(bin_str_list[i]) * (2 ** potencia)
        
    return int(decimal)


def tcu(text=str,show=False, reverse=False):
    """
    TEXT CONVERT UNICODE

    Args:
        text (_type_, required): text convert. Defaults to str.
        show (bool, optional): show details. Defaults to False.
        reverse (bool, optional): show reverse details. Defaults to False.

    Returns:
        _type_: list
    - Consult Table https://pt.wikipedia.org/wiki/ASCII
    """
    
    name = str(text).strip()
    unicode_list = list()
    count = 0
    character = 'CHARACTER'
    ascII = 'ASCII'
    binary = 'BINARY'
    hexx = 'HEX'
    text_char = ""
    text_binary = ""
    delimiter = 90
    list_obj = list()
    dict_obj = dict()
    binary_list = list()
    ascii_list = list()
    char_list = list()
    hex_list = list()
    
    for i in range(len(name)):
        try:
            while True:
                if name[i] == chr(count): # limite chr 0x10ffff
                    unicode_list.append(count)
                    count = 0
                    break
                
                count += 1
        except ValueError as err:
            print(err) 
    
    if show:
        
        print('-'* delimiter)
        print(f'{"TEXT CONVERT UNICODE": ^{delimiter}}')
        print('-'* delimiter)
        
        
        if reverse:
            
            print(f"{binary: ^20} {ascII: ^20} {hexx: ^20} {character: ^20}\n")
            
            for i in range(len(unicode_list)):
                text_char += chr(unicode_list[i])
                text_binary += str(decimal_binario(unicode_list[i]))
                #sleep(.4)
                print(f"{decimal_binario(unicode_list[i]): ^20} {unicode_list[i]: ^20} {binario_hexadecimal(decimal_binario(unicode_list[i]),binario_decimal): ^20} {chr(binario_decimal(decimal_binario(unicode_list[i]))): ^20}")
            #sleep(1)
            
            print('-'* delimiter)
            print(f'{text_binary} ==> {text_char}')
            print('-'* delimiter)
            
        else:
            
            print(f"{character: ^20} {ascII: ^20} {hexx: ^20} {binary: ^20}\n")
            
            for i in range(len(unicode_list)):
                text_char += chr(unicode_list[i])
                text_binary += str(decimal_binario(unicode_list[i]))
                #sleep(.4)
                print(f"{chr(unicode_list[i]): ^20} {unicode_list[i]: ^20} {binario_hexadecimal(decimal_binario(unicode_list[i]),binario_decimal): ^20} {decimal_binario(unicode_list[i]): ^20}")
            #sleep(1)
            print('-'* delimiter)
            print(f'{text_char} ==> {text_binary}')
            print('-'* delimiter)
            
    for i in range(0, len(unicode_list)):
        ascii_list.append(unicode_list[i])
        char_list.append(chr(unicode_list[i]))
        binary_list.append(decimal_binario(unicode_list[i]))
        hex_list.append(binario_hexadecimal(decimal_binario(unicode_list[i]),binario_decimal))
        
    dict_obj['ascii_list'] = ascii_list
    dict_obj['char_list'] = char_list
    dict_obj['binary_list'] = binary_list
    dict_obj['hex_list'] = hex_list
    list_obj.append(dict_obj)
    
    return list_obj
