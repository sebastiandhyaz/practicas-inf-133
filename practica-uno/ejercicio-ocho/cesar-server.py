from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

mensajes = []

def cifrado_cesar(mensaje):
    resultado = ""
    for letra in mensaje:
        if letra.isalpha():
            ascii_offset = 65 if letra.isupper() else 97
            resultado += chr((ord(letra) - ascii_offset + 3) % 26 + ascii_offset)
        else:
            resultado += letra
    return resultado

class Mensaje(Resource):
    def get(self, id=None):
        if id:
            for mensaje in mensajes:
                if mensaje['id'] == id:
                    return mensaje
            return {'error': 'Mensaje no encontrado'}, 404
        else:
            return mensajes

    def post(self):
        mensaje = request.get_json()
        mensaje['id'] = str(len(mensajes) + 1)
        mensaje['contenido_encriptado'] = cifrado_cesar(mensaje['contenido'])
        mensajes.append(mensaje)
        return mensaje, 201

    def put(self, id):
        for mensaje in mensajes:
            if mensaje['id'] == id:
                mensaje['contenido'] = request.json.get('contenido', mensaje['contenido'])
                mensaje['contenido_encriptado'] = cifrado_cesar(mensaje['contenido'])
                return mensaje
        return {'error': 'Mensaje no encontrado'}, 404

    def delete(self, id):
        global mensajes
        mensajes = [mensaje for mensaje in mensajes if mensaje['id'] != id]
        return {'message': 'Mensaje eliminado'}

api.add_resource(Mensaje, '/mensajes', '/mensajes/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
