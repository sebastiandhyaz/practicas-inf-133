# server.py
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, num1, num2):
        return num1 + num2

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, num1, num2):
        return num1 - num2

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, num1, num2):
        return num1 * num2

    @rpc(Integer, Integer, _returns=Integer)
    def divide(ctx, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 // num2

application = Application([CalculatorService], 'CalculatorService',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8000, wsgi_application)
    server.serve_forever()
