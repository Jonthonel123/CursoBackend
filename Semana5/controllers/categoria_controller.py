from flask_restful import Resource, request
from configuracion import conexion
from models.categorias_model import Categoria
from dtos.categoria_dto import CategoriaDto
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError


class CategoriasController(Resource):
    def get(self):
        data = conexion.session.query(Categoria).all()
        # print(data[0].nombre)
        serializador = CategoriaDto(many=True)
        resultado = serializador.dump(data)
        return {
            'content': resultado
        }

    def post(self):
        data = request.get_json()
        print(data)
        serializador = CategoriaDto()
        try:
            resultado = serializador.load(data)
            print(resultado)
            nuevaCategoria = Categoria(nombre=resultado.get('nombre'))
            conexion.session.add(nuevaCategoria)
            conexion.session.commit()
            return {
                'message': 'Categoria creada exitosamente'
            }
        except IntegrityError as error_integridad:
            return {
                'message': 'Error al crear la categoria, esa categoria ya existe'
            }
        except ValidationError as error_validacion:
            return {
                'message': 'Error al crear la categoria, vea el content',
                'content': error_validacion.args
            }
        except Exception as error:
            return {
                'message': 'Error al crear la categoria',
                'content': error.args
            }


class CategoriaController(Resource):
    def get(self, id):
        print(id)
        categoria = conexion.session.query(Categoria).filter_by(id=id).first()
        print(categoria)
        return {
            'content': ''
        }
