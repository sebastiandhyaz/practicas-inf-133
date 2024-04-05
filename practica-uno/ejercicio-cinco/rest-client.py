import requests

base_url = 'http://localhost:5000/animales'

# Crear un animal
nuevo_animal = {
    'id': '1',
    'nombre': 'Simba',
    'especie': 'León',
    'genero': 'Masculino',
    'edad': 5,
    'peso': 190
}
response = requests.post(base_url, json=nuevo_animal)
print(response.json())

# Listar todos los animales
response = requests.get(base_url)
print(response.json())

# Buscar un animal por ID
response = requests.get(f'{base_url}/1')
print(response.json())

# Actualizar la información de un animal
actualizacion_animal = {
    'id': '1',
    'nombre': 'Simba',
    'especie': 'León',
    'genero': 'Masculino',
    'edad': 6,
    'peso': 200
}
response = requests.put(f'{base_url}/1', json=actualizacion_animal)
print(response.json())

# Eliminar un animal
response = requests.delete(f'{base_url}/1')
print(response.json())
