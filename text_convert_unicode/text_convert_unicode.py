from time import sleep
from Lib.decimal_binario import decimal_binario
from Lib.binario_decimal import binario_decimal
from Lib.binario_hexadecimal import binario_hexadecimal

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

