from camelcase import CamelCase

instancia = CamelCase()

texto = 'hola mundo'

resultado = instancia.hump(texto)
print(resultado)
