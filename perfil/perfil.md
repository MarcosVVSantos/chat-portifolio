# Ficha do Marcos Vinicio Vieira dos Santos

> Este arquivo é a ÚNICA fonte de verdade do chat. O bot só responde com o que está aqui.
> Para mudar o que o bot sabe, edite este arquivo. Não coloque aqui nada que você não quer que um recrutador leia.

## Resumo

- Marcos Vinicio Vieira dos Santos, de Jandira, SP (região de Osasco).
- Supervisor de operações que automatiza o próprio trabalho com IA: cria skills de LLM, fluxos n8n e pipelines no BigQuery que viram relatórios, alertas e decisões para equipes de campo.
- Construiu do zero um agente de WhatsApp com tool calling e servidor MCP, testado em piloto real com cliente.
- Objetivo profissional: transformar problemas de operação em agentes e ferramentas de IA. Busca oportunidades em IA aplicada, no perfil de "AI Builder": usar IA para construir soluções de ponta a ponta.
- O diferencial dele é juntar três coisas que raramente vêm juntas: experiência de operação (sabe onde dói), dados (SQL, BigQuery, Power BI) e desenvolvimento com IA (agentes, LLMs, MCP).

## Experiência

### Mottu (aluguel de motos, operação nacional) | mai/2022 – atual

**Supervisor de Field Services Sr | ago/2026 – atual**
- Lidera uma equipe de 49 pessoas (15 reportes diretos) de recolhimento de veículos em 4 estados, priorizando expedições por custo e distância com dados do BigQuery.
- Automatizou os relatórios semanais de inadimplência e de parceiros com skills próprias no Claude (Anthropic).
- Criou um treinamento de abordagem para motoristas com quiz e correção automática (Google Apps Script/Forms), aplicado a toda a base de líderes do suporte de rua.

**Supervisor de Monitoramento I | jun/2025 – out/2026**
- Reduziu a perda de ativos de 1,28% para 0,51%, reestruturando os pipelines de dados (BigQuery/Dataform) e o acompanhamento diário da operação.
- Estruturou do zero o monitoramento de inadimplência e recuperação de ativos, com KPIs diários por filial e parceiro, cobrindo mais de 240 parceiros terceirizados em vários estados.
- Construiu fluxos n8n que levam dados do BigQuery para as APIs das filiais e disparam notificações por fase de cobrança (WebEngage/Novu).
- Desenvolveu um sistema que recomenda o destino de motos recolhidas (filial ou parceiro) ordenado por custo, usando cálculo de distância geoespacial no BigQuery.
- Criou dashboards em Power BI (funil de inadimplência, pré-apropriação, produtividade de parceiros) usados por gestores regionais e nacionais.

**Fleet Analyst | dez/2024 – jul/2025**
- Criou painéis de performance da frota em Power BI usados nas decisões de gestão da frota.

**Customer Success Analyst (dez/2023 – dez/2024) e Front-atendimento (mai/2022 – fev/2024)**
- Mapeou padrões em solicitações recorrentes de parceiros e implementou soluções de suporte que otimizaram o atendimento.

**Antes da Mottu:** Assistente administrativo na Prefeitura de Santana de Parnaíba (jul/2020 – mai/2022).

## Projetos (missões concluídas)

### Fleet AI Analyst: agente de análise de dados de frota
- Demo online: https://fleet-ai-analyst-marcos.streamlit.app
- Código: https://github.com/MarcosVVSantos/fleet-ai-analyst
- O que é: um agente text-to-SQL. Você pergunta em português sobre a operação de uma frota (recolhimentos, inadimplência, parceiros) e o LLM (DeepSeek) gera o SQL, que é validado com sqlglot, executado no DuckDB e devolvido com conclusão, tabela e gráfico em Streamlit. Os dados são fictícios.
- Segurança: só deixa rodar consultas de leitura; 11 tentativas de injeção de SQL são bloqueadas nos testes.
- Eval: 20 perguntas com respostas de referência. O primeiro resultado foi 55%. Ao investigar os erros, ele descobriu que o problema estava em regras de negócio ambíguas e num avaliador rígido demais, não no modelo. Depois de documentar as regras, o acerto chegou a 100% na última execução. 23 testes automatizados.
- Indicado para quem procura: análise de dados com IA, text-to-SQL, avaliação de LLMs (evals), demo construída em poucos dias.

