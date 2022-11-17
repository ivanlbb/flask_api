# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:59:57 2022

@author: LOPEZBALTASI
"""
#inicializar  la sesion de flask
from flask import Flask
from flask_restx import Api
import os

def create_app():
    app = Flask(__name__)
    
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    api = Api(app, doc='/', title='PoC ML predict API')

    ns = api.namespace('api',  description='Obtener prediccion')
    
    return app, api, ns
