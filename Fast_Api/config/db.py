#necesario para realizar la conexion a la base de datos
from sqlalchemy import create_engine,MetaData

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/hr_2')
meta = MetaData()
conn = engine.connect()