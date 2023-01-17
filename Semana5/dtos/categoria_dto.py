from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categorias_model import Categoria


class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        # sirve para pasarle los metadatos a la clase que estamos heredando, es una clase exlusiva de python
        # Metadatos son informacion que necsita la clase que estamos heredando como atribudtos para que funcionas correctamete
        # Sirve para indicar mediante que modelo se tiene que guiar para haccer el mapeo de la informacion
        model = Categoria
