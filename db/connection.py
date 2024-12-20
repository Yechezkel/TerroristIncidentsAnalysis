import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.region import Region
from models.weapon_type import WeaponType
from models.attack_type import AttackType
from models.event import Event
from models.target_type import TargetType
from models.city import City
from models.country import Country
from models.terror_organization import TerrorOrganization
import os
from dotenv import load_dotenv



load_dotenv()
engine = create_engine(os.getenv('POSTGRES_URI'))
Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)


def rebuild_all_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Successfully rebuilt all tables")

