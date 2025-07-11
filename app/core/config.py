import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')
db_host =  os.getenv('DB_HOST')
db_port =  os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

print("DB_URL: ", f"mongodb://{db_user}:{db_password}@{db_host}:{db_port}")


MONGO_URI = f"mongodb://{db_host}:{db_port}/{db_name}"
