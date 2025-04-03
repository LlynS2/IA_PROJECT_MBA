<div align="right">
   Other languages : <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Português" target="_blank">Português <img src="https://github.com/user-attachments/assets/fa0289cd-3feb-4b62-a6b5-19d80a95a50c" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Español" target="_blank">Español <img src="https://github.com/user-attachments/assets/0a4eb85c-cd21-43fc-bd98-7c1042f7b08e" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/中文" target="_blank">中文 <img src="https://github.com/user-attachments/assets/e3939437-846c-452f-b2a8-ec4dc394d7d9" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/한국어" target="_blank">한국어 <img src="https://github.com/user-attachments/assets/5f6886c4-4a79-49b7-b33c-053e1b7ba8c4" width="17"></a>
</div><br>
<div align="center">
  <h1>Strategic AI: Financial Impacts, Corporate Growth, and the New Challenges of Business Leadership</h1>
</div>
<div>
    <p>Este repositório contém o código-fonte do projeto de conclusão de curso do MBA em Engenharia de Software (USP/Esalq), cujo objetivo foi analisar os impactos financeiros da adoção da Inteligência Artificial (IA) em empresas dos setores de tecnologia, finanças e indústria.</p>
</div>
<div>
   <h2>🧠 Sobre o Projeto</h2>
    <p>O projeto aplica técnicas de regressão linear múltipla para analisar se a adoção de IA impactou estatisticamente os indicadores financeiros:</p>
    <ul>
        <li>Receita</li>
        <li>Lucro</li>
        <li>ROI (Retorno sobre Investimento)</li>
    </ul>
    <p>A base de dados foi construída com informações reais extraídas de plataformas como Yahoo Finance, Google Finance, TradingView, entre outras fontes públicas, cobrindo o período de 2020 a 2024.</p>
    <h2>🛠️ Tecnologias Utilizadas</h2>
    <ul>
        <li>Python 3.10+</li>
        <li>PostgreSQL</li>
        <li>Pandas</li>
        <li>Statsmodels</li>
        <li>Matplotlib</li>
        <li>DBeaver (opcional)</li>
    </ul>
    <h2>💾 Banco de Dados</h2>
    <p>Os dados foram organizados em um banco de dados relacional PostgreSQL. A estrutura foi composta por:</p>
    <ul>
        <li><strong>Tabela <code>empresas</code></strong>: informações das empresas analisadas</li>
        <li><strong>Tabela <code>financeiros</code></strong>: dados semestrais de receita, lucro e ROI</li>
        <li><strong>Tabela <code>ia_adocao</code></strong>: status de adoção de IA por empresa e ano</li>
    </ul>
    <p>Você pode ajustar o arquivo <code>db_config.py</code> com suas credenciais:</p>
    <pre><code>DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'ia_tcc',
    'user': 'seu_usuario',
    'password': 'sua_senha'
}
</div>
<div>
    <h2>▶️ Como Executar o Projeto</h2>
    <ol>
        <li><strong>Clone o repositório</strong><br>
        <code>git clone https://github.com/seu-usuario/IA_PROJECT_MBA.git</code></li>
        <li><strong>Configure o ambiente</strong><br>
        <code>pip install -r requirements.txt</code></li>
        <li><strong>Configure o banco de dados</strong><br>
        - Importe o schema.sql para seu PostgreSQL<br>
        - Edite <code>db_config.py</code> com suas credenciais</li>
        <li><strong>Execute os testes</strong><br>
        <code>python src/IA_TCC/t_test_manager.py</code></li>
    </ol>
    <p>Os resultados da regressão serão impressos no console e salvos em arquivos <code>.csv</code> na pasta <code>/results</code> (se habilitado).</p>
</div>
<div align="center">
   <p>Projeto desenvolvido por Hevellyn Mc'Frei - XRevolution Technologies | Todos os direitos reservados (2025).</p><br>
   <p>Este projeto sob a <a href="LICENSE">Licença MIT</a>.</p>
</div>
