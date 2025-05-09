nome = input()

salarioBase = float (input())
vendasMes = float (input())

bonus = vendasMes * 15 / 100
salarioFinal = salarioBase + bonus

print(nome)
print(f"R$ {salarioFinal:.2f}")