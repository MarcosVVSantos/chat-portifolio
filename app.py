"""MARCOS.EXE: currículo interativo com IA em estilo de game retrô. Rodar com: streamlit run app.py"""
from __future__ import annotations

import os

import streamlit as st

from chat_curriculo.chat import (
    MAX_PERGUNTAS_SESSAO, RESPOSTAS_DEMO, carregar_perfil, cliente_openai,
    montar_mensagens, montar_prompt_sistema, resposta_demo, validar_pergunta,
)

st.set_page_config(page_title="MARCOS.EXE · currículo interativo", page_icon="👾", layout="centered")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

:root {
  --bg: #0b0d2b; --painel: #14174a; --borda: #f5f5f5;
  --vermelho: #e4000f; --azul: #2e6bff; --amarelo: #ffd400; --verde: #00c853;
  --texto: #e8ecff; --apagado: #8f96d6;
}

/* Fundo com estrelas e efeito de TV de tubo */
[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(1px 1px at 20% 30%, #fff8 50%, transparent 51%),
    radial-gradient(1px 1px at 70% 80%, #fff6 50%, transparent 51%),
    radial-gradient(2px 2px at 40% 60%, #fff5 50%, transparent 51%),
    radial-gradient(1px 1px at 85% 20%, #fff7 50%, transparent 51%),
    radial-gradient(ellipse at center, #1a1f6b 0%, var(--bg) 70%);
  background-size: 220px 220px, 300px 300px, 260px 260px, 180px 180px, 100% 100%;
}
[data-testid="stAppViewContainer"]::after {
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 999;
  background: repeating-linear-gradient(to bottom, rgba(0,0,0,.18) 0 1px, transparent 1px 3px);
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stMainBlockContainer"], .block-container { padding-top: 3.5rem !important; }
.menu-titulo { font-family: 'Press Start 2P', monospace; font-size: .72rem; color: var(--amarelo); margin: 6px 4px 10px; }
[data-testid="stSidebar"] { display: none; }

html, body, [data-testid="stAppViewContainer"] * { font-family: 'VT323', monospace; }
[data-testid="stAppViewContainer"] p, [data-testid="stAppViewContainer"] li { font-size: 1.35rem; line-height: 1.25; color: var(--texto); }
a { color: var(--amarelo) !important; text-decoration: underline dotted; }

/* Título no estilo dos logos de console 64 bits */
.titulo { text-align: center; margin: .5rem 0 .2rem; }
.titulo h1 {
  font-family: 'Press Start 2P', monospace !important; font-size: 2.4rem; letter-spacing: 2px; margin: 0;
  color: var(--amarelo);
  text-shadow: 3px 3px 0 var(--vermelho), 6px 6px 0 var(--azul), 9px 9px 0 #000;
}
.titulo .sub { font-family: 'Press Start 2P', monospace; font-size: .62rem; color: var(--apagado); margin-top: 1rem; }
.pisca { font-family: 'Press Start 2P', monospace; color: var(--verde); font-size: .8rem; text-align: center;
         animation: pisca 1.1s steps(2, start) infinite; margin: .8rem 0 1.2rem; }
@keyframes pisca { to { visibility: hidden; } }

/* Painéis com borda pixelada */
.painel {
  background: var(--painel); border: 4px solid var(--borda);
  box-shadow: 0 0 0 4px #000, 6px 6px 0 4px #000; padding: 14px 16px; margin: 10px 4px 22px;
}
.painel h3 { font-family: 'Press Start 2P', monospace !important; font-size: .72rem; color: var(--amarelo); margin: 0 0 10px; }
.hud { display: grid; grid-template-columns: 1fr 1fr; gap: 4px 18px; font-size: 1.3rem; color: var(--texto); }
.hud b { color: var(--verde); font-weight: normal; }
.itens span { display: inline-block; border: 2px solid var(--azul); padding: 0 8px; margin: 3px; font-size: 1.15rem; color: var(--texto); background: #0e1140; }
.missao { border-left: 6px solid var(--vermelho); padding: 4px 10px; margin: 8px 0; background: #0e1140; }
.missao .nome { font-family: 'Press Start 2P', monospace; font-size: .62rem; color: var(--texto); }
.missao .desc { font-size: 1.2rem; color: var(--apagado); }
.missao .ok { color: var(--verde); font-family: 'Press Start 2P', monospace; font-size: .55rem; }

/* Botões do menu */
.stButton > button {
  font-family: 'Press Start 2P', monospace !important; font-size: .58rem !important; line-height: 1.6;
  background: var(--azul); color: #fff; border: 3px solid #fff; border-radius: 0;
  box-shadow: 4px 4px 0 #000; width: 100%; min-height: 3.2rem; transition: none;
}
.stButton > button:hover { background: var(--vermelho); color: #fff; border-color: var(--amarelo); }
.stButton > button:active { transform: translate(3px, 3px); box-shadow: 1px 1px 0 #000; }
.stButton > button p { font-family: 'Press Start 2P', monospace !important; font-size: .58rem !important; }

/* Mensagens como caixas de diálogo de RPG */
[data-testid="stChatMessage"] {
  background: var(--painel); border: 4px solid var(--borda); border-radius: 0;
  box-shadow: 0 0 0 4px #000, 5px 5px 0 4px #000; margin: 14px 4px; padding: 12px;
}
[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li { font-size: 1.4rem !important; }

/* Caixa de digitação */
[data-testid="stChatInput"] { border: 3px solid var(--amarelo) !important; border-radius: 0 !important; background: var(--painel) !important; }
[data-testid="stChatInput"] > div, [data-testid="stChatInput"] div { background: var(--painel) !important; border-radius: 0 !important; }
[data-testid="stChatInput"] textarea::placeholder { color: var(--apagado) !important; }
[data-testid="stChatInput"] textarea { font-family: 'VT323', monospace !important; font-size: 1.35rem !important; color: var(--texto) !important; }
[data-testid="stBottomBlockContainer"], [data-testid="stBottom"] > div { background: var(--bg) !important; }

.rodape { text-align: center; font-family: 'Press Start 2P', monospace; font-size: .5rem; color: var(--apagado); margin: 28px 0 8px; }
.aviso { font-family: 'Press Start 2P', monospace; font-size: .55rem; color: var(--amarelo); text-align: center; margin-bottom: 10px; }
</style>
"""

TELA_INICIAL = """
<div class="titulo">
  <h1>MARCOS.EXE</h1>
  <div class="sub">CURRÍCULO INTERATIVO · MOVIDO A IA</div>
</div>
<div class="pisca">▶ PRESS START: FAÇA UMA PERGUNTA</div>

<div class="painel">
  <h3>★ PLAYER 1</h3>
  <div class="hud">
    <div>NOME: <b>Marcos Vinicio</b></div>
    <div>CLASSE: <b>AI Builder</b></div>
    <div>ATUAL: <b>Supervisor · Mottu</b></div>
    <div>ALIADOS: <b>49 no time</b></div>
    <div>BASE: <b>Jandira-SP</b></div>
    <div>XP: <b>4+ anos em operação</b></div>
  </div>
</div>

<div class="painel">
  <h3>✚ INVENTÁRIO</h3>
  <div class="itens">
    <span>Agentes de IA</span><span>MCP</span><span>Tool calling</span><span>Text-to-SQL</span><span>Evals</span>
    <span>Python</span><span>FastAPI</span><span>SQL · BigQuery</span><span>Power BI</span><span>n8n</span>
    <span>Streamlit</span><span>Docker</span><span>Liderança</span>
  </div>
</div>

<div class="painel">
  <h3>⚑ MISSÕES CONCLUÍDAS</h3>
  <div class="missao">
    <div class="nome">FLEET AI ANALYST <span class="ok">✔ CLEAR</span></div>
    <div class="desc">Agente text-to-SQL com eval de 20 perguntas ·
      <a href="https://fleet-ai-analyst-marcos.streamlit.app" target="_blank">jogar demo</a> ·
      <a href="https://github.com/MarcosVVSantos/fleet-ai-analyst" target="_blank">código</a></div>
  </div>
  <div class="missao">
    <div class="nome">BARBERSHOP BOT <span class="ok">✔ CLEAR</span></div>
    <div class="desc">Agente de WhatsApp · 21 ferramentas MCP · 94 testes ·
      <a href="https://github.com/MarcosVVSantos/barbershop-bot" target="_blank">código</a></div>
  </div>
  <div class="missao">
    <div class="nome">CHAT-CURRÍCULO <span class="ok">✔ CLEAR</span></div>
    <div class="desc">Este jogo que você está jogando ·
      <a href="https://github.com/MarcosVVSantos/chat-portifolio" target="_blank">código</a></div>
  </div>
</div>
"""


def _segredo(nome: str, padrao: str = "") -> str:
    try:
        return st.secrets.get(nome, os.getenv(nome, padrao))
    except FileNotFoundError:
        return os.getenv(nome, padrao)


@st.cache_resource
def preparar():
    prompt = montar_prompt_sistema(carregar_perfil())
    chave = _segredo("LLM_API_KEY")
    if not chave:
        return prompt, None
    llm = cliente_openai(chave, _segredo("LLM_BASE_URL", "https://api.deepseek.com"), _segredo("LLM_MODEL", "deepseek-chat"))
    return prompt, llm


def responder(pergunta: str, prompt: str, llm) -> str:
    """Mostra a resposta chegando aos poucos e devolve o texto completo."""
    if llm is None:
        return st.write_stream(resposta_demo(pergunta))
    mensagens = montar_mensagens(prompt, st.session_state.historico, pergunta)
    try:
        return st.write_stream(llm(mensagens))
    except Exception as e:  # chave inválida, API fora do ar, limite de uso...
        texto = ("⚠ GLITCH NA MATRIX: não consegui falar com a IA agora "
                 f"({type(e).__name__}). Tente de novo em instantes ou fale direto com o Marcos: "
                 "marcos28.vinicio@gmail.com")
        st.markdown(texto)
        return texto


st.markdown(CSS, unsafe_allow_html=True)
prompt_sistema, llm = preparar()
st.session_state.setdefault("historico", [])
st.session_state.setdefault("usadas", 0)

st.markdown(TELA_INICIAL, unsafe_allow_html=True)
if llm is None:
    st.markdown('<div class="aviso">MODO DEMO: SÓ AS PERGUNTAS DO MENU FUNCIONAM</div>', unsafe_allow_html=True)

st.markdown('<div class="menu-titulo">☰ ESCOLHA UMA OPÇÃO OU DIGITE SUA PERGUNTA</div>', unsafe_allow_html=True)
clicada = None
colunas = st.columns(2)
for i, opcao in enumerate(RESPOSTAS_DEMO):
    if colunas[i % 2].button(f"▶ {opcao}", key=f"menu{i}", width="stretch"):
        clicada = opcao

for msg in st.session_state.historico:
    with st.chat_message(msg["role"], avatar="🕹️" if msg["role"] == "user" else "👾"):
        st.markdown(msg["content"])

pergunta = st.chat_input("Pergunte qualquer coisa sobre o Marcos...") or clicada
if pergunta:
    with st.chat_message("user", avatar="🕹️"):
        st.markdown(pergunta)
    with st.chat_message("assistant", avatar="👾"):
        bloqueio = validar_pergunta(pergunta, st.session_state.usadas)
        if bloqueio:
            st.markdown(bloqueio)
        else:
            resposta = responder(pergunta, prompt_sistema, llm)
            st.session_state.usadas += 1
            st.session_state.historico += [
                {"role": "user", "content": pergunta},
                {"role": "assistant", "content": resposta if isinstance(resposta, str) else str(resposta)},
            ]

st.markdown(
    f'<div class="rodape">PERGUNTAS: {st.session_state.usadas}/{MAX_PERGUNTAS_SESSAO} · '
    'FEITO POR MARCOS COM PYTHON + STREAMLIT + DEEPSEEK · INSERT COIN TO CONTINUE</div>',
    unsafe_allow_html=True,
)
