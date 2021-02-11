import requests
metodo = 'GET'
uria = "http://egela.ehu.eus/"
cabeceras = {'Host': 'egela.ehu.eus'}
cuerpo = ''
respuesta = requests.request(metodo, uria, headers=cabeceras, data=cuerpo, allow_redirects=False)
codigo = respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
    cuerpo = respuesta.content
    print(cuerpo)
    metodo = 'GET'
    uri = respuesta.headers['Location']
    cabeceras = {'Host': uria.split('/')[2]}
    cuerpo = ''
    respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo, allow_redirects=False)
    codigo = respuesta.status_code
    descripcion = respuesta.reason
    print(str(codigo) + " " + descripcion)
    for cabecera in respuesta.headers:
        print(cabecera + ": " + respuesta.headers[cabecera])
        cuerpo = respuesta.content
        print(cuerpo)