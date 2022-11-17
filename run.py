# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:22:08 2022
Archivo para correr la aplicacion
@author: LOPEZBALTASI
"""
#importar las funciones 
from application import create_app

from flask import jsonify, request
from flask_restx import  Resource, fields
from ml_model.rf_model  import cargarModelo, predict, getX_test


import pandas as pd
import os
#para cargar la configuracion
import config


#crear la aplicacion en una funcion como se aconseja en la documentacion de flask
app, api, ns = create_app()

ml_model_serialized = os.environ['ML_MODEL_SERIALIZED']

muestra_json = api.model('Muestra', {
        '1': fields.Integer(description='Clump Thickness 1 - 10', required=True),
        '2': fields.Integer(description='Uniformity of Cell Size 1 - 10', required=True),
        '3': fields.Integer(description='Uniformity of Cell Shape 1 - 10', required=True),
        '4': fields.Integer(description='Marginal Adhesion 1 - 10', required=True),
        '5': fields.Integer(description='Single Epithelial Cell Size 1 - 10', required=True),
        '6': fields.Integer(description='Bare Nuclei 1 - 10', required=True),
        '7': fields.Integer(description='Bland Chromatin 1 - 10', required=True),
        '8': fields.Integer(description='Normal Nucleoli 1 - 10', required=True),
        '9': fields.Integer(description='Mitoses  1 - 10', required=True)
})

@ns.route('/predict')
class Prediccion(Resource):    
    #https://flask-restx.readthedocs.io/en/latest/swagger.html
    @ns.doc(body=muestra_json)
    @ns.expect(muestra_json, validate=False)
    def post(self):
        
        X_test = getX_test(request)           

        df = pd.DataFrame(X_test)
        print(df.columns)
        if df.empty or df.isnull().values.any():
            return 'No se ha podido obtener una tupla con la información proporcionada', 400
           
        y_pred = predict(cargarModelo( ml_model_serialized) , df)       
        resultado = 'Benigno'
        if y_pred == 4:
            resultado = 'Maligno'
    
        return jsonify({'Predicción': resultado})        
        


if __name__ == '__main__':
    print (f"++ Entorno: {app.config.get('ENV')}")
    if app.config.get('ENV') == 'development':
        app.run(host='0.0.0.0', port = 7002, debug=True)
    if app.config.get('ENV') == 'docker':
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)        
