from sqlalchemy import Column, Integer, String
from . import Base


class WeaponType(Base):
    __tablename__ = "weapon_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False, default="Unknown", server_default="Unknown", index=True)


    def __repr__(self):
        return f"<WeaponType(id={self.id}, name={self.name})>"

    def __str__(self):
        return self.__repr__()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }