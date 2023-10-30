def input_numero(texto="Insira seu texto aqui:", tipo="int"):
    try:
        if tipo == "int":
            return int(input(texto + " "))
        if tipo == "float":
            return float(input(texto + " "))
    except:
        print("Deve ser um numero")
        return input_numero(texto)

def final_privado(res):
    if res < 5:
        print(f"Sua emissão de CO2 é de: {res:.2f}. Por conseguir emitir menos de 5 kg de CO2, você acaba ganhando 15% de desconto na Declaração de Imposto de Renda do ano vigente")
    else:
        print (f"Sua emissão de CO2 é de: {result:.2f}.")
        compensacao = input_numero("Por estar acima do recomendável, será necessária compensação por créditos de carbono.\n 1 - Fazenda Ouro Verde - Eunápolis, Bahia \n 2 - Fazenda Belo Horizonte - Potiguará, Bahia \n 3- Entre Rios - Maracaçumé, Maranhão \n 4 - outra forma de compensação de carbono \n Escreva aqui:")
        if compensacao == 4:
            print("Você terá que pagar o valor de R$ 185,00 para uma empresa parceira de sua escolha, entre em contato com o suporte da empresa para emissão de boleto.")
        else:
            print("Para comprar os créditos de carbono do projeto solicitado se dirija até o endereço da organização ou entre em contato pelo número", end="")
            if compensacao == 1:
                print("+55 21 3819-2166")
            if compensacao == 2:
                print("+55 21 3819-2166")
            if compensacao == 3:
                print("+55 21 3819-2166")

def final_publico(res):
    if res < 100:
        print(f"Sua emissão de CO2 é de: {res:.2f}. Por conseguir emitir menos de 100 kg de CO2 por ônibus, sua empresa terá desconto na compra de créditos de carbono e nos impostos relacionados.")
    else: 
        print (f"Sua emissão de CO2 é de: {result:.2f}.")
        compensacao = input_numero("Sua frota emitiu mais CO2 do que o recomendável. Devido a isso será cobrado 15% de juros na receita da empresa e será necessária compensação por créditos de carbono.\n 1 - Fazenda Ouro Verde - Eunápolis, Bahia \n 2 - Fazenda Belo Horizonte - Potiguará, Bahia \n 3- Entre Rios - Maracaçumé, Maranhão \n 4 - Outra forma de compensação de carbono \n Escreva aqui:")
        if compensacao == 4:
            print("Você terá que pagar o valor de R$ 5.000,00 para uma empresa parceira de sua escolha, entre em contato com o suporte da empresa para emissão de boleto.")
        else:
            print("Para comprar os créditos de carbono do projeto solicitado se dirija até o endereço da organização ou entre em contato pelo número", end="")
            if compensacao == 1:
                print("+55 21 3819-2166")
            if compensacao == 2:
                print("+55 21 3819-2166")
            if compensacao == 3:
                print("+55 21 3819-2166")

def quilometro_litro():
    km = input_numero("Quantos km você roda por dia?: ", "float")
    l = input_numero("Quantos litros você coloca?: ", "float")
    return km / l

trans = input_numero("Olá! Bem-vindo. \n Você busca calcular por transporte Privado ou Público? \n 1 - Privado \n 2 - Público \n Escreva aqui:")

if trans == 1:
    esc = input_numero("Agora escolha o meio de transporte em que queira calcular o Crédito de Carbono: \n 1 - Carro \n 2 - Van/Ônibus \n Escreva aqui o véiculo desejado:")
    if esc == 1:
        kml = quilometro_litro()
        com = input_numero("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado:")
        if com == 1:
            result = kml*0.83*0.75*3.7
            final_privado(result)
        if com == 2:
            result = kml*0.83*0.85*3.7
            final_privado(result)
        if com == 3:
            result = kml*0.83*0.78*3.7
            final_privado(result)
        if com == 4:
            result = kml*0.83*0.76*3.7
            final_privado(result)

    if esc == 2:
        kml = quilometro_litro()
        com = int(input("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado:"))
        if com == 1:
            result = kml*0.83*0.75*3.7
            final_privado(result)
        if com == 2:
            result = kml*0.83*0.85*3.7
            final_privado(result)
        if com == 3:
            result = kml*0.83*0.78*3.7
            final_privado(result)
        if com == 4:
            result = kml*0.83*0.76*3.7
            final_privado(result)

if trans == 2:
    frota = input_numero("Essa seção é feita para empresas \n Para calcular a emissão de CO2 da sua empresa insira aqui a quantidade de frota (unidades) em uso:")
    km = float(input("Insira a distância percorrida pela sua frota em km: "))
    l = float(input("Insira a quantidade de gasolina para cada ônibus em litros: "))
    kml = km/l
    com = int(input("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado:"))
    if com == 1:
        result = frota*kml*0.83*0.75*3.7
        final_publico(result)
    if com == 2:
        result = frota*kml*0.83*0.85*3.7
        final_publico(result)
    if com == 3:
        result = frota*kml*0.83*0.78*3.7
        final_publico(result)
    if com == 4:
        result = frota*kml*0.83*0.76*3.7
        final_publico(result)

else:
    print ("A opção selecionada não foi encontrada. Por favor, feche o programa e o abra novamente para voltar ao inicio")