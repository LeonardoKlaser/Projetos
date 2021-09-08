"""
exemplo conta para validar cpfs
cpf exemplo = 168.995.350-09
somar os resultados da contas a seguir:
1x10                            1x11
6x9                             6x10
8x8                             8x9
9x7                             9x8
9x6                             9x7
5x5                             5x6
3x4                             3x5
5x3                             5x4
0x2                             0x3
=                               0x2
297                             =343
11 - (297 % 11) = 11           11- (343 % 11) = 9
11> 9 = 0
digito 1 = 0                    digito 2 = 9

"""


# Loop do CPF
while True:
    cpf = input("Digite um CPF: ")
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9,
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print("CPF valido")
    else:
        print("CPF invalido")