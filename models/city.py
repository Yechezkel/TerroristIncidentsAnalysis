from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from . import Base


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,  nullable=True, default="Unknown", server_default="Unknown", index=True)
    country_id = Column(Integer, ForeignKey("countries.id"), index=True, nullable=False)
    __table_args__ = ( UniqueConstraint(name, country_id, name='unique_name_&_country_id'), )
    country = relationship("Country")


    def __repr__(self):
        return f"<City(id={self.id}, name={self.name})>"

    def __str__(self):
        return self.__repr__()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country.to_dict() if self.country is not None else None,
        }