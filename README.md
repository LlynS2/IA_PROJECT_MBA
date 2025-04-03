<div align="right">
  其他语言 : <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Português" target="_blank">Português <img src="https://github.com/user-attachments/assets/fa0289cd-3feb-4b62-a6b5-19d80a95a50c" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA" target="_blank">English <img src="https://github.com/user-attachments/assets/8e065c04-101a-4fd8-814c-b8e6778fca1a" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Español" target="_blank">Español <img src="https://github.com/user-attachments/assets/0a4eb85c-cd21-43fc-bd98-7c1042f7b08e" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/한국어" target="_blank">한국어 <img src="https://github.com/user-attachments/assets/5f6886c4-4a79-49b7-b33c-053e1b7ba8c4" width="17"></a></div><br>
<div align="center">
  <h1>战略性人工智能：财务影响、企业增长与新时代领导力挑战</h1>
  <p>本仓库展示了数据分析、统计建模与可观察性技术的实际应用，用于研究人工智能（AI）在技术、金融与工业领域的采用所带来的财务影响。
     本项目作为圣保罗大学（USP/Esalq）软件工程MBA的毕业研究，结合了学术严谨性与商业视角，提供了一个结构清晰、可复用并以决策为导向的代码基础。</p>
</div>

<div>
   <h2>𝐀𝐛𝐨𝐮𝐭 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 ✍</h2>
    <p>该项目应用多元线性回归技术，分析人工智能的采用是否对企业的财务指标产生了统计显著的影响，包括：</p>
    <ul>
        <li>收入</li>
        <li>利润</li>
        <li>投资回报率（ROI）</li>
    </ul>
    <p>数据基础来自于 <b>Yahoo Finance、Google Finance、TradingView</b> 等公共平台，覆盖 2020 至 2024 年的真实企业数据。最初整理于 <b>Excel 电子表格</b>，并通过 <b>PostgreSQL</b> 数据库进行建模与插入，使用 <b>DBeaver</b> 数据库管理工具辅助（<i>*非必需</i>）。</p>
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
    <p>数据被组织在一个关系型数据库 PostgreSQL 中，结构包含以下表：</p>
    <ul>
        <li><strong><code>empresas</code> 表</strong>：被分析企业的信息</li>
        <li><strong><code>investimentos</code> 表</strong>：半年期的收入、利润与 ROI 数据</li>
        <li><strong><code>ia_adocao</code> 表</strong>：企业每年的人工智能采用状态</li>
    </ul>
   <div align="center">
      <h3>ER 图（建模）</h3>
      <img src="https://github.com/user-attachments/assets/c1b92ac3-7c77-4c0a-96a4-d06dd1e6a4c7" alt="ER Diagram" width="950">
   </div>
    <h3>👉 重 要 提 示 👇</h3>
    <p>你可以根据自己的数据库连接信息修改 <code>db_config.py</code> 文件：</p>
    <pre><code>DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'TCC_MBA_COMPANIES_IA',
    'user': '你的用户名',
    'password': '你的密码' }
    </code></pre>
</div>

<div>
    <h2>𝐇𝐨𝐰 𝐭𝐨 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 ❓</h2>
   <ul>
        <li><strong>克隆项目仓库</strong><br><code>git clone https://github.com/seu-usuario/IA_PROJECT_MBA.git</code></li>
        <li><strong>配置运行环境</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>配置数据库</strong><br>编辑 <code>db_config.py</code> 文件填入数据库信息</li>
        <li><strong>运行分析代码</strong><br><code>python src/IA_TCC/main.py</code></li>
    </ul>
    <p>完成！控制台将显示回归分析结果，并自动生成图表以辅助可视化和分析。
</div><br>

<div align="center">
   <p>
      <div align="center">
         <img src="https://github.com/user-attachments/assets/2005b055-a382-401c-8f93-f22a5b0eedc8" alt="License" width="150">
         <p>本项目基于 <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPL-3.0</a> 许可证发布</p>
      </div>
      <strong>由 Hevellyn Mc'Frei – XRevolution Technologies 开发</strong> | 版权所有 © 2025
   </p>
</div>
