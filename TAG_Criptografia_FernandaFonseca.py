'''
PROCESSO SELETIVO - Grupo de Resposta a Incidentes de Segurança

Nome: Fernanda Veiga Gomes da Fonseca
TAG - Criptografia - Entrega: 29/02/2020
'''

# Crypto Challenge Set 1 - https://cryptopals.com/sets/1

## 1- Convert hex to base64

'''
Após ler o enunciado do problema, minha primeira ideia foi tranformar a string em hexadecimal em uma string em binário (base2),
porque a equivalência para a base64 é de 6 bits (2⁶ = 64 possíveis caracteres).
Uma vez que poderiam ser úteis futuramente, decidi utilizar duas funções (uma para converter a string para base2 e outra, o resultado da primeira para base64).
'''

def hex_para_bits (string_hex):
    '''
    A função hex_para_bits converte uma string string_hex em hexadecimal em uma string string_bits de bits.
    '''
    
    string_bits = '' # Valor inicial da string que será retornada pela função.
    
    for elemento in string_hex:
        '''
        A equivalência de cada caracter em hexadecimal para binário é de 4 bits (2⁴ = 16 caracteres hexadecimais, 0 -> f),
        onde o valor hexadecimal de cada caracter é igual à soma das potências de 2 para cada bit (por exemplo, 'a' = 10 = 1*2³ + 0*2² + 1*2¹ + 0*2⁰).
        '''
        
        if elemento == '0':
            string_bits += '0000'
            
        elif elemento == '1':
            string_bits += '0001'
            
        elif elemento == '2':
            string_bits += '0010'
        
        elif elemento == '3':
            string_bits += '0011'

        elif elemento == '4':
            string_bits += '0100'

        elif elemento == '5':
            string_bits += '0101'

        elif elemento == '6':
            string_bits += '0110'

        elif elemento == '7':
            string_bits += '0111'

        elif elemento == '8':
            string_bits += '1000'

        elif elemento == '9':
            string_bits += '1001'

        elif elemento == 'a' or elemento == 'A': # O enunciado fornece uma string com caracteres não-numérios minúsculos, porém optei por analisar de maneira geral.
            string_bits += '1010'

        elif elemento == 'b' or elemento == 'B':
            string_bits += '1011'

        elif elemento == 'c' or elemento == 'C':
            string_bits += '1100'

        elif elemento == 'd' or elemento == 'D':
            string_bits += '1101'

        elif elemento == 'e' or elemento == 'E':
            string_bits += '1110'

        elif elemento == 'f' or elemento == 'F':
            string_bits += '1111'

        else:
            '''
            Apesar de a string dada não conter caracteres fora do intervalo 0 -> f,
            decidi deixar uma condição para analisar casos com erros de digitação na string de entrada.
            
            Um caracter fora do intervalo não compromete a análise dos demais.
            O erro pode ser corrigido atentando-se para a posição do alerta e alterando o caracter na mesma da string de entrada.
            '''
            
            string_bits += ('#Erro!#')
            
    return string_bits

