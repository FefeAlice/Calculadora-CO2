trans=int(input("Olá! Bem-vindo. \n Você busca calcular por transporte Privado ou Público? \n 1 - Privado \n 2 - Público \n Escreva aqui: "))

if trans == 1:
    esc = int(input("Agora escolha o meio de transporte em que queira calcular o Crédito de Carbono: \n 1 - Carro \n 2 - Van/Ônibus \n Escreva aqui o véiculo desejado: "))
    if esc == 1:
        km = float(input("Quantos km você roda por dia?: "))
        l = float(input("Quantos litros você coloca?: "))
        kml = km/l
        com = int(input("Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado: "))
        if com == 1:
            result = kml*0.82*0.75*3.7
            if result < 5:
                print (f"Sua emissão de CO2 é de: {result}. Por conseguir emitir menos de 5 kg de CO2, você acaba ganhando 15% de desconto na Declaração de Imposto de Renda do ano vigente")
            else: 
                print (f"Sua emissão de CO2 é de: {result}")

if trans == 2:
    esc = int(input("Agora escolha o meio de transporte em que queira calcular o Crédito de Carbono: \n 1 - Ônibus \n 2 - Trem \n Escreva aqui o véiculo desejado: "))
    if esc == 1:
        km = float(input("Quantos km você roda por dia(ida e volta)?: "))
        s = float(input("Quantas vezes por semana você faz esse trajeto?: "))
        kms = km*s
        com = int(input("Qual o combustível que você utiliza no véiculo?. \n 1 - Diesel \n 2 - Alcool \n 3- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado: "))
        if com == 1:
             l = float(input("Quantos litros você coloca para realizar as viagens?: "))
             kml = kms/l
             result = kml*0.83*3.7
             oni = int(input("Quantos ônibus a sua empresa possui?: "))
             fin = result*oni
             print (f"Sua emissão de CO2 por um ônibus é de: {result} kg, já a emissão total de todos os seus ônibus que realizam a mesma rota é de: {fin}. Confira com o Gestor Ambiental os próximos passos")

