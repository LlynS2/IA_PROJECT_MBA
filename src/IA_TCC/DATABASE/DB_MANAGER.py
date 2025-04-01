from src.IA_TCC.DATABASE.DB_CONFIG import connection
from src.IA_TCC.DATABASE.DB_MODELS import create_tables
from src.IA_TCC.DATABASE.DB_INSERT import insert_datas

class DBManager:
    def __init__(self):
        self.conn = None
        try:
            self.conn = connection()
            if self.conn:
                print("✅ Connection with the database successfully established!")
            else:
                print("❌ Failed to connect to the database.")
        except Exception as e:
            print(f"❌ Error initializing database connection: {e}")

    def execute_processes(self):
        if not self.conn:
            print("❌ Oops... We had an error, we were unable to connect to the database. Aborted processes.")
            return

        try:
            print("⚙️ Creating tables in the database...")
            create_tables()

            print("📥 Inserting data into the database...")
            insert_datas(self.conn)

            print("✅ Processes completed successfully!")
        except Exception as e:
            print(f"❌ Hmm... Error when executing processes: {e}")
        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn:
            try:
                self.conn.close()
                print("🔐 Connection with database closed.")
            except Exception as e:
                print(f"⚠️ Warning: Error closing database connection: {e}")