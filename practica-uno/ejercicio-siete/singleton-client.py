import requests

base_url = 'http://localhost:5000/partidas'
elementos = ['piedra', 'papel', 'tijera']

# Crear varias partidas
for i in range(1, 11):
    for elemento in elementos:
        nueva_partida = {
            'elemento': elemento
        }
        response = requests.post(base_url, json=nueva_partida)
        print(f"Partida {i} con {elemento}:")
        print(response.json())
        print("\n")

# Listar todas las partidas
print("Todas las partidas:")
response = requests.get(base_url)
for partida in response.json():
    print(partida)
print("\n")

# Listar partidas perdidas
print("Partidas perdidas:")
response = requests.get(base_url, params={'resultado': 'perdió'})
for partida in response.json():
    print(partida)
print("\n")

# Listar partidas ganadas
print("Partidas ganadas:")
response = requests.get(base_url, params={'resultado': 'ganó'})
for partida in response.json():
    print(partida)
print("\n")
