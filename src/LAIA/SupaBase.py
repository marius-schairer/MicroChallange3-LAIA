from supabase import create_client as supabase_create_client, Client
import os
from dotenv import load_dotenv
import csv

load_dotenv()

def setup_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return supabase_create_client(url, key)

def fetch_data(client):
    LiveData = client.table('Inputs').select("*").execute()
    return LiveData.data  # Ensure to return just the data part if that's what you need
    

def fetch_data_from_database_and_save(client):
    live_data = client.table('Inputs').select("*").execute()

    # Define path to save CSV
    csv_file_path = 'docs/inputdata/input.csv'

    # Save the data to CSV
    if live_data.data:
        keys = live_data.data[0].keys()  # Grab the keys for CSV column headers
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for data in live_data.data:
                writer.writerow(data)
    
