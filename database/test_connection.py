import pymysql
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) AS total FROM departments")
result = cursor.fetchone()
print("Connection successful! Departments count:", result)

cursor.close()
conn.close()