import pickle
from flask import  session

def isFormData(contentType):
    return 'application/x-www-form-urlencoded' in contentType or  'multipart/form-data' in contentType

def getX_test(request):
    X_test = [[]]

    if 'application/json' in request.headers.get('Content-Type', ''):
           datos = request.get_json()           
           X_test=[[datos.get('1'), datos.get('2'), datos.get('3'), datos.get('4'), datos.get('5'), datos.get('6'), datos.get('7'), datos.get('8'), datos.get('9')]]
           
    if isFormData(request.headers.get('Content-Type', '')):
           col_1 = request.form['1']
           col_2 = request.form['2']
           col_3 = request.form['3']
           col_4 = request.form['4']
           col_5 = request.form['5']
           col_6 = request.form['6']
           col_7 = request.form['7']
           col_8 = request.form['8']
           col_9 = request.form['9']
           X_test=[[col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9]]
    return X_test   

def cargarModelo(fichero):

    pickled_model = pickle.load(open(fichero, 'rb'))
    #if not pickled_model:
    #    abort(404, message="No se ha podido cargar el modelo serializado")

    return pickled_model


def predict(modelo, X_test):
    
    if modelo:
        return modelo.predict(X_test)
