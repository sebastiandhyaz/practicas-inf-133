import requests

base_url = 'http://localhost:5000/mensajes'
mensajes = ['hola mundo', 'adios mundo', 'buenos dias', 'buenas noches', 'hasta luego']

# Crear varios mensajes
for i, contenido in enumerate(mensajes, start=1):
    nuevo_mensaje = {
        'contenido': contenido
    }
    response = requests.post(base_url, json=nuevo_mensaje)
    print(f"Mensaje {i}:")
    print(response.json())
    print("\n")

# Listar todos los mensajes
print("Todos los mensajes:")
response = requests.get(base_url)
for mensaje in response.json():
    print(mensaje)
print("\n")
