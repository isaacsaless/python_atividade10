# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida

print("Calculador de multas")
vel = float(input("Digite a velocidade do veículo: "))
multa = (vel-60)*7
if vel<60:
    print("O veículo está na velocidade permitida, não receberá multas.")
else:
    print(f"O veículo excedeu a velocidade permitida, por isso, receberá uma multa de {multa}.")