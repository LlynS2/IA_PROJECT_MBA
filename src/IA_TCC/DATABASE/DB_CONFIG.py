import psycopg2
from sqlalchemy import create_engine

DB_NAME ="TCC_MBA_COMPANIES_IA"
DB_USER ="postgres"
DB_PASSWORD ="senha"
DB_HOST = "localhost"
DB_PORT = "5432"
def connection():
    try:
        return psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
    except Exception as e:
        print("Connection error :", e)
        return None

def sqlalchemy_engine():
    try:
        url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        return create_engine(url)
    except Exception:
        return None
