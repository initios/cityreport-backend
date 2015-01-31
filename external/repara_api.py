import requests, base64

from core.models import Issue


class ReparaCiudad:
    LIMPIEZA = 1
    SEMAFOROS = 2
    VEHICULOS = 3
    ALUMBRADO = 4
    MOBILIARIO_URBANO = 5
    VIA_PUBLICA = 6
    ARBOLADO = 7
    OTRAS = 8
    TRANSPORTE_PUBLICO = 9
    RENFE = 10
    FGC = 11
    TRANVIA = 12
    AUTOBUS = 13

    def retrieve_city(self, city):

        city_encode = self.encode_city(city)

        r = requests.get('http://reparaciudad.com/incidencia/cargarResultadosBusquedas/0/0/1/0/0/'
                         + city_encode)

        return r.json()

    def save_city(self, city):

        city_objs = self.retrieve_city(self, city)

        for object in city_objs:
            if object.has_key('id'):
                issue = Issue()
                issue.lat = object.latitud
                issue.lon = object.longitud
                issue.address = object.direccion
                issue.description = object.desperfectoTexto

                issue.save()

    def encode_city(city):
        string = bytes(city, 'utf-8')
        b64bytes = base64.encodebytes(string)
        b64auth = b64bytes.decode('ascii')

        return b64auth
