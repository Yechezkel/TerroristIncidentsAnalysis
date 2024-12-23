from dotenv import load_dotenv
from csv_files.normalize_scv import normalize_dataset
from db.initial_db import load_csv_to_db
from db.connection import rebuild_all_tables
import os





if __name__ == '__main__':
    load_dotenv()
    rebuild_all_tables()
    if not os.path.exists(os.getenv("NORMAL_DATASET_CSV_PATH")):
        normalize_dataset()
    load_csv_to_db()