def bits_para_base64 (string_bits):
    '''
    A função bits_para_base64 converte uma string string_bits de bits em uma string string_base64 na base 64.
    '''
    
    string_base64 = '' # Valor inicial da string que será retornada pela função.
    
    string_conversao = string_bits # String de entrada a ser convertida.    
    numero_bytes = len (string_bits) % 8 # O número de bytes corresponde ao número de blocos de 8 bits na string.
    
    '''
    Caso a string original provenha de uma string em hexadecimal, possui um número de bits múltiplo de 4, mas, de maneira geral, 
    pode-se entender que o número de bits é múltiplo de 8, porque equivale ao número de bytes. 
    Entretanto, na conversão para a base 64, devemos dividir a string em blocos de 6 bits (2⁶ = 64 possibilidades).
    
    Dessa forma, a string a ser convertida (parâmetro da função) deve ser um múltiplo de 24 (MMC (6, 8)).
        Caso a string tenha n + 8 bits, devemos acrescentar 2 bytes de valor zero, onde n é divisível por 24.
        Caso a string tenha n + 16 bits, devemos acrescentar 1 byte de valor zero, onde n é divisível por 24.
    '''
    
    if numero_bytes % 24 != 0: # Verifica se a string possui um número de bits múltiplo de 24.
        if numero_bytes % 24 == 8:
            string_conversao = string_bits + '0000000000000000' # Acrescentar 2 bytes de valor zero.
            
        elif numero_bytes % 24 == 16:
            string_conversao = string_bits + '00000000' # Acrescentar 1 byte de valor zero.
    
    '''
    Comparações feitas com base na tabela de conversão (fonte: https://pt.wikipedia.org/wiki/Base64),
    onde os valores decimais foram convertidos em suas formas binárias separadamente utilizando o método de divisões sucessivas por 2.
    '''
    
    for i in range (0, len (string_conversao), 6):
        '''
        A equivalência para cada caracter na base 64 é de 6 bits.
        '''
        
        bloco = string_conversao [i:i+6] # Bloco de 6 bits.
        
        if bloco == '000000':
            '''
            Segundo a regra de conversão para base 64, devem ser adicionados bytes de valor zero nos casos descritos nas linhas 101 a 109.
            Também, caso o último bloco de 6 bits da string tenha valor zero, o valor atribuído a eles corresponde ao caracter '='.
            Caso não seja o último bloco de 6 bits da string, o valor atribuído a ele segue a tabela de conversão (no caso, corresponderá ao caracter 'A').
            '''
            
            if (i+5) != (len (string_conversao) - 1): # Verifica se o índice do último bit do bloco é igual ao índice do último bit da string.
                string_base64 += 'A'
                
            else:
                string_base64 += '='
                
        elif bloco == '000001':
            string_base64 += 'B'
            
        elif bloco == '000010':
            string_base64 += 'C'
            
        elif bloco == '000011':
            string_base64 += 'D'
            
        elif bloco == '000100':
            string_base64 += 'E'
            
        elif bloco == '000101':
            string_base64 += 'F'
            
        elif bloco == '000110':
            string_base64 += 'G'
            
        elif bloco == '000111':
            string_base64 += 'H'
            
        elif bloco == '001000':
            string_base64 += 'I'
            
        elif bloco == '001001':
            string_base64 += 'J'
            
        elif bloco == '001010':
            string_base64 += 'K'
            
        elif bloco == '001011':
            string_base64 += 'L'
            
        elif bloco == '001100':
            string_base64 += 'M'
            
        elif bloco == '001101':
            string_base64 += 'N'
            
        elif bloco == '001110':
            string_base64 += 'O'
            
        elif bloco == '001111':
            string_base64 += 'P'
            
        elif bloco == '010000':
            string_base64 += 'Q'
            
        elif bloco == '010001':
            string_base64 += 'R'
            
        elif bloco == '010010':
            string_base64 += 'S'
            
        elif bloco == '010011':
            string_base64 += 'T'
            
        elif bloco == '010100':
            string_base64 += 'U'
            
        elif bloco == '010101':
            string_base64 += 'V'
            
        elif bloco == '010110':
            string_base64 += 'W'
            
        elif bloco == '010111':
            string_base64 += 'X'
            
        elif bloco == '011000':
            string_base64 += 'Y'
            
        elif bloco == '011001':
            string_base64 += 'Z'
            
        elif bloco == '011010':
            string_base64 += 'a'
            
        elif bloco == '011011':
            string_base64 += 'b'
            
        elif bloco == '011100':
            string_base64 += 'c'
            
        elif bloco == '011101':
            string_base64 += 'd'
            
        elif bloco == '011110':
            string_base64 += 'e'
            
        elif bloco == '011111':
            string_base64 += 'f'
            
        elif bloco == '100000':
            string_base64 += 'g'
            
        elif bloco == '100001':
            string_base64 += 'h'
            
        elif bloco == '100010':
            string_base64 += 'i'
            
        elif bloco == '100011':
            string_base64 += 'j'
            
        elif bloco == '100100':
            string_base64 += 'k'
            
        elif bloco == '100101':
            string_base64 += 'l'
            
        elif bloco == '100110':
            string_base64 += 'm'
            
        elif bloco == '100111':
            string_base64 += 'n'
            
        elif bloco == '101000':
            string_base64 += 'o'
            
        elif bloco == '101001':
            string_base64 += 'p'
            
        elif bloco == '101010':
            string_base64 += 'q'
            
        elif bloco == '101011':
            string_base64 += 'r'
            
        elif bloco == '101100':
            string_base64 += 's'
            
        elif bloco == '101101':
            string_base64 += 't'
            
        elif bloco == '101110':
            string_base64 += 'u'
            
        elif bloco == '101111':
            string_base64 += 'v'
            
        elif bloco == '110000':
            string_base64 += 'w'
            
        elif bloco == '110001':
            string_base64 += 'x'
            
        elif bloco == '110010':
            string_base64 += 'y'
            
        elif bloco == '110011':
            string_base64 += 'z'
            
        elif bloco == '110100':
            string_base64 += '0'
            
        elif bloco == '110101':
            string_base64 += '1'
            
        elif bloco == '110110':
            string_base64 += '2'
            
        elif bloco == '110111':
            string_base64 += '3'
            
        elif bloco == '111000':
            string_base64 += '4'
            
        elif bloco == '111001':
            string_base64 += '5'
            
        elif bloco == '111010':
            string_base64 += '6'
            
        elif bloco == '111011':
            string_base64 += '7'
            
        elif bloco == '111100':
            string_base64 += '8'
            
        elif bloco == '111101':
            string_base64 += '9'
            
        elif bloco == '111110':
            string_base64 += '+'
            
        elif bloco == '111111':
            string_base64 += '/'
            
        else:
            '''
            Assim como na função hex_para_bits, decidi deixar uma condição para analisar casos com erros de digitação na string de entrada.
            
            Um caracter diferente de 0 ou 1 não compromete a análise dos demais.
            O erro pode ser corrigido atentando-se para a posição do alerta, alterando o dígito na mesma da string de entrada.
            '''
            
            string_base64 += '#Erro!#'
            
    return string_base64         


