#mostrar o maior valor 
matriz=[[5,7,8],[1,2,4],[6,3,9]]
soma=0
for linha in range(3):
    for coluna in range(3):
        soma = soma + matriz[linha][coluna]
    print(soma)