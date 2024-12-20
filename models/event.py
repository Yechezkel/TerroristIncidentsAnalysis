from sqlalchemy import Column, Integer, BigInteger, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Event(Base):  # todo:indices
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    attackers_num = Column(Integer, nullable=False, default=1, server_default="1") # why str in server_default?
    injuries_num = Column(Integer, nullable=False, default=0, server_default="0")
    fatalities_num = Column(Integer, nullable=False, default=0, server_default="0")
    date = Column(Date, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), index=True, nullable=False)
    target_type_id = Column(Integer, ForeignKey("target_types.id"), index=True, nullable=True)
    terror_organization_id = Column(Integer, ForeignKey("terror_organizations.id"), index=True, nullable=True)
    weapon_type_id = Column(Integer, ForeignKey("weapon_types.id"), index=True, nullable=True)
    attack_type_id = Column(Integer, ForeignKey("attack_types.id"), index=True, nullable=True)
    weapon_type = relationship("WeaponType")
    attack_type = relationship("AttackType")
    terror_organization = relationship("TerrorOrganization")
    target_type = relationship("TargetType")
    city = relationship("City")


    # def __repr__(self):
    #     return f"<WeaponType(id={self.id}, name={self.name})>"
    #
    # def __str__(self):
    #     return self.__repr__()
    #
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name
    #     }