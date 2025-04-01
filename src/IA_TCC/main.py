from src.IA_TCC.DATABASE.DB_MANAGER import DBManager
from src.IA_TCC.DATABASE.DB_CONFIG import sqlalchemy_engine
from src.IA_TCC.STATISTICAL_CALCULATION.LINEAR_REGRESSION import Linear_Regression

def main():
    db_manager = DBManager()
    db_manager.execute_processes()
    connection = sqlalchemy_engine
    model = Linear_Regression(connection)
    model.run()

if __name__ == "__main__":
    main()