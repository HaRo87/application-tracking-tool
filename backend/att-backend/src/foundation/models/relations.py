from sqlalchemy import orm, Column, Date, Integer, String
from sqlalchemy.sql import func

Base = orm.declarative_base()


class CountriesOrm(Base):
    __tablename__ = "countries"
    id = Column(
        "id", Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column("name", String, nullable=False)
    code = Column("code", String(2), nullable=False)
    created_at = Column("created_at", Date, nullable=False, default=func.now())
    removed_at = Column("removed_at", Date, nullable=True)