### Teste
string_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d' # String dada no enunciado.

'''
#1 Conversão da string dada para uma string de bits.
#2 Conversão para uma string na base 64.
#3 O resultado obtido foi comparado com a string também fornecida pelo enunciado do problema.
'''

string_bits = hex_para_bits (string_hex) #1
string_base64 = bits_para_base64 (string_bits) #2

if string_base64 == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t': #3
    print ('1- Correto!')
    
else:
    print ('1- Incorreto!')



## 2- Fixed XOR
'''
Lembrete -> XOR: ¬A·B + A·¬B, onde A e B são bits (0 ou 1).
'''

def xor_strings_bits (a, b):
    '''
    A função xor_strings_bits realiza o XOR de duas strings em hexadecimal e de mesmo tamanho.
    A string retornada (resultado) é uma string de bits.
    '''
    
    resultado = '' # Valor inicial da string que será retornada pela função.
    
    '''
    No problema, é necessário realizar um XOR de strings.
    Como as strings dadas estão em hexadecimal, primeiro elas devem ser transformadas em strings de bits para que a operação seja feita bit a bit.
    '''
    
    a_bits = hex_para_bits (a)
    b_bits = hex_para_bits (b)
    
    '''
    Todos os bits das strings geradas acima são percorridos.
    Os bits de mesmo índice nas strings são utilizados para a realização do XOR.
    O resultado de cada operação é adicionado ao final da mesma na string a ser retornada pela função.
    '''
    
    for i in range (0, len (a_bits)): # OU tamanho = len (b_bits)
        bit_a = int (a_bits [i])
        bit_b = int (b_bits [i])
        
        resultado += str (int (not (bit_a) and bit_b or bit_a and not (bit_b)))
        
    return resultado

