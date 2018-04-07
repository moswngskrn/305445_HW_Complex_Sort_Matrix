from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('list')


#Bubble Sort
def BubbleSort(list):
    n = len(list)
    isSwap = True
    while(isSwap):
        isSwap = False
        for i in range(n-1):
            if(list[i]<list[i+1]):
                temp = list[i]
                list[i]=list[i+1]
                list[i+1]=temp
                isSwap = True
    return list

#Quick Sort
def QuickSort(list,start,last):
    if(start>=last):
        return list
    if(start==last+1):
        if(list[start]<list[last]):
            temp = list[start]
            list[start] = list[last]
            list[last] = temp
        return list
    pivot = list[start]
    i=start+1
    k=last
    while(i<k):
        if(list[k]>=pivot):
            while (i<k):
                if(list[i]<pivot):
                    temp = list[i]
                    list[i]=list[k]
                    list[k]=temp
                    break
                i+=1
        if(i==k): break
        k-=1
    if(list[k]>pivot):
        list[start] = list[k]
        list[k] = pivot
    list = QuickSort(list,start,k-1)
    list = QuickSort(list,k+1,last)
    return list

# Merge Sort
def MergeList(list1,list2):
    i=0
    j=0
    my_list=[]
    while(i<len(list1) or j<len(list2)):
        if(i<len(list1)):
            if(j<len(list2)):
                if(list1[i]>list2[j]):
                    my_list.append(list1[i])
                    i+=1
                else:
                    my_list.append(list2[j])
                    j+=1
            else:
                my_list.append(list1[i])
                i+=1
        else:
            if(j<len(list2)):
                my_list.append(list2[j])
            j+=1
    return my_list

def MergeSort(list):
    if(len(list)==1):
        return list
    nC = len(list)/2
    listL = MergeSort(list[0:nC])
    listR = MergeSort(list[nC:len(list)])
    list = MergeList(listL,listR)
    return list

#ex. args['list'] = 5,2,7,8,9,2,1
class Bubble(Resource):
        def post(self):
            args = parser.parse_args()
            list = map(int,str(args['list']).split(','))
            return {"result":BubbleSort(list)}
class Quick(Resource):
        def post(self):
            args = parser.parse_args()
            list = map(int,str(args['list']).split(','))
            return {"result":BubbleSort(list)}

class Merge(Resource):
        def post(self):
            args = parser.parse_args()
            list = map(int,str(args['list']).split(','))
            return {"result":BubbleSort(list)}

api.add_resource(Bubble,'/Bubble')
api.add_resource(Quick,'/Quick')
api.add_resource(Merge,'/Merge')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)
