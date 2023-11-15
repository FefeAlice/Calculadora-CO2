#Constantes
GASOLINA = 0.75
DIESEL = 0.85
ALCOOL = 0.78
GNV = 0.76
COMBPORKM = 3.7
EMISSAO = 0.83

#Input() adaptado para apenas números
def input_numero(texto="Insira seu número:", tipo="int"):
    try:
        if tipo == "int":
            return int(input(texto + " "))
        if tipo == "float":
            return float(input(texto + " "))
    except:
        print("Deve ser um número!")
        return input_numero(texto)

#Função usada no final do código (em caso de escolha "Privado")
def final_privado(res):
    if res == -1:
        print("Tente novamente.")
    elif res < 5:
        print(f"Sua emissão de CO2 é de: {res:.2f}. Por conseguir emitir menos de 5 kg de CO2, você acaba ganhando 15% de desconto na Declaração de Imposto de Renda do ano vigente.")
    else:
        print (f"Sua emissão de CO2 é de: {result:.2f}.")
        compensacao = input_numero("Por estar acima do recomendável, será necessária compensação por créditos de carbono.\n 1 - Fazenda Ouro Verde - Eunápolis, Bahia \n 2 - Fazenda Belo Horizonte - Potiguará, Bahia \n 3 - Entre Rios - Maracaçumé, Maranhão \n 4 - outra forma de compensação de carbono \nEscreva aqui:")
        if compensacao == 4:
            print("Você terá que pagar o valor de R$ 185,00 para uma empresa parceira de sua escolha, entre em contato com o suporte da empresa para emissão de boleto.")
        else:
            print("Para comprar os créditos de carbono do projeto solicitado se dirija até o endereço da organização ou entre em contato pelo número +55 21 3819-2166.")

#Função usada no final do código (em caso de escolha "Privado")
def final_publico(res):
    if res == -1:
        print("Tente novamente.")
    elif res < 100:
        print(f"Sua emissão de CO2 é de: {res:.2f}. Por conseguir emitir menos de 100 kg de CO2 por ônibus, sua empresa terá desconto na compra de créditos de carbono e nos impostos relacionados.")
    else: 
        print (f"Sua emissão de CO2 é de: {result:.2f}.")
        compensacao = input_numero("Sua frota emitiu mais CO2 do que o recomendável. Devido a isso será cobrado 15% de juros na receita da empresa e será necessária compensação por créditos de carbono.\n 1 - Fazenda Ouro Verde - Eunápolis, Bahia \n 2 - Fazenda Belo Horizonte - Potiguará, Bahia \n 3 - Entre Rios - Maracaçumé, Maranhão \n 4 - Outra forma de compensação de carbono \nEscreva aqui:")
        if compensacao == 4:
            print("Você terá que pagar o valor de R$ 5.000,00 para uma empresa parceira de sua escolha, entre em contato com o suporte da empresa para emissão de boleto.")
        else:
            print("Para comprar os créditos de carbono do projeto solicitado se dirija até o endereço da organização ou entre em contato pelo número +55 21 3819-2166.")

#Cálculo da relação quilômetro-litro
def quilometro_litro(publico_ou_privado):
    if publico_ou_privado == "publico":
        km = input_numero("Quantos km você roda por dia?:", "float")
        l = input_numero("Quantos litros você coloca?:", "float")
    elif publico_ou_privado == "privado":
        km = input_numero("Insira a distância percorrida pela sua frota em km:", "float")
        l = input_numero("Insira a quantidade de gasolina para cada ônibus em litros:", "float")
    return km / l


#Início
trans = input_numero("Olá! Bem-vindo. \nVocê busca calcular por transporte Privado ou Público? \n 1 - Privado \n 2 - Público \nEscreva aqui:")

#Em caso de escolha ("1 - Privado")
if trans == 1:
    esc = input_numero("Agora escolha o meio de transporte em que queira calcular o Crédito de Carbono: \n 1 - Carro \n 2 - Moto \n 3 - Van/Ônibus \nEscreva aqui o véiculo desejado:")
    
    #Em caso de escolha ("1 - Carro")
    if esc == 1:
        kml = quilometro_litro("publico")
        com = input_numero("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\nEscreva aqui qual o combústivel utilizado:")
        result = -1
        if com == 1:
            result = kml * EMISSAO * GASOLINA * COMBPORKM
        if com == 2:
            result = kml * EMISSAO * DIESEL * COMBPORKM
        if com == 3:
            result = kml * EMISSAO * ALCOOL * COMBPORKM
        if com == 4:
            result = kml * EMISSAO * GNV * COMBPORKM
        else:
            print("A opção selecionada não foi encontrada.")
        final_privado(result)

    #Em caso de escolha ("2 - Motos")
    if esc == 2:
        kml = quilometro_litro("publico")
        com = input_numero("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\nEscreva aqui qual o combústivel utilizado:")
        result = -1
        if com == 1:
            result = kml * EMISSAO * GASOLINA * COMBPORKM
        elif com == 2:
            result = kml * EMISSAO * DIESEL * COMBPORKM
        elif com == 3:
            result = kml * EMISSAO * ALCOOL * COMBPORKM
        elif com == 4:
            result = kml * EMISSAO * GNV * COMBPORKM
        else:
            print("A opção selecionada não foi encontrada.")
        final_privado(result)

    #Em caso de escolha ("3 - Van/Ônibus")
    if esc == 3:
        kml = quilometro_litro("publico")
        com = input_numero("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\nEscreva aqui qual o combústivel utilizado:")
        result = -1
        if com == 1:
            result = kml * EMISSAO * GASOLINA * COMBPORKM
        elif com == 2:
            result = kml * EMISSAO * DIESEL * COMBPORKM
        elif com == 3:
            result = kml * EMISSAO * ALCOOL * COMBPORKM
        elif com == 4:
            result = kml * EMISSAO * GNV * COMBPORKM
        else:
            print("A opção selecionada não foi encontrada.")
        final_privado(result)

#Em caso de escolha ("2 - Público")
elif trans == 2:
    frota = input_numero("Essa seção é feita para empresas. \nPara calcular a emissão de CO2 da sua empresa insira aqui a quantidade de frota (unidades) em uso:")
    kml = quilometro_litro("privado")
    com = input_numero("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\nEscreva aqui qual o combústivel utilizado:", "float")
    result = -1
    if com == 1:
        result = frota * kml * EMISSAO * GASOLINA * COMBPORKM
    elif com == 2:
        result = frota * kml * EMISSAO * DIESEL * COMBPORKM
    elif com == 3:
        result = frota * kml * EMISSAO * ALCOOL * COMBPORKM
    elif com == 4:
        result = frota * kml * EMISSAO * GNV * COMBPORKM
    else:
        print("A opção selecionada não foi encontrada.")
    final_publico(result)

#Caso o usuário escolha algo que não 1 ou 2
else:
    print ("A opção selecionada não foi encontrada. Por favor, feche o programa e o abra novamente para voltar ao inicio.")