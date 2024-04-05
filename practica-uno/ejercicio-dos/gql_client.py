import requests
import json

url = 'http://localhost:5000/graphql'
plantas = [
    {
        'nombreComun': 'Rosa',
        'especie': 'Rosa spp.',
        'edad': 12,
        'altura': 50,
        'frutos': 0
    },
    {
        'nombreComun': 'Girasol',
        'especie': 'Helianthus annuus',
        'edad': 6,
        'altura': 150,
        'frutos': 20
    },
    {
        'nombreComun': 'Orquídea',
        'especie': 'Orchidaceae',
        'edad': 24,
        'altura': 25,
        'frutos': 0
    },
    {
        'nombreComun': 'Bonsái',
        'especie': 'Juniperus chinensis',
        'edad': 60,
        'altura': 30,
        'frutos': 0
    }
]

# Crear varias plantas
for i, planta in enumerate(plantas, start=1):
    query = f'''
    mutation {{
      crearPlanta(nombreComun: "{planta['nombreComun']}", especie: "{planta['especie']}", edad: {planta['edad']}, altura: {planta['altura']}, frutos: {planta['frutos']}) {{
        planta {{
          nombreComun
          especie
          edad
          altura
          frutos
        }}
      }}
    }}
    '''
    response = requests.post(url, json={'query': query})
    print(f"Planta {i}:")
    print(json.dumps(response.json(), indent=2))
    print("\n")

# Listar todas las plantas
query = '''
{
  plantas {
    nombreComun
    especie
    edad
    altura
    frutos
  }
}
'''
response = requests.post(url, json={'query': query})
print("Todas las plantas:")
print(json.dumps(response.json(), indent=2))
