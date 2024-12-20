from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False, default="Unknown", server_default="Unknown", index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), index=True, nullable=False)
    region = relationship("Region")

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"

    def __str__(self):
        return self.__repr__()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region.to_dict() if self.region is not None else None,
        }