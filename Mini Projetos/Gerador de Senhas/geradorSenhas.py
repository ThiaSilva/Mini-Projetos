chave = input("Digite a sua base de senha: ") # Pedido de entrada da base da senha (Chave)

senha = " " # Esta variavel de string vazia é criada para armazenar a senha gerada. A cada iteração do loop, caracteres serão adicionados a essa string.

for letra in chave: # Este loop percorre cada caractere (letra) da chave fornecida pelo usuário.
    if letra in "Aa": 
        senha = senha + "10" # A cada iteração, o caractere atual é adicionado à variavel senha.
    elif letra in "Bb": 
        senha = senha + "11"
    elif letra in "Cc": 
        senha = senha + "12"
    elif letra in "Dd": 
        senha = senha + "13"
    elif letra in "Ee": 
        senha = senha + "14"
    elif letra in "Ff": 
        senha = senha + "15"
    elif letra in "Rr": 
        senha = senha + "*"
    elif letra in "Ss": 
        senha = senha + "%"
    elif letra in "Mm": 
        senha = senha + "#"
    else:
        senha = senha + letra

print(senha) # Após todas as substituições, a senha final é impressa na tela.