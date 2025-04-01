import os
import pandas as pd
from src.IA_TCC.DATABASE.DB_CONFIG import connection

file_path = os.path.join(os.path.dirname(__file__), "Datas", "DATAS - COMPANIES.xlsx")
df = pd.read_excel(file_path)

def insert_datas(conn):
    df.columns = [col.strip() for col in df.columns]
    conn = connection()

    if conn:
        cur = conn.cursor()

        cur.execute("DELETE FROM TB_INVESTIMENTOS;")
        cur.execute("DELETE FROM TB_ADOCAO_IA;")
        cur.execute("DELETE FROM TB_EMPRESAS;")

        empresas_inseridas = set()

        for _, row in df.iterrows():
            empresa = row['Empresa']
            if empresa not in empresas_inseridas:
                print(f"🟢 Inserindo empresa: {empresa}")
                cur.execute("""
                    INSERT INTO TB_EMPRESAS (nome, ticker, setor)
                    VALUES (%s, %s, %s)
                    ON CONFLICT DO NOTHING;
                """, (empresa, row['Ticker'], row['Setor']))
                empresas_inseridas.add(empresa)

        for empresa in empresas_inseridas:
            adotou_ia = bool(df.loc[df['Empresa'] == empresa]['Adotou_IA'].iloc[0])
            cur.execute("""
                INSERT INTO TB_ADOCAO_IA (id_empresa, adotou_ia)
                SELECT id, %s FROM TB_EMPRESAS WHERE nome = %s;
            """, (adotou_ia, empresa))

        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO TB_INVESTIMENTOS (id_empresa, ano, semestre, receita, lucro, roi)
                SELECT id, %s, %s, %s, %s, %s FROM TB_EMPRESAS WHERE nome = %s;
            """, (
                row['Ano'],
                row['Semestre'],
                row['Receita'],
                row['Lucro_Liquido'],
                row['ROI'],
                row['Empresa']
            ))

        conn.commit()
        cur.close()
        conn.close()