def bits_para_hex (string_bits):
    '''
    A função bits_para_hex converte uma string string_bits de bits em uma string string_hex em hexadecimal.
    '''
    
    '''
    Considerando que havia sido necessária uma função de conversão hexadecimal para binário no problema anterior,
    pensei em alterar a mesma para que também realizasse a operação inversa, necessária para o atual problema.
    A alteração estaria resumida na utilização de estruturas como dicionários ou listas de listas (ou tuplas) para o mapeamento das correspondências de valores.
    
    Porém, uma vez que a função hex_para_bits já havia sido feita, decidi não descartá-la, fazendo uma função separada para a conversão binário para hexadecimal.
    '''
    
    string_hex = '' # Valor inicial da string que será retornada pela função.
    
    for i in range (0, len (string_bits), 4):
        '''
        O raciocínio empregado é oposto ao utilizado na função hex_para_bits: aqui, foram mapeados blocos de 4 bits para cada caracter hexadecimal.
        '''
        
        bloco = string_bits [i:i+4] # Bloco de 4 bits.
        
        if bloco == '0000':
            string_hex += '0'
            
        elif bloco == '0001':
            string_hex += '1'
            
        elif bloco == '0010':
            string_hex += '2'
            
        elif bloco == '0011':
            string_hex += '3'
            
        elif bloco == '0100':
            string_hex += '4'
            
        elif bloco == '0101':
            string_hex += '5'
            
        elif bloco == '0110':
            string_hex += '6'
            
        elif bloco == '0111':
            string_hex += '7'
            
        elif bloco == '1000':
            string_hex += '8'
            
        elif bloco == '1001':
            string_hex += '9'
            
        elif bloco == '1010':
            string_hex += 'a'
            
        elif bloco == '1011':
            string_hex += 'b'
            
        elif bloco == '1100':
            string_hex += 'c'
            
        elif bloco == '1101':
            string_hex += 'd'
            
        elif bloco == '1110':
            string_hex += 'e'
            
        elif bloco == '1111':
            string_hex += 'f'

        else:
            '''
            Conforme padrão utilizado nas funções anteriores, decidi deixar uma condição para analisar casos com erros de digitação na string de entrada.
            
            Um caracter diferente de 0 ou 1 no bloco de 4 bits não compromete a análise dos demais blocos.
            O erro pode ser corrigido alterando o dígito na string de entrada.
            '''
            
            string_hex += ('#Erro!#')

    return string_hex


### Teste
a = '1c0111001f010100061a024b53535009181c' # 1ª string dada no enunciado.
b = '686974207468652062756c6c277320657965' # 2ª string dada no enunciado.

'''
#1 XOR entre as strings a e b.
#2 Conversão da string obtida pelo XOR em uma string em hexadecimal.
#3 Comparação com a 3ª string fornecida pelo enunciado do problema.
'''

string_xor = xor_strings_bits (a, b) #1
string_hex = bits_para_hex (string_xor) #2

if string_hex == '746865206b696420646f6e277420706c6179': #3
    print ('2- Correto!')
    
else:
    print ('2- Incorreto!')
    
    
    
## 3- Single-byte XOR cipher    
'''
O objetivo do desafio é analisar todos os resultados de um XOR entre uma string dada no enunciado e um caracter ASCII desconhecido,
com base na frequência de caracteres da língua inglesa (fonte: https://en.wikipedia.org/wiki/Letter_frequency).

Meu raciocício está resumido nos seguintes pontos:
        1- Utilizar a função xor_strings_bits do desafio anterior.
        2- Como a função tem como parâmetros strings em hexadecimal, o caracter ASCII deve ser convertido em hexadecimal (a string do enunciado já está em hexadecimal).
           Os caracteres ASCII vão de 0 a 255. Como estão em decimal, preciso de uma função que realize a conversão.
        3- Como cada caracter ASCII corresponde a dois dígitos hexadecimais, o XOR com a string dada no enunciado deve ser feita em duplas para cada um deles.
        4- Todas as possibilidades obtidas pelo XOR devem estar no formato ASCII para a análise da frequência de caracteres.
        5- Com base nas frequências, foram atribuídas pontuações para cada possibilidade.
        6- A possibilidade com maior pontuação é a resposta do desafio.
'''
    
def decimal_para_hex (numero):
    '''
    A função decimal_para_hex converte um valor decimal (numero) uma string string_hex em hexadecimal.
    '''
    
    '''
    Primeiro, decidi converter o parâmetro da função em seu equivalente binário.
    Usei o método format, porém ele não retorna os bits nulos à esquerda para completar o byte mais significativo.
    Por isso, realizei uma verificação para adicionar bits 0 à esquerda para tal fim.
    '''
    
    auxiliar = format (numero, 'b') # Equivalente binário do valor decimal.
    
    if len (auxiliar) % 8 != 0:
        binario = '0'*(8 - len (auxiliar) % 8) + auxiliar
    
    else:
        binario = auxiliar
        
    '''
    Em seguida, utilizei o valor binário obtido acima como parâmetro da função de conversão binário para hexadecimal.
    '''
        
    string_hex = bits_para_hex (binario)
    
    return string_hex

