from flask import Blueprint, render_template
from flask import request # this is needed to read data from a POST or DELETE request
from planeador import models
mod =  Blueprint('api', __name__)


@mod.route('/clases', methods=['GET'])
def listElems():
    return '{"result":"Estas son todas las clases"}'
# <id> means that this part of the url will be interpreted
# as the variable "id". This variable is passed as a parameter
#  to the function that handles the route .
@mod.route('/clases/<id>', methods=['GET', 'DELETE'])
def getOrDeleteclase(id):
    """Function that gets or deletes a clase with a specific id"""
    if request.method == "GET":
        return f'{{"result":"Esta es la clase con id {id}"'
    if request.method == "DELETE":
        return f'{{"result":"Esta es la solicitud para eliminar la clase {id}"'

@mod.route('/clases/<id>', methods=['PUT'])
def modifyClase(id):
    """Function that modifies the clase with the specified id"""
    return f'{{"result":"Esta es la solicitud para modificar la clase {id} con nuevo nombre {request.form["Nombre"]}"'

@mod.route('/clases', methods=['POST'])
def addClase():
    
    return f'{{"result":"Este es el resultado de la solicitud post de {request.form["Nombre"]}"}}'