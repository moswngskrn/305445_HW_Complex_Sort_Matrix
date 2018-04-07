from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('complex1')
parser.add_argument('complex2')


def Complex(cp):
    real=0
    imaginary=0
    i=0
    if(cp[0]=='-'):
        for i in range(1,len(cp)):
            if(cp[i]=='+' or cp[i]=='-'):
                real = int(cp[1:i])*-1
                imaginary = int(cp[i+1:len(cp)-1])
                if(cp[i]=='-'):
                    imaginary=imaginary*-1
                i=len(cp)

    else:
        for i in range(0,len(cp)):
            if(cp[i]=='+' or cp[i]=='-'):
                real = int(cp[0:i])
                imaginary = int(cp[i+1:len(cp)-1])
                if(cp[i]=='-'):
                    imaginary=imaginary*-1
                i=len(cp)
    return [real,imaginary]

def ComplexAdd(cp1,cp2):
    if(len(cp1)==2 and len(cp2)==2):
        cp = [cp1[0]+cp2[0],cp1[1]+cp2[1]]
        return cp
    return [None,None]

def ComplexSub(cp1,cp2):
    if(len(cp1)==2 and len(cp2)==2):
        cp = [cp1[0]-cp2[0],cp1[1]-cp2[1]]
        return cp
    return [None,None]

def ComplexMultiply(cp1,cp2):
    if(len(cp1)==2 and len(cp2)==2):
        cp = [cp1[0]*cp2[0] - cp1[1]*cp2[1],cp1[0]*cp2[1]+cp1[1]*cp2[0]]
        return cp
    return [None,None]

def ComplexToString(cp):
    ressult = str(cp)
    if(cp[1]<0):
        ressult = ressult.replace('[','').replace(']','i').replace(',','').replace(' ','')
    else:
        ressult = ressult.replace('[','').replace(']','i').replace(',','+').replace(' ','')
    return ressult

class Add(Resource):
        def post(self):
                args = parser.parse_args()
                complex1 = Complex(str(args['complex1']))
                complex2 = Complex(str(args['complex2']))
                return {"result":ComplexToString(ComplexAdd(complex1,complex2))}
class Sub(Resource):
        def post(self):
                args = parser.parse_args()
                complex1 = Complex(str(args['complex1']))
                complex2 = Complex(str(args['complex2']))
                return {"result":ComplexToString(ComplexSub(complex1,complex2))}
class Multiply(Resource):
        def post(self):
                args = parser.parse_args()
                complex1 = Complex(str(args['complex1']))
                complex2 = Complex(str(args['complex2']))
                return {"result":ComplexToString(ComplexMultiply(complex1,complex2))}

api.add_resource(Add,'/Add')
api.add_resource(Sub,'/Sub')
api.add_resource(Multiply,'/Multiply')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)