def xor_string_caract (string_hex):
    '''
    Função que retorna os possíveis resultados em hexadecimal de um XOR entre uma string string_hex em hexadecimal e um caracter ASCII desconhecido (256 possibilidades).
    '''
    
    '''
    Foi realizado um XOR entre uma string em hexadecimal e um caracter ASCII.
    Dessa forma, a ideia foi verificar todas as possibilidades de resultado que o XOR poderia gerar.
    
    Há 256 possibilidades de caracteres ASCII. Por isso, seu equivalente binário tem 8 bits.
    Como a função xor_strings_bits deve receber duas strings em hexadecimal de mesmo tamanho e cada caracter ASCII corresponde a dois dígitos hexadecimais,
    a string string_hex deve ser mapeada em duplas (dois dígitos hexadecimais) para a realização do XOR com cada possível caracter ASCII.
    
    Cada XOR é adicionado a uma string possib.
    Após percorrer toda a extensão de string_hex para um dado caracter ASCII, possib é adicionada a uma lista de todos os resultados possíveis de XOR,
    a qual será retornada pela função.
    '''
    
    possibilidades = [] # Valor inicial da lista que será retornada pela função.
    
    for posicao in range (0, 256):
        '''
        O XOR é realizado com todos os possíveis caracteres ASCII.
        '''
        
        caract = decimal_para_hex (posicao) # Ponto nº 2.
        possib = '' # Valor inicial da possibilidade que será adicionada à lista de possibilidades.
        
        for i in range (0, len (string_hex), 2): # Ponto nº 3.
            '''
            Conforme explicação contida nas linhas 554 a 556, a string string_hex deve ser analisada em duplas.
            '''
            
            byte = string_hex [i:i+2] # Um byte da string, ou seja, dois dígitos hexadecimais.

            possib += xor_strings_bits (byte, caract) # Ponto nº 1.
            
        possibilidades += [bits_para_hex (possib)]
        
    return possibilidades

def byte_para_decimal (string_byte):
    '''
    Função que converte uma string string_byte de 8 bits em seu decimal correspondente.
    '''
    
    decimal = 0 # Valor inicial do número decimal que será retornado pela função.
    
    for i in range (0, len (string_byte)):
        '''
        Calcula o decimal correspondente através da soma das potências de 2 para cada bit.
        '''
        
        bit = int (string_byte [i])
        peso = len (string_byte) - 1 - i
        
        decimal += bit*2**peso
        
    return decimal

