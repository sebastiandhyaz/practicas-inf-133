# client.py
from zeep import Client

client = Client('http://localhost:8000/?wsdl')

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("Suma: {} + {} = {}".format(num1, num2, client.service.add(num1, num2)))
print("Resta: {} - {} = {}".format(num1, num2, client.service.subtract(num1, num2)))
print("Multiplicación: {} * {} = {}".format(num1, num2, client.service.multiply(num1, num2)))
print("División: {} / {} = {}".format(num1, num2, client.service.divide(num1, num2)))
