# PROJECT IMPORTS
from src.infrastructure.sql_alchemy.infrastructure import SqlAlchemyInfrastructure

db, ma = SqlAlchemyInfrastructure.database_configuration()


class LapTopModel(db.Model):
    laptop_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    description = db.Column(db.String(255))

    def __init__(self, laptop_id, brand, description):
        self.laptop_id = laptop_id
        self.brand = brand
        self.description = description


class LaptopSchema(ma.Schema):
    class Meta:
        fields = ('laptop_id', 'brand', 'description')


# initializing schemas
laptop_schema = LaptopSchema(strict=True)
laptops_schema = LaptopSchema(many=True, strict=True)
