from configuracion import conexion
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey


class CategoriaProducto(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer, nullable=False, name='categoria_id')
    productoId = Column(ForeignKey(column='productos.id'),
                        type_=types.Integer, nullable=False, name='producto_id')
    __tablename__ = 'categorias_productos'
