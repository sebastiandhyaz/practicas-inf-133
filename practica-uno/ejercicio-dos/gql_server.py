from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Boolean, Int, Field, List, Schema, Mutation

app = Flask(__name__)

class Planta(ObjectType):
    id = Int()
    nombre_comun = String()
    especie = String()
    edad = Int()
    altura = Int()
    frutos = Int()

plantas = []

class Query(ObjectType):
    plantas = List(Planta)

    def resolve_plantas(self, info):
        return plantas

class CrearPlanta(Mutation):
    class Arguments:
        nombre_comun = String(required=True)
        especie = String(required=True)
        edad = Int(required=True)
        altura = Int(required=True)
        frutos = Int(required=True)

    planta = Field(lambda: Planta)

    def mutate(self, info, nombre_comun, especie, edad, altura, frutos):
        planta = Planta(id=len(plantas)+1, nombre_comun=nombre_comun, especie=especie, edad=edad, altura=altura, frutos=frutos)
        plantas.append(planta)
        return CrearPlanta(planta=planta)

class Mutation(ObjectType):
    crear_planta = CrearPlanta.Field()

schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
