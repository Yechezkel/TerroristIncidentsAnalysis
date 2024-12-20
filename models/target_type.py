from sqlalchemy import Column, Integer, String
from . import Base


class TargetType(Base):
    __tablename__ = "target_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False, default="Unknown", server_default="Unknown", index=True)


    def __repr__(self):
        return f"<TargetType(id={self.id}, name={self.name})>"

    def __str__(self):
        return self.__repr__()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }