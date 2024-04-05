from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

pacientes = []

class Paciente(Resource):
    def get(self, ci=None):
        if ci:
            for paciente in pacientes:
                if paciente['ci'] == ci:
                    return paciente
            return {'error': 'Paciente no encontrado'}, 404
        else:
            return pacientes

    def post(self):
        paciente = request.get_json()
        pacientes.append(paciente)
        return paciente, 201

    def put(self, ci):
        for paciente in pacientes:
            if paciente['ci'] == ci:
                paciente.update(request.get_json())
                return paciente
        return {'error': 'Paciente no encontrado'}, 404

    def delete(self, ci):
        global pacientes
        pacientes = [paciente for paciente in pacientes if paciente['ci'] != ci]
        return {'message': 'Paciente eliminado'}

api.add_resource(Paciente, '/pacientes', '/pacientes/<string:ci>')

if __name__ == '__main__':
    app.run(debug=True)