### Barbershop Bot / NuvoData: agente de WhatsApp para pequenos negócios
- Código: https://github.com/MarcosVVSantos/barbershop-bot
- O que é: um agente em que o LLM (DeepSeek) usa tool calling para escolher entre 21 ferramentas de um servidor MCP (FastMCP): agendar, cancelar, confirmar presença, vender produtos e gerar o relatório mensal do dono. Gateway FastAPI, SQLite, Google Calendar, Docker Compose.
- Multi-tenant: o mesmo motor atende barbearia, adega ou nutricionista trocando um arquivo JSON de configuração.
- Anti-alucinação: injeta no contexto os IDs reais do cliente e dos agendamentos antes de cada resposta, para o modelo nunca inventar dados.
- 94 testes automatizados, organizados em 4 fases de uma especificação de dados (estados do agendamento, confirmação prévia, no-show, relatório mensal).
- Rodou num piloto real numa barbearia (hoje pausado). O número do piloto foi banido pelo WhatsApp por usar uma API não oficial; a decisão foi migrar para a WhatsApp Cloud API oficial da Meta. O motor está sendo adaptado para gestão de pequenas frotas, com a marca NuvoData.
- Indicado para quem procura: agentes de IA, MCP, tool calling, integração com WhatsApp, produto de IA para negócio real.

### Chat-currículo (este chat)
- Código: https://github.com/MarcosVVSantos/chat-portifolio
- O que é: este próprio chat. Um LLM responde perguntas de recrutadores usando só uma ficha revisada pelo Marcos, com travas para não inventar informação.

### TrackHub: plataforma colaborativa para produtores musicais ("GitHub para música")
- Demo online: https://trackhub-v3.vercel.app
- Código: https://github.com/MarcosVVSantos/TrackHub-v3
- O que é: plataforma para produtores musicais organizarem projetos, colaborarem e verem analytics. A versão atual (v3) é um monorepo com API em Node.js + Express + Prisma (MySQL) e front-end em React + Vite + TailwindCSS, com o front publicado na Vercel.
- Versão anterior, em Java/Spring Boot com autenticação JWT, JPA/MySQL e React: https://github.com/MarcosVVSantos/TrackHub-TheProject
- Indicado para quem procura: desenvolvimento full-stack, produto web do zero, modelagem relacional.

### Outros projetos no GitHub
- Controle Consultório: sistema fullstack de gestão de consultório com Node.js/Express, React, Sequelize e MySQL. https://github.com/MarcosVVSantos/controle-consultorio
- Perfil completo no GitHub: https://github.com/MarcosVVSantos

## Competências

- IA generativa: LLMs (Claude, DeepSeek), agentes com tool calling, MCP (FastMCP), text-to-SQL, avaliação de LLMs (evals), prompt engineering, skills e Claude Code.
- Automação: n8n, Google Apps Script, GitHub Actions, APScheduler, integração por APIs REST.
- Dados: SQL (BigQuery, Dataform, DuckDB), Power BI (DAX), Python (Pandas), Streamlit, análise geoespacial.
- Desenvolvimento: Python/FastAPI, Docker, Java/Spring Boot, Node.js, React, React Native, Kotlin/Android.
- Liderança e operação: gestão de equipe de campo, KPIs, priorização por custo, comunicação com times técnicos e não técnicos.

## Formação

- Tecnólogo em Desenvolvimento de Software Multiplataforma, FATEC Cotia, ago/2024 – ago/2027 (previsão). Disciplinas relevantes: Aprendizagem de Máquina, Computação em Nuvem, Banco de Dados, Segurança da Informação, Desenvolvimento Mobile.
- Técnico em Administração, Etec Prefeito Braz Paschoalin, 2016 – 2018.

## Idiomas

- Português nativo.
- Inglês intermediário (B1): lê documentação técnica e se comunica por escrito.

## Contato

- E-mail: marcos28.vinicio@gmail.com
- LinkedIn: https://www.linkedin.com/in/marcos-v-v-santos
- GitHub: https://github.com/MarcosVVSantos

## Assuntos que o chat NÃO responde (encaminhar para o Marcos)

- Pretensão salarial, benefícios e negociação.
- Disponibilidade de início, horários e modelo de trabalho.
- Vida pessoal, família, saúde, religião, política.
- Dados internos da Mottu além do que está nesta ficha.
- Qualquer coisa que não esteja escrita nesta ficha.
