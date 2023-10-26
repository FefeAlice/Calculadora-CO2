trans=int(input("Olá! Bem-vindo. \n Você busca calcular por transporte Privado ou Público? \n 1 - Privado \n 2 - Público \n Escreva aqui: "))

if trans == 1:
    esc = int(input("Agora escolha o meio de transporte em que queira calcular o Crédito de Carbono: \n 1 - Carro \n 2 - Van/Ônibus \n Escreva aqui o véiculo desejado: "))
    if esc == 1:
        km = float(input(" Quantos km você roda por dia?: "))
        l = float(input(" Quantos litros você coloca?: "))
        kml = km/l
        com = int(input(" Qual o combustível que você utiliza no véiculo?. \n 1 - Gasolina \n 2 - Diesel \n 3 - Alcool \n 4- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado"))
        if com == 1:
            result = kml*0.82*0.75*3.7
            if result < 5:
            print (f" Sua emissão de CO2 é de:{result}. Por conseguir emitir menos de 5 kg de CO2, você acaba ganhando 15% de desconto em suas contas")

if trans == 2:
    esc = int(input("Agora escolha o meio de transporte em que queira calcular o Crédito de Carbono: \n 1 - Ônibus \n 2 - Trem \n Escreva aqui o véiculo desejado: "))
    if esc == 1:
        km = float(input(" Quantos km você roda por dia(ida e volta)?: "))
        l = float(input(" Quantas vezes por semana vocÊ faz esse trajeto?: "))
        kml = km/l
        com = int(input(" Qual o combustível que você utiliza no véiculo?. \n 1 - Diesel \n 2 - Alcool \n 3- Gás Natural (GNV)\n Escreva aqui qual o combústivel utilizado"))
        if com == 1:
             print (f" Sua emissão de CO2 é de:{result}. Tente evitar a emissão de CO2, a cada 1 tonelada evitada, gera um crédito de carbono")
         
    
    
