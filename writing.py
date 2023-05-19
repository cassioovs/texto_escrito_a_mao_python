import pywhatkit as kit

# Espaço dedicado para o seu texto
texto = '''
Escreva seu texto aqui :)
'''
# Gera imagem com texto escrito
kit.text_to_handwriting(texto, save_to='texto_escrito_a_mao.png')