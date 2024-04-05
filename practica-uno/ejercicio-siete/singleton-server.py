from flask import Flask, request
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

partidas = []
elementos = ['piedra', 'papel', 'tijera']

class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("Esta clase es un singleton!")
        else:
            Singleton._instance = self

class Partida(Resource):
    def get(self, id=None):
        if id:
            for partida in partidas:
                if partida['id'] == id:
                    return partida
            return {'error': 'Partida no encontrada'}, 404
        else:
            resultado = request.args.get('resultado')
            if resultado:
                return [partida for partida in partidas if partida['resultado'] == resultado]
            else:
                return partidas

    def post(self):
        partida = request.get_json()
        partida['id'] = str(len(partidas) + 1)
        partida['elemento_servidor'] = random.choice(elementos)
        if partida['elemento'] == partida['elemento_servidor']:
            partida['resultado'] = 'empató'
        elif (partida['elemento'] == 'piedra' and partida['elemento_servidor'] == 'tijera') or \
             (partida['elemento'] == 'tijera' and partida['elemento_servidor'] == 'papel') or \
             (partida['elemento'] == 'papel' and partida['elemento_servidor'] == 'piedra'):
            partida['resultado'] = 'ganó'
        else:
            partida['resultado'] = 'perdió'
        partidas.append(partida)
        return partida, 201

api.add_resource(Partida, '/partidas', '/partidas/<string:id>')

if __name__ == '__main__':
    Singleton.getInstance()
    app.run(debug=True)
