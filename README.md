<div align="right">
  다른 언어 : <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Português" target="_blank">Português <img src="https://github.com/user-attachments/assets/fa0289cd-3feb-4b62-a6b5-19d80a95a50c" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA" target="_blank">English <img src="https://github.com/user-attachments/assets/8e065c04-101a-4fd8-814c-b8e6778fca1a" width="15"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/Español" target="_blank">Español <img src="https://github.com/user-attachments/assets/0a4eb85c-cd21-43fc-bd98-7c1042f7b08e" width="17"></a> | <a href="https://github.com/LlynS2/IA_PROJECT_MBA/tree/中文" target="_blank">中文 <img src="https://github.com/user-attachments/assets/e3939437-846c-452f-b2a8-ec4dc394d7d9" width="17"></a>
</div><br>
<div align="center">
  <h1>전략적 인공지능: 재무적 영향, 기업 성장 및 새로운 리더십 도전</h1>
  <p>이 저장소는 기술, 금융 및 산업 분야에서 인공지능(AI) 도입이 재무 성과에 미치는 영향을 분석하기 위해 데이터 분석, 통계 모델링 및 가시성 기술을 실무에 적용한 프로젝트입니다. 
     본 프로젝트는 상파울루 대학교(USP/Esalq) 소프트웨어 엔지니어링 MBA 졸업 연구로 개발되었으며, 학문적 엄밀성과 비즈니스 통찰력을 결합하여 깔끔하고 재사용 가능하며 의사결정 지향적인 코드를 제공합니다.</p>
</div>

<div>
   <h2>𝐀𝐛𝐨𝐮𝐭 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 ✍</h2>
    <p>이 프로젝트는 다중 선형 회귀 분석(Multiple Linear Regression)을 활용하여 AI 도입이 다음과 같은 재무 지표에 통계적으로 유의미한 영향을 미쳤는지를 평가합니다:</p>
    <ul>
        <li>수익 (Revenue)</li>
        <li>이익 (Profit)</li>
        <li>투자 수익률 (ROI)</li>
    </ul>
    <p>데이터는 <b>Yahoo Finance, Google Finance, TradingView</b> 등 공개 소스를 기반으로 수집되었으며, 2020년부터 2024년까지의 기간을 포괄합니다. 초기 데이터는 <b>Excel 시트</b>로 정리되었고, 이후 <b>PostgreSQL</b> 데이터베이스로 연결 및 삽입되었으며, <b>DBeaver</b>라는 데이터베이스 관리 툴을 사용했습니다 (<i>*필수는 아님</i>)</p>
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
    <p>데이터는 관계형 데이터베이스인 PostgreSQL에 구성되었으며, 구조는 다음과 같은 테이블로 이루어져 있습니다:</p>
    <ul>
        <li><strong><code>empresas</code> 테이블</strong>: 분석 대상 기업 정보</li>
        <li><strong><code>investimentos</code> 테이블</strong>: 반기 수익, 이익 및 ROI 데이터</li>
        <li><strong><code>ia_adocao</code> 테이블</strong>: 기업의 연도별 AI 도입 여부</li>
    </ul>
   <div align="center">
      <h3>ER 다이어그램 (데이터 모델링)</h3>
      <img src="https://github.com/user-attachments/assets/c1b92ac3-7c77-4c0a-96a4-d06dd1e6a4c7" alt="ER Diagram" width="950">
   </div>
    <h3>👉 중요 사항 👇</h3>
    <p><code>db_config.py</code> 파일을 수정하여 본인의 데이터베이스 환경에 맞게 구성하세요:</p>
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
        <li><strong>저장소 클론</strong><br><code>git clone https://github.com/seu-usuario/IA_PROJECT_MBA.git</code></li>
        <li><strong>가상환경 및 종속성 설치</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>데이터베이스 설정</strong><br> <code>db_config.py</code> 파일을 사용자 정보로 수정</li>
        <li><strong>분석 실행</strong><br><code>python src/IA_TCC/main.py</code></li>
    </ul>
    <p>분석이 완료되면 결과는 콘솔에 출력되며, 시각화를 위한 그래프가 자동으로 생성됩니다.
</div><br>

<div align="center">
   <p>
      <div align="center">
         <img src="https://github.com/user-attachments/assets/2005b055-a382-401c-8f93-f22a5b0eedc8" alt="License" width="150">
         <p>이 프로젝트는 <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank">AGPL-3.0</a> 라이선스 하에 배포됩니다.</p>
      </div>
      <strong>이 프로젝트는 Hevellyn Mc'Frei – XRevolution Technologies에 의해 개발되었습니다.</strong> | 모든 권리 보유 © 2025.
   </p>
</div>
