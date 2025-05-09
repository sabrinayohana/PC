comprimento_estrada, distancia_pedagios = map(int, input().split())  
custo_percuso, valor_pedagio = map(int, input().split()) 

custo_km = comprimento_estrada * custo_percuso

quantidade_pedagios = comprimento_estrada // distancia_pedagios
custo_pedagios = quantidade_pedagios * valor_pedagio

custo_total = custo_km + custo_pedagios
print(custo_total)