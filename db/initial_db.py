import os, pandas as pd
from dotenv import load_dotenv
from models.region import Region
from models.weapon_type import WeaponType
from models.attack_type import AttackType
from models.event import Event
from models.target_type import TargetType
from models.city import City
from models.country import Country
from models.terror_organization import TerrorOrganization
from .connection import session_factory


load_dotenv()

def load_csv_to_db():
    session = session_factory()
    try:
        df = pd.read_csv(os.getenv("NORMAL_DATASET_CSV_PATH"), encoding='latin1')
        df_to_db(session ,TargetType, df[["target_type", "target_type_id"]], { "target_type_id": "id", "target_type": "name"})
        df_to_db(session ,AttackType, df[["attack_type", "attack_type_id"]], { "attack_type_id": "id", "attack_type": "name"})
        df_to_db(session ,WeaponType, df[["weapon_type", "weapon_type_id"]], { "weapon_type_id": "id", "weapon_type": "name"})
        df_to_db(session ,Region, df[["region", "region_id"]], { "region_id": "id", "region": "name"})
        df_to_db(session ,Country, df[["country", "country_id", "region_id"]], { "country_id": "id", "country": "name"})
        df_to_db(session ,TerrorOrganization, df[["terror_organization", "terror_organization_id"]], { "terror_organization_id": "id", "terror_organization": "name"})
        df_to_db(session ,City, df[["city", "city_id", "country_id"]], {"city_id": "id", "city": "name"})
        df_to_db(session ,Event, df[["event_id","latitude","longitude", "fatalities_num","injuries_num", "attackers_num", "date","city_id", "terror_organization_id","attack_type_id","weapon_type_id", "target_type_id"]],{"event_id": "id"})
        print("Successfully inserted all the tables in the csv file to the database")
    except Exception as e:
        session.rollback()
        print(f"all the insertions has rolled back due the error occurred while inserting the csv file into the database {e}")
    finally:
        session.close()



def df_to_db(session ,model:object, df: pd.DataFrame, rename_columns_to_fields:dict[str,str]):
    df = df.drop_duplicates()
    df = df.rename(columns=rename_columns_to_fields)
    rows_as_dict_list = df.to_dict(orient='records')
    session.bulk_insert_mappings(model, rows_as_dict_list)
    session.commit()
    print(f"Successfully inserted data to the table '{model.__tablename__}' in the database")





#
# if __name__ == '__main__':
#     from dotenv import load_dotenv
#     load_dotenv()
#     load_csv_to_db()