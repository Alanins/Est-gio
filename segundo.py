### Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre###

def contar_letra_a(texto):
    # Converte o texto para minúsculas para facilitar a verificação
    texto = texto.lower()
    
    # Conta a quantidade de 'a's
    quantidade = texto.count('a')
    
    # Verifica se a letra 'a' está presente
    if quantidade > 0:
        print(f"A letra 'a' ocorre {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Exemplo de uso
string_exemplo = "A programação é uma arte."
contar_letra_a(string_exemplo)