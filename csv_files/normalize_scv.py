# from api_services.groq_api import get_city_from_summary
import pandas as pd
import numpy as np
import os

def normalize_dataset(): # this is a dev function not for production
    df = pd.read_csv(os.getenv("NOT_NORMAL_DATASET_CSV_PATH"), encoding='latin1', low_memory=False)
    df["imonth"] = df["imonth"].replace(0, 1)
    df["iday"] = df["iday"].replace(0, 1)
    df["date"] = pd.to_datetime(dict(year=df["iyear"], month=df["imonth"], day=df["iday"]))
    columns_to_keep = [
        'eventid', 'date', 'city', 'longitude', 'latitude',
        'country_txt', 'country', 'region_txt', 'region',
        'weaptype1', 'weaptype1_txt', 'attacktype1', 'attacktype1_txt',
        'targtype1', 'targtype1_txt', 'summary', 'nperps', 'nkill','nwound', 'gname'
    ]
    columns_not_none = [
        'eventid', 'date', 'city', 'longitude', 'latitude',
        'country_txt', 'country', 'region_txt', 'region',
    ]
    df = df[columns_to_keep].copy()
    df = df.dropna(subset=columns_not_none)
    # df['nwound'] = df['nwound'].map(lambda x: None if x<0 or x==np.nan else x)
    # df['nkill'] = df['nkill'].map(lambda x: None if x<0 or x==np.nan else x)
    # df['nperps'] = df['nperps'].map(lambda x: None if x<0 or x==np.nan else x)
    df[["nperps", "nkill", "nwound"]] = df[["nperps","nkill" ,"nwound"]].fillna(-99)  # todo:to handle it with a null value not -99, and then in the function df_to_db to add the option to convert np.nan into None
    column_rename_map = {
        'weaptype1_txt': 'weapon_type',
        'weaptype1': 'weapon_type_id',
        'targtype1_txt': 'target_type',
        'targtype1': 'target_type_id',
        'attacktype1_txt': 'attack_type',
        'attacktype1': 'attack_type_id',
        'region_txt': 'region',
        'region': 'region_id',
        'country_txt': 'country',
        'country': 'country_id',
        'eventid': 'event_id',
        'city': 'city',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'date': 'date',
        'summary': 'summary',
        'nperps': 'attackers_num',
        'nwound': 'injuries_num',
        'nkill': 'fatalities_num',
        'gname': 'terror_organization',
    }
    df = df.rename(columns=column_rename_map)
    terror_org_map = {org: id for id, org in enumerate(df['terror_organization'].unique(), start=1)}
    df['terror_organization_id'] = df['terror_organization'].map(terror_org_map)
    city_country_map = {combo: idx for idx, combo in enumerate((df['city']+'_*_'+df['country_id'].astype(str)).unique(), start=1)}
    df['city_id'] = (df['city']+'_*_'+df['country_id'].astype(str)).map(city_country_map)
    event_id_map = {old_id: new_id for new_id, old_id in enumerate(df['event_id'].unique(), start=1)}
    df['event_id'] = df['event_id'].map(event_id_map)
    df.to_csv( os.getenv("NORMAL_DATASET_CSV_PATH"), index=False, encoding='latin1')
    print("the dataset has been normalized and stored in a csv file")


# if __name__ == "__main__":
#     from dotenv import load_dotenv
#     load_dotenv()
#     normalize_dataset()




# def initial_db():  # this is a production version
#     df = pd.read_csv('global_terrorism_full_dataset.csv', encoding='latin1')
#     df["imonth"] = df["imonth"].replace(0, 1)
#     df["iday"] = df["iday"].replace(0, 1)
#     df["date"] = pd.to_datetime(dict(year=df["iyear"], month=df["imonth"], day=df["iday"]))
#
#     df.loc[df["city"].isna() & (df["longitude"].isna() | df["latitude"].isna()), "city"] = get_city_from_summary(df["summary"], df["country"])
#       todo: ta add here the calls to get lon and lat by city name
#       todo: to add here the calls to get city name by lon and lat



