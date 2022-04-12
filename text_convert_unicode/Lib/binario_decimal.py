
def binario_decimal(numero_binario):
    #bin_str_list = str(valor_binario).strip().replace(""," ").split()
    bin_str_list = [*str(numero_binario)]
    potencia = len(bin_str_list)
    decimal = 0
    for i in range(0, len(bin_str_list)):
        potencia -= 1
        decimal += int(bin_str_list[i]) * (2 ** potencia)
        
    return int(decimal)
