import requests

base_url = 'http://localhost:5000/animales'

# Crear un mamífero
nuevo_animal = {
    'id': '1',
    'nombre': 'Simba',
    'especie': 'León',
    'genero': 'Masculino',
    'edad': 5,
    'peso': 190,
    'tipo': 'Mamífero'
}
response = requests.post(base_url, json=nuevo_animal)
print(response.json())

# Crear un ave
nuevo_animal = {
    'id': '2',
    'nombre': 'Tweety',
    'especie': 'Canario',
    'genero': 'Masculino',
    'edad': 2,
    'peso': 0.03,
    'tipo': 'Ave'
}
response = requests.post(base_url, json=nuevo_animal)
print(response.json())

# Crear un reptil
nuevo_animal = {
    'id': '3',
    'nombre': 'Rex',
    'especie': 'Tortuga',
    'genero': 'Masculino',
    'edad': 10,
    'peso': 5,
    'tipo': 'Reptil'
}
response = requests.post(base_url, json=nuevo_animal)
print(response.json())

# Crear un anfibio
nuevo_animal = {
    'id': '4',
    'nombre': 'Kermit',
    'especie': 'Rana',
    'genero': 'Masculino',
    'edad': 3,
    'peso': 0.1,
    'tipo': 'Anfibio'
}
response = requests.post(base_url, json=nuevo_animal)
print(response.json())

# Crear un pez
nuevo_animal = {
    'id': '5',
    'nombre': 'Nemo',
    'especie': 'Pez Payaso',
    'genero': 'Masculino',
    'edad': 2,
    'peso': 0.1,
    'tipo': 'Pez'
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
    'peso': 200,
    'tipo': 'Mamífero'
}
response = requests.put(f'{base_url}/1', json=actualizacion_animal)
print(response.json())

# Eliminar un animal
response = requests.delete(f'{base_url}/1')
print(response.json())
