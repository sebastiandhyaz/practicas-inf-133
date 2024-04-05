from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

animales = []

class Animal:
    def __init__(self, id, nombre, especie, genero, edad, peso, tipo):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso
        self.tipo = tipo

class Mamifero(Animal):
    def __init__(self, id, nombre, especie, genero, edad, peso):
        super().__init__(id, nombre, especie, genero, edad, peso, 'Mamífero')

class Ave(Animal):
    def __init__(self, id, nombre, especie, genero, edad, peso):
        super().__init__(id, nombre, especie, genero, edad, peso, 'Ave')

class Reptil(Animal):
    def __init__(self, id, nombre, especie, genero, edad, peso):
        super().__init__(id, nombre, especie, genero, edad, peso, 'Reptil')

class Anfibio(Animal):
    def __init__(self, id, nombre, especie, genero, edad, peso):
        super().__init__(id, nombre, especie, genero, edad, peso, 'Anfibio')

class Pez(Animal):
    def __init__(self, id, nombre, especie, genero, edad, peso):
        super().__init__(id, nombre, especie, genero, edad, peso, 'Pez')

class AnimalFactory:
    def crear_animal(self, tipo, id, nombre, especie, genero, edad, peso):
        if tipo == 'Mamífero':
            return Mamifero(id, nombre, especie, genero, edad, peso)
        elif tipo == 'Ave':
            return Ave(id, nombre, especie, genero, edad, peso)
        elif tipo == 'Reptil':
            return Reptil(id, nombre, especie, genero, edad, peso)
        elif tipo == 'Anfibio':
            return Anfibio(id, nombre, especie, genero, edad, peso)
        elif tipo == 'Pez':
            return Pez(id, nombre, especie, genero, edad, peso)
        else:
            return None

class AnimalResource(Resource):
    def get(self, id=None):
        if id:
            for animal in animales:
                if animal.id == id:
                    return animal.__dict__
            return {'error': 'Animal no encontrado'}, 404
        else:
            especie = request.args.get('especie')
            genero = request.args.get('genero')
            if especie:
                return [animal.__dict__ for animal in animales if animal.especie == especie]
            elif genero:
                return [animal.__dict__ for animal in animales if animal.genero == genero]
            else:
                return [animal.__dict__ for animal in animales]

    def post(self):
        factory = AnimalFactory()
        animal = factory.crear_animal(
            request.json['tipo'],
            request.json['id'],
            request.json['nombre'],
            request.json['especie'],
            request.json['genero'],
            request.json['edad'],
            request.json['peso']
        )
        if animal is None:
            return {'error': 'Tipo de animal no válido'}, 400
        animales.append(animal)
        return animal.__dict__, 201

    def put(self, id):
        for animal in animales:
            if animal.id == id:
                animal.nombre = request.json.get('nombre', animal.nombre)
                animal.especie = request.json.get('especie', animal.especie)
                animal.genero = request.json.get('genero', animal.genero)
                animal.edad = request.json.get('edad', animal.edad)
                animal.peso = request.json.get('peso', animal.peso)
                return animal.__dict__
        return {'error': 'Animal no encontrado'}, 404

    def delete(self, id):
        global animales
        animales = [animal for animal in animales if animal.id != id]
        return {'message': 'Animal eliminado'}

api.add_resource(AnimalResource, '/animales', '/animales/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
