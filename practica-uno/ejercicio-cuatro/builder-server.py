from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

pacientes = []

class PacienteBuilder:
    def __init__(self):
        self.paciente = {}

    def con_ci(self, ci):
        self.paciente['ci'] = ci
        return self

    def con_nombre(self, nombre):
        self.paciente['nombre'] = nombre
        return self

    def con_apellido(self, apellido):
        self.paciente['apellido'] = apellido
        return self

    def con_edad(self, edad):
        self.paciente['edad'] = edad
        return self

    def con_genero(self, genero):
        self.paciente['genero'] = genero
        return self

    def con_diagnostico(self, diagnostico):
        self.paciente['diagnostico'] = diagnostico
        return self

    def con_doctor(self, doctor):
        self.paciente['doctor'] = doctor
        return self

    def construir(self):
        return self.paciente

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
        builder = PacienteBuilder()
        paciente = builder \
            .con_ci(request.json['ci']) \
            .con_nombre(request.json['nombre']) \
            .con_apellido(request.json['apellido']) \
            .con_edad(request.json['edad']) \
            .con_genero(request.json['genero']) \
            .con_diagnostico(request.json['diagnostico']) \
            .con_doctor(request.json['doctor']) \
            .construir()
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
