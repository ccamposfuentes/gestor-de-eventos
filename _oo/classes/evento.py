# -*- coding: utf-8 -*-
#Evenge - gestor de eventos (events management)
#Copyright (C) 2014 - desarrollo.evenge@gmail.com
#Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import datetime
from asistente import Asistente

class Evento(ndb.Model):
    nombre = ndb.StringProperty()
    tipo = ndb.StringProperty()
    privado = ndb.BooleanProperty()
    idCreador = ndb.StringProperty()
    hora = ndb.TimeProperty()
    fecha = ndb.DateProperty()
    fechaInsercion = ndb.DateTimeProperty(auto_now_add=True)
    lugar = ndb.StringProperty()
    coordenadas = ndb.GeoPtProperty(indexed=False)
    descripcion = ndb.TextProperty(indexed=False)
    asistencia = ndb.BooleanProperty(indexed=False)
    asistentes = ndb.StructuredProperty(Asistente, repeated=True)
    ponentes = ndb.StringProperty(repeated=True)

    def getKey(self):
        return str(self.key.id())
