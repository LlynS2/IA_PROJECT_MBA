import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from src.IA_TCC.DATABASE.DB_CONFIG import sqlalchemy_engine

class Linear_Regression:
    def __init__(self, connection):
        self.conn = sqlalchemy_engine()
    def interpretar_resultado(self, modelo, nome_modelo):
        print(f"\n📊 Interpretação para {nome_modelo}")
        for var in modelo.params.index:
            coef = modelo.params[var]
            pval = modelo.pvalues[var]

            if pval < 0.05:
                direcao = "positivo" if coef > 0 else "negativo"
                print(f"- {var}: ✅ Significativo ({direcao}), coef = {coef:.2f}, p-valor = {pval:.3f}")
            elif pval < 0.1:
                print(f"- {var}: ❕ Tendência (marginal), coef = {coef:.2f}, p-valor = {pval:.3f}")
            else:
                print(f"- {var}: ❌ Não significativo, coef = {coef:.2f}, p-valor = {pval:.3f}")

    def run(self):
        engine = sqlalchemy_engine()
        df = pd.read_sql_query("""
            SELECT e.nome, e.ticker, e.setor,
                   i.ano , i.semestre,
                   i.receita, i.lucro, i.roi,
                   a.adotou_ia
            FROM tb_investimentos i
            JOIN tb_empresas e ON i.id_empresa = e.id
            JOIN tb_adocao_ia a ON e.id = a.id_empresa
        """, engine)

        df.columns = df.columns.str.strip().str.lower()
        df["setor"] = df["setor"].astype(str).str.strip().str.lower()
        df["ano"] = df["ano"].astype(int)
        df["adotou_ia"] = df["adotou_ia"].astype(int)

        setores = df["setor"].unique()

        for setor in setores:
            print(f"\n\n======================")
            print(f"📊 ANÁLISE - SETOR: {setor.upper()}")
            print(f"======================")

            df_setor = df[df["setor"] == setor].copy()

            print("\nEmpresas analisadas:")
            for adotou in [1, 0]:
                grupo = "Grupo A (Adotou IA)" if adotou else "Grupo B (Não adotou IA)"
                nomes = df_setor[df_setor["adotou_ia"] == adotou]["nome"].unique()
                print(f"- {grupo}: {', '.join(nomes) if len(nomes) > 0 else 'Nenhuma'}")

            for alvo in ["roi", "lucro", "receita"]:
                print(f"\n=== Regressão para {alvo.upper()} ===")

                df_model = df_setor.copy()
                df_model["ia_ano"] = df_model["adotou_ia"] * df_model["ano"]
                df_model = df_model.dropna(subset=[alvo])

                y = df_model[alvo].astype(float)
                X = df_model[["adotou_ia", "ano", "ia_ano"]]
                X = sm.add_constant(X)

                modelo = sm.OLS(y, X).fit()
                print(modelo.summary())
                self.interpretar_resultado(modelo, f"{alvo.upper()} - Setor {setor.capitalize()}")

                plot_df = df_model.copy()
                plot_df["adotou_ia"] = plot_df["adotou_ia"].map({1: "Adotou IA", 0: "Não Adotou IA"})
                agrupado = plot_df.groupby(["ano", "adotou_ia"])[alvo].mean().reset_index()

                plt.figure(figsize=(10, 6))
                sns.lineplot(data=agrupado, x="ano", y=alvo, hue="adotou_ia", marker="o")
                plt.title(f"Evolução de {alvo.capitalize()} - Setor {setor.capitalize()}")
                plt.ylabel(f"{alvo.capitalize()} médio")
                plt.grid(True)
                plt.tight_layout()
                plt.show()