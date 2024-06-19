taxa=20
try :
    custo=float(input("Digite o número de quilômetros da viagem: "))
    if custo<0 :
        print("Erro: O número de quilômetros não pode ser negativo.")
    elif custo <=50 :
        print("Erro: O número de quilômetros não pode ser inferior a 50 km")
    elif custo <=200 :
        menor_km=custo*0.75+taxa
        print(f"Sua viagem com {custo} km custará R$ {menor_km}") 
    elif custo <=500 :
        medio_km=custo*0.60+taxa
        print(f"Sua viagem com {custo} km custará R$ {medio_km}")
    else :
        maior_km=custo*0.50 + taxa
        print(f"Sua viagem com {custo} km custará R$ {maior_km}")
except :
    print("insira números corretamente")
