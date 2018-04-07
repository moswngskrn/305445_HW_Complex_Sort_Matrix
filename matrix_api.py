from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('A')
parser.add_argument('B')

def strToArray3x3(stringArray):
    k = 0
    result = []

    for i in range(1,len(stringArray)-1):
        if(stringArray[i]=='['):
            k = i+1
        if(stringArray[i]==']'):
            m = stringArray[k:i]
            m=map(int,m.split(','))
            result.append(m)
    return result

def AddSub3x3(A,B):
    for i in range(3):
        for j in range(3):
            B[i][j]=B[i][j]*2

    for i in range(3):
        for j in range(3):
            A[i][j]=A[i][j]+B[i][j]
    return A

def MultiplyDot3x3(k,A):
    for i in range(3):
        for j in range(3):
            A[i][j] = A[i][j]*k
        
    
    return A
def Sum3x3(A,B):
    for i in range(3):
        for j in range(3):
            A[i][j]=A[i][j]+B[i][j]
    return A
def Multiply3x3(A,B):
    result = []
    for i in range(3):
        m = []
        for j in range(3):
            s = 0
            for k in range(3):
                s += A[i][k]*B[k][j]
            m.append(s)
        result.append(m)
    return result
def Det3x3(A):
    m=0
    for i in range(3):
        s=1
        for j in range(3):
            if(i+j<3):
                s*=A[j][j+i]
            else:
                s*=A[j][j+i-3]
        m+=s
    n=0
    for i in range(3):
        s=1
        for j in range(2,-1,-1):
            if(3-j+i<3):
                s*=A[j][3-j+i]
            else:
                s*=A[j][3-j+i-3]
        n+=s
    return m-n
def Adj3x3(A):
    g = []
    for i in range(3):
        h = []
        for j in range(3):
            m = []
            for p in range(3):
                n = []
                isAdd = False
                for q in range(3):
                    if (p != i) and (q != j):
                        isAdd = True
                        n.append(A[p][q])
                if(isAdd):
                    m.append(n)
            h.append(m[0][0]*m[1][1]-m[1][0]*m[0][1])
        g.append(h)

    g[0][1]*=-1
    g[1][2]*=-1
    g[2][1]*=-1
    g[1][0]*=-1
    result = []
    for i in range(3):
        m = []
        for j in range(3):
            m.append(g[j][i])
        result.append(m)
    return result
def Invese3x3(A):
    det = Det3x3(A)
    A = Adj3x3(A)
    for i in range(3):
        for j in range(3):
            A[i][j] = float(A[i][j])/det
    return A

def Pow2_3x3(A):
    return Multiply3x3(A,A)

def Num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def FixedPoint3x3(A):
    for i in range(3):
        for j in range(3):
            A[i][j] = Num('%g'%(A[i][j]))
    return A


class AddSub(Resource):
        def post(self):
            args = parser.parse_args()
            A = str(args['A'])
            B = str(args['B'])
            Z = Sum3x3(strToArray3x3(A),MultiplyDot3x3(2,strToArray3x3(B)))
            return {"Z":Z}
class Multiply(Resource):
        def post(self):
            args = parser.parse_args()
            A = str(args['A'])
            B = str(args['B'])
            Z = Multiply3x3(strToArray3x3(A),strToArray3x3(B))
            return {"Z":Z}

class Hardcore(Resource):
        def post(self):
            args = parser.parse_args()
            A = str(args['A'])
            B = str(args['B'])
            O = Multiply3x3(Pow2_3x3(strToArray3x3(A)),Invese3x3(strToArray3x3(B)))
            M = Multiply3x3(Invese3x3(strToArray3x3(A)),strToArray3x3(B))
            G = Multiply3x3(strToArray3x3(A),strToArray3x3(B))
            Z = Sum3x3(O,Sum3x3(M,G))
            return {"Z":FixedPoint3x3(Z)}

api.add_resource(AddSub,'/AddSub')
api.add_resource(Multiply,'/Multiply')
api.add_resource(Hardcore,'/Hardcore')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)
