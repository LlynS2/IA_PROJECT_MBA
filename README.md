<div align="right">
   Other languages : <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Português" target="_blank">Português <img src="https://github.com/user-attachments/assets/fa0289cd-3feb-4b62-a6b5-19d80a95a50c" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Español" target="_blank">Español <img src="https://github.com/user-attachments/assets/0a4eb85c-cd21-43fc-bd98-7c1042f7b08e" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/中文" target="_blank">中文 <img src="https://github.com/user-attachments/assets/e3939437-846c-452f-b2a8-ec4dc394d7d9" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/한국어" target="_blank">한국어 <img src="https://github.com/user-attachments/assets/5f6886c4-4a79-49b7-b33c-053e1b7ba8c4" width="17"></a>
</div><br>
<div align="center">
  <h1>IA Estratégica: Impactos Financeiros, Crescimento Corporativo e os Novos Desafios da Liderança Empresarial</h1>
  <p>Este repositório apresenta a aplicação prática de técnicas de análise de dados, modelagem estatística e observabilidade para investigar os impactos financeiros da adoção da Inteligência Artificial (IA) nos setores de tecnologia, finanças e indústria.
     Desenvolvido como projeto de conclusão do MBA em Engenharia de Software (USP/Esalq), este estudo combina rigor acadêmico com visão de negócios, entregando um código limpo, reutilizável e orientado à tomada de decisão.</p>
</div>
<div>
   <h2>𝐒𝐨𝐛𝐫𝐞 𝐨 𝐏𝐫𝐨𝐣𝐞𝐭𝐨 ✍</h2>
    <p>O projeto aplica técnicas de Regressão Linear Múltipla para analisar se a adoção da Inteligência Artificial impactou estatisticamente os indicadores financeiros das empresas, sendo eles :</p>
    <ul>
        <li>Receita</li>
        <li>Lucro</li>
        <li>ROI ( Retorno sobre Investimento )</li>
    </ul>
    <p>A base de dados foi construída com informações reais extraídas de plataformas como <b>Yahoo Finance, Google Finance, TradingView, entre outras fontes públicas</b>, cobrindo o período de 2020 a 2024. Os dados foram levantados em uma <b>planilha excel</b>, mas sua <b>conexão, modelagem e inserção</b> foram utilizados via banco <b>PostgreSQL</b>, utilizando uma ferramenta de gerencimaneto de banco de dados chamado <b>DBeaver</b> <i>( *Não obrigatório )</i></p>
    <h2>🤖 𝐓𝐞𝐜𝐧𝐨𝐥𝐨𝐠𝐢𝐚𝐬 𝐔𝐭𝐢𝐥𝐢𝐳𝐚𝐝𝐚𝐬</h2>
   <table>
      <tbody>
      <tr>
        <td><img src="https://github.com/user-attachments/assets/79b00d68-5931-4f9e-921d-09c779c6edc6" alt="Python" width="55"></td>
        <td>Python 3.10</td>
        <td><img src="https://github.com/user-attachments/assets/41616e29-7bff-4bae-8523-684ff3dd9ca1" alt="Alura" width="55"></td>
        <td>PostgreSQL</td>
        <td><img src="https://github.com/user-attachments/assets/41616e29-7bff-4bae-8523-684ff3dd9ca1" alt="Alura" width="55"></td>
        <td>Pandas</td>
        <td><img src="https://github.com/user-attachments/assets/41616e29-7bff-4bae-8523-684ff3dd9ca1" alt="Alura" width="55"></td>
        <td>Statsmodels</td>
        <td><img src="https://github.com/user-attachments/assets/41616e29-7bff-4bae-8523-684ff3dd9ca1" alt="Alura" width="55"></td>
        <td>Matplotlib</td>
        <td><img src="https://github.com/user-attachments/assets/41616e29-7bff-4bae-8523-684ff3dd9ca1" alt="Alura" width="55"></td>
        <td>DBeaver</td>
      </tr>
    </tbody>
   </table>
   <div>
    <h2>𝐁𝐚𝐧𝐜𝐨 𝐝𝐞 𝐃𝐚𝐝𝐨𝐬 🧠</h2>
    <p>Os dados foram organizados em um banco de dados relacional PostgreSQL, sendo a estrutura foi composta pelas tabelas :</p>
    <ul>
        <li><strong>Tabela <code>empresas</code></strong>: Informações das empresas analisadas</li>
        <li><strong>Tabela <code>investimentos</code></strong>: Dados semestrais de receita, lucro e ROI</li>
        <li><strong>Tabela <code>ia_adocao</code></strong>: Status de adoção de IA por empresa e ano</li>
    </ul>
   <div align="center" >
      <h3>DIAGRAMA ER ( MODELAGEM )<h3>
    <img src="https://github.com/user-attachments/assets/c1b92ac3-7c77-4c0a-96a4-d06dd1e6a4c7" alt="Alura" width="950">
   </div>
    <h3>👉 ɪᴍᴘᴏʀᴛᴀɴᴛᴇ 👇</h3>
    <p>Você pode ajustar o arquivo <code>db_config.py</code> com suas credenciais para a conexão no banco de dados :</p>
    <pre><code>DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'TCC_MBA_COMPANIES_IA',
    'user': 'seu_usuario',
    'password': 'sua_senha' }
    </code></pre>
</div>
<div>
    <h2>𝐂𝐨𝐦𝐨 𝐞𝐱𝐞𝐜𝐮𝐭𝐚𝐫 𝐨 𝐩𝐫𝐨𝐣𝐞𝐭𝐨 ❓</h2>
   <ul>
        <li><strong>Clone o repositório</strong><br><code>git clone https://github.com/seu-usuario/IA_PROJECT_MBA.git</code></li>
        <li><strong>Configure o ambiente</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>Configure o banco de dados</strong><br> Edite <code>db_config.py</code> com suas credenciais</li>
        <li><strong>Execute o cáculo</strong><br><code>python src/IA_TCC/main.py</code></li>
    </ul>
    <p>Pronto ! Os resultados da regressão serão impressos no console junto aos gráficos para a visualização e análise.
</div><br>
<div align="center">
   <p>
      <div align="center">
         <img src="https://github.com/user-attachments/assets/2005b055-a382-401c-8f93-f22a5b0eedc8" alt="License" width="150">
         <p>Este projeto está licenciado sob a <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPL-3.0</a></p>
      </div>
      <strong>Projeto desenvolvido por Hevellyn Mc'Frei – XRevolution Technologies</strong> | Todos os direitos reservados © 2025.
   </p>
</div>
