import requests

base_url = 'http://localhost:5000/pacientes'

# Crear un paciente
nuevo_paciente = {
    'ci': '12345678',
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 30,
    'genero': 'masculino',
    'diagnostico': 'Diabetes',
    'doctor': 'Pedro Pérez'
}
response = requests.post(base_url, json=nuevo_paciente)
print(response.json())

# Listar todos los pacientes
response = requests.get(base_url)
print(response.json())

# Buscar un paciente por CI
response = requests.get(f'{base_url}/12345678')
print(response.json())

# Actualizar la información de un paciente
actualizacion_paciente = {
    'ci': '12345678',
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 31,
    'genero': 'masculino',
    'diagnostico': 'Diabetes',
    'doctor': 'Pedro Pérez'
}
response = requests.put(f'{base_url}/12345678', json=actualizacion_paciente)
print(response.json())

# Eliminar un paciente
response = requests.delete(f'{base_url}/12345678')
print(response.json())
