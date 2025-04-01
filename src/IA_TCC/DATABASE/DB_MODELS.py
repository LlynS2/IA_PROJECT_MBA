from src.IA_TCC.DATABASE.DB_CONFIG import connection
def create_tables():
    conn = connection()
    if conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS TB_EMPRESAS (
                id SERIAL PRIMARY KEY,
                ticker VARCHAR(20),
                nome VARCHAR(255) NOT NULL,
                setor VARCHAR(100)
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS TB_ADOCAO_IA (
                id SERIAL PRIMARY KEY,
                id_empresa INT REFERENCES TB_EMPRESAS(id),
                adotou_ia BOOLEAN NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS TB_INVESTIMENTOS (
                id SERIAL PRIMARY KEY,
                id_empresa INT REFERENCES TB_EMPRESAS(id),
                ano INT,
                semestre VARCHAR(20),
                receita NUMERIC,
                lucro NUMERIC,
                roi NUMERIC
            );
        """)

        conn.commit()
        cur.close()
        conn.close()