def mais_possivel (possibilidades):
    '''
    Função que determina um texto mais possível no formato ASCII a partir de uma lista (possibilidades) de strings em hexadecimal.
    '''
    
    '''
    As strings geradas pela função xor_string_caract () estão no formato hexadecimal.
    A seguir, todas foram convertidas em binário e armazenadas em uma nova lista (possibilidades_bits).
    '''

    possibilidades_bits = []
    
    for possib in possibilidades:
        possibilidades_bits += [hex_para_bits (possib)]
        
    '''
    Como há 256 caracteres ASCII, as possibilidades em bits devem ser mapeadas em bytes para realizar a equivalência.
    
    O dicionário abaixo foi montado por mim a partir de uma tabela da internet (fonte: https://theasciicode.com.ar/ascii-codes.txt),
    porque não encontrei um método no Python que realizasse o mapeamento das 256 possibilidades (encontrei um módulo - binascii -, porém mapeia apenas 100 caracteres).
    '''
    
    dicio_ascii = {0: 'NUL', 1: 'SOH', 2: 'STX', 3: 'ETX', 4: 'EOT', 5: 'ENQ', 6: 'ACK', 7: 'BEL',
                   8: 'BS', 9: 'HT', 10: 'LF', 11: 'VT', 12: 'FF', 13: 'CR', 14: 'SO', 15: 'SI',
                   16: 'DLE', 17: 'DC1', 18: 'DC2', 19: 'DC3', 20: 'DC4', 21: 'NAK', 22: 'SYN',
                   23: 'ETB', 24: 'CAN', 25: 'EM', 26: 'SUB', 27: 'ESC', 28: 'FS', 29: 'GS', 30: 'RS',
                   31: 'US', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'",
                   40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0',
                   49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 
                   58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B',
                   67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K',
                   76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T',
                   85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '/\/', 93: ']',
                   94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f',
                   103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o',
                   112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x',
                   121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 127: 'DEL', 128: 'Ç', 129: 'ü',
                   130: 'é', 131: 'â', 132: 'ä', 133: 'à', 134: 'å', 135: 'ç', 136: 'ê', 137: 'ë', 138: 'è',
                   139: 'ï', 140: 'î', 141: 'ì', 142: 'Ä', 143: 'Å', 144: 'É', 145: 'æ', 146: 'Æ', 147: 'ô',
                   148: 'ö', 149: 'ò', 150: 'û', 151: 'ù', 152: 'ÿ', 153: 'Ö', 154: 'Ü', 155: 'ø', 156: '£',
                   157: 'Ø', 158: '×', 159: 'ƒ', 160: 'á', 161: 'í', 162: 'ó', 163: 'ú', 164: 'ñ', 165: 'Ñ',
                   166: 'ª', 167: 'º', 168: '¿', 169: '®', 170: '¬', 171: '½', 172: '¼', 173: '¡', 174: '«',
                   175: '»', 176: '░', 177: '▒', 178: '▓', 179: '│', 180: '┤', 181: 'Á', 182: 'Â', 183: 'À',
                   184: '©', 185: '╣', 186: '║', 187: '╗', 188: '╝', 189: '¢', 190: '¥', 191: '┐', 192: '└',
                   193: '┴', 194: '┬', 195: '├', 196: '─', 197: '┼', 198: 'ã', 199: 'Ã', 200: '╚', 201: '╔',
                   202: '╩', 203: '╦', 204: '╠', 205: '═', 206: '╬', 207: '¤', 208: 'ð', 209: 'Ð', 210: 'Ê',
                   211: 'Ë', 212: 'È', 213: 'ı', 214: 'Í', 215: 'Î', 216: 'Ï', 217: '┘', 218: '┌', 219: '█',
                   220: '▄', 221: '¦', 222: 'Ì', 223: '▀', 224: 'Ó', 225: 'ß', 226: 'Ô', 227: 'Ò', 228: 'õ',
                   229: 'Õ', 230: 'µ', 231: 'þ', 232: 'Þ', 233: 'Ú', 234: 'Û', 235: 'Ù', 236: 'ý', 237: 'Ý',
                   238: '¯', 239: '´', 240: '¬', 241: '±', 242: '‗', 243: '¾', 244: '¶', 245: '§', 246: '÷',
                   247: '¸', 248: '°', 249: '¨', 250: '•', 251: '¹', 252: '³', 253: '²', 254: '■', 255: 'nbsp'}
        
    '''
    Conversão das possíveis strings para o formato ASCII.
    '''
    
    textos = []
    
    for possib_bits in possibilidades_bits:
        texto = ''
        
        for i in range (0, len (possib_bits), 8):
            '''
            Como o dicionário montado mapeia os caracteres ASCII de acordo com seus decimais,
            cada byte contido na possibilidade possib_bits na lista possibilidades_bits foi convertido em seu decimal correspondente,
            utilizando a função byte_para_decimal, para identificar o caracter ASCII correspondente.
            '''
            
            byte = possib_bits [i:i+8] # Um byte da string.
            decimal = byte_para_decimal (byte) # Decimal correspondente ao byte.
            
            texto += dicio_ascii [decimal]
            
        textos += [texto] # Ponto nº 4.
        
    '''
    As possibilidades foram analisadas segundo a frequência de caracteres na língua inglesa.
    '''
    
    caract_frequencias = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 
                          'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 
                          'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 
                          'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 
                          'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974, 
                          'z': .00074, ' ': .13000}
    
    pontuacao = [] # Valor inicial da lista com pontuações de cada possibilidade.

    for texto in textos:
        pontuacao_texto = 0 # Pontuação inicial da possibilidade texto da lista com possibilidades no formato ASCII.
        
        for caracter in texto:
            if caracter in caract_frequencias: # Foi atribuída pontuação apenas para caracteres tradicionais, contidos em caract_frequencias.
                pontuacao_texto += caract_frequencias [caracter]
            
        pontuacao += [pontuacao_texto] # Ponto nº 5.
        
    maior_pontuacao = max (pontuacao) # Ponto nº 6.
    
    indice = pontuacao.index (maior_pontuacao)
    caract_ascii = dicio_ascii [indice] # Caracter ASCII usado no XOR com a string fornecida pelo enunciado que resultou na possibilidade com maior pontuação.
        
    return (indice, textos [indice], caract_ascii)

### Teste
string_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736' # String dada no enunciado.

mais_possivel_ascii = mais_possivel (xor_string_caract (string_hex)) # Possibilidade com maior pontuação.

print ('3- Mensagem: ' + mais_possivel_ascii [1] + '; caracter ASCII: ' + mais_possivel_ascii [2])