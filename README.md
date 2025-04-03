<div align="right">
  Otros idiomas : <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Português" target="_blank">Português <img src="https://github.com/user-attachments/assets/fa0289cd-3feb-4b62-a6b5-19d80a95a50c" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA" target="_blank">English <img src="https://github.com/user-attachments/assets/8e065c04-101a-4fd8-814c-b8e6778fca1a" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/中文" target="_blank">中文 <img src="https://github.com/user-attachments/assets/e3939437-846c-452f-b2a8-ec4dc394d7d9" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/한국어" target="_blank">한국어 <img src="https://github.com/user-attachments/assets/5f6886c4-4a79-49b7-b33c-053e1b7ba8c4" width="17"></a>
</div><br>
<div align="center">
  <h1>IA Estratégica: Impactos Financieros, Crecimiento Corporativo y los Nuevos Desafíos del Liderazgo Empresarial</h1>
  <p>Este repositorio presenta la aplicación práctica de técnicas de análisis de datos, modelado estadístico y observabilidad para investigar los impactos financieros de la adopción de Inteligencia Artificial (IA) en los sectores de tecnología, finanzas e industria.
     Desarrollado como proyecto final del MBA en Ingeniería de Software (USP/Esalq), este estudio combina rigor académico con visión empresarial, entregando un código limpio, reutilizable y orientado a la toma de decisiones.</p>
</div>

<div>
   <h2>𝐒𝐨𝐛𝐫𝐞 𝐞𝐥 𝐏𝐫𝐨𝐲𝐞𝐜𝐭𝐨 ✍</h2>
    <p>El proyecto aplica técnicas de Regresión Lineal Múltiple para analizar si la adopción de la IA tuvo un impacto estadístico en los indicadores financieros de las empresas, siendo estos:</p>
    <ul>
        <li>Ingresos</li>
        <li>Ganancia</li>
        <li>ROI (Retorno sobre la Inversión)</li>
    </ul>
    <p>La base de datos fue construida con información real extraída de plataformas como <b>Yahoo Finance, Google Finance, TradingView, entre otras fuentes públicas</b>, cubriendo el período de 2020 a 2024. Los datos fueron recolectados en una <b>hoja de cálculo de Excel</b>, pero su <b>conexión, modelado e inserción</b> se realizaron a través de una base de datos <b>PostgreSQL</b>, utilizando una herramienta de gestión de bases de datos llamada <b>DBeaver</b> <i>(*No obligatorio)</i></p>

    <h2>🤖 𝐓𝐞𝐜𝐧𝐨𝐥𝐨𝐠𝐢́𝐚𝐬 𝐔𝐭𝐢𝐥𝐢𝐳𝐚𝐝𝐚𝐬</h2>
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
    <h2>𝐁𝐚𝐬𝐞 𝐝𝐞 𝐃𝐚𝐭𝐨𝐬 🧠</h2>
    <p>Los datos fueron organizados en una base de datos relacional PostgreSQL, cuya estructura se compone de las siguientes tablas:</p>
    <ul>
        <li><strong>Tabla <code>empresas</code></strong>: Información sobre las empresas analizadas</li>
        <li><strong>Tabla <code>inversiones</code></strong>: Datos semestrales de ingresos, ganancias y ROI</li>
        <li><strong>Tabla <code>ia_adopcion</code></strong>: Estado de adopción de IA por empresa y año</li>
    </ul>
   <div align="center" >
      <h3>DIAGRAMA ER (MODELADO)</h3>
    <img src="https://github.com/user-attachments/assets/c1b92ac3-7c77-4c0a-96a4-d06dd1e6a4c7" alt="ER Diagram" width="950">
   </div>
    <h3>👉 ɪᴍᴩᴏʀᴛᴀɴᴛᴇ 👇</h3>
    <p>Puedes ajustar el archivo <code>db_config.py</code> con tus credenciales para conectarte a la base de datos:</p>
    <pre><code>DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'TCC_MBA_COMPANIES_IA',
    'user': 'tu_usuario',
    'password': 'tu_contraseña' }
    </code></pre>
</div>

<div>
    <h2>𝐂𝐨́𝐦𝐨 𝐞𝐣𝐞𝐜𝐮𝐭𝐚𝐫 𝐞𝐥 𝐩𝐫𝐨𝐲𝐞𝐜𝐭𝐨 ❓</h2>
   <ul>
        <li><strong>Clona el repositorio</strong><br><code>git clone https://github.com/tu-usuario/IA_PROJECT_MBA.git</code></li>
        <li><strong>Configura el entorno</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>Configura la base de datos</strong><br>Edita el archivo <code>db_config.py</code> con tus credenciales</li>
        <li><strong>Ejecuta el análisis</strong><br><code>python src/IA_TCC/main.py</code></li>
    </ul>
    <p>¡Listo! Los resultados de la regresión se imprimirán en la consola junto con los gráficos para visualización y análisis.
</div><br>

<div align="center">
   <p>
      <div align="center">
         <img src="https://github.com/user-attachments/assets/2005b055-a382-401c-8f93-f22a5b0eedc8" alt="License" width="150">
         <p>Este proyecto está licenciado bajo la <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPL-3.0</a></p>
      </div>
      <strong>Proyecto desarrollado por Hevellyn Mc'Frei – XRevolution Technologies</strong> | Todos los derechos reservados © 2025.
   </p>
</div>
