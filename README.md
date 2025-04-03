<div align="right">
   Other languages : <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Português" target="_blank">Português <img src="https://github.com/user-attachments/assets/fa0289cd-3feb-4b62-a6b5-19d80a95a50c" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Español" target="_blank">Español <img src="https://github.com/user-attachments/assets/0a4eb85c-cd21-43fc-bd98-7c1042f7b08e" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/中文" target="_blank">中文 <img src="https://github.com/user-attachments/assets/e3939437-846c-452f-b2a8-ec4dc394d7d9" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/한국어" target="_blank">한국어 <img src="https://github.com/user-attachments/assets/5f6886c4-4a79-49b7-b33c-053e1b7ba8c4" width="17"></a>
</div><br>
<div align="center">
  <h1>Strategic AI: Financial Impacts, Corporate Growth, and the New Challenges of Business Leadership</h1>
  <p>This repository presents the practical application of data analysis, statistical modeling, and observability techniques to investigate the financial impacts of Artificial Intelligence (AI) adoption in the technology, finance, and industry sectors.
     Developed as a capstone project for the MBA in Software Engineering (USP/Esalq), this study combines academic rigor with business insight, delivering clean, reusable, and decision-oriented code.</p>
</div>

<div>
   <h2>𝐀𝐛𝐨𝐮𝐭 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 ✍</h2>
    <p>The project applies Multiple Linear Regression techniques to analyze whether AI adoption had a statistical impact on companies' financial indicators, which include:</p>
    <ul>
        <li>Revenue</li>
        <li>Profit</li>
        <li>ROI (Return on Investment)</li>
    </ul>
    <p>The database was built with real data extracted from platforms like <b>Yahoo Finance, Google Finance, TradingView, among other public sources</b>, covering the period from 2020 to 2024. The data was initially gathered in an <b>Excel spreadsheet</b>, but its <b>connection, modeling, and insertion</b> were handled using a <b>PostgreSQL</b> database, with the help of a management tool called <b>DBeaver</b> <i>(*Optional)</i></p>
    <h2>🤖 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬 𝐔𝐬𝐞𝐝</h2>
   <table>
      <tbody>
      <tr>
        <td><img src="https://github.com/user-attachments/assets/79b00d68-5931-4f9e-921d-09c779c6edc6" alt="Python" width="95"></td>
        <td>Python 3.10</td>
        <td><img src="https://github.com/user-attachments/assets/f8ddd777-b71b-430d-9eda-d69ce34e5d4e" alt="PostgreSQL" width="95"></td>
        <td>PostgreSQL</td>
        <td><img src="https://github.com/user-attachments/assets/79b3568c-817d-42e0-a606-fe646144dc82" alt="Pandas" width="95"></td>
        <td>Pandas</td>
        <td><img src="https://github.com/user-attachments/assets/c6d8e24a-d8a2-4e49-9a55-4aa5127a66bc" alt="Statsmodels" width="95"></td>
        <td>Statsmodels</td>
        <td><img src="https://github.com/user-attachments/assets/25366bfd-8d8e-4c03-bc5b-26b7eb6e0717" alt="Matplotlib" width="95"></td>
        <td>Matplotlib</td>
        <td><img src="https://github.com/user-attachments/assets/3a09892a-3aa3-4eb9-ab55-517132968b6e" alt="DBeaver" width="95"></td>
        <td>DBeaver</td>
      </tr>
    </tbody>
   </table>

   <div>
    <h2>𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 🧠</h2>
    <p>The data was organized in a relational PostgreSQL database, structured with the following tables:</p>
    <ul>
        <li><strong><code>companies</code> table</strong>: Information about the analyzed companies</li>
        <li><strong><code>investments</code> table</strong>: Semiannual data on revenue, profit, and ROI</li>
        <li><strong><code>ia_adoption</code> table</strong>: AI adoption status by company and year</li>
    </ul>
   <div align="center" >
      <h3>ER DIAGRAM (MODELING)<h3>
    <img src="https://github.com/user-attachments/assets/c1b92ac3-7c77-4c0a-96a4-d06dd1e6a4c7" alt="ER Diagram" width="950">
   </div>
    <h3>👉 ɪᴍᴘᴏʀᴛᴀɴᴛ 👇</h3>
    <p>You can adjust the <code>db_config.py</code> file with your credentials to connect to the database:</p>
    <pre><code>DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'TCC_MBA_COMPANIES_IA',
    'user': 'your_user',
    'password': 'your_password' }
    </code></pre>
</div>

<div>
    <h2>𝐇𝐨𝐰 𝐭𝐨 𝐫𝐮𝐧 𝐭𝐡𝐞 𝐩𝐫𝐨𝐣𝐞𝐜𝐭 ❓</h2>
   <ul>
        <li><strong>Clone the repository</strong><br><code>git clone https://github.com/your-username/IA_PROJECT_MBA.git</code></li>
        <li><strong>Set up the environment</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>Configure the database</strong><br>Edit <code>db_config.py</code> with your credentials</li>
        <li><strong>Run the analysis</strong><br><code>python src/IA_TCC/main.py</code></li>
    </ul>
    <p>Done! The regression results will be printed in the console along with charts for visualization and analysis.
</div><br>

<div align="center">
   <p>
      <div align="center">
         <img src="https://github.com/user-attachments/assets/2005b055-a382-401c-8f93-f22a5b0eedc8" alt="License" width="150">
         <p>This project is licensed under the <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPL-3.0</a></p>
      </div>
      <strong>Project developed by Hevellyn Mc'Frei – XRevolution Technologies</strong> | All rights reserved © 2025.
   </p>
</div>
