from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

animales = []

class Animal(Resource):
    def get(self, id=None):
        if id:
            for animal in animales:
                if animal['id'] == id:
                    return animal
            return {'error': 'Animal no encontrado'}, 404
        else:
            especie = request.args.get('especie')
            genero = request.args.get('genero')
            if especie:
                return [animal for animal in animales if animal['especie'] == especie]
            elif genero:
                return [animal for animal in animales if animal['genero'] == genero]
            else:
                return animales

    def post(self):
        animal = request.get_json()
        animales.append(animal)
        return animal, 201

    def put(self, id):
        for animal in animales:
            if animal['id'] == id:
                animal.update(request.get_json())
                return animal
        return {'error': 'Animal no encontrado'}, 404

    def delete(self, id):
        global animales
        animales = [animal for animal in animales if animal['id'] != id]
        return {'message': 'Animal eliminado'}

api.add_resource(Animal, '/animales', '/animales/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
