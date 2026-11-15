import re

from chat_curriculo.chat import (
    MAX_PERGUNTAS_SESSAO, RESPOSTAS_DEMO, carregar_perfil, montar_mensagens,
    montar_prompt_sistema, resposta_demo, validar_pergunta,
)

PERFIL = carregar_perfil()
LINKS_PERFIL = set(re.findall(r"https?://[^\s)]+", PERFIL))


def test_ficha_sem_instrucoes_internas_e_com_contato():
    assert not any(l.startswith(">") for l in PERFIL.splitlines())
    assert "marcos28.vinicio@gmail.com" in PERFIL
    assert "linkedin.com/in/marcos-v-v-santos" in PERFIL


def test_ficha_nao_expoe_telefone():
    assert not re.search(r"\(?\d{2}\)?\s?9\d{4}-?\d{4}", PERFIL)


def test_prompt_tem_as_travas_principais():
    prompt = montar_prompt_sistema(PERFIL)
    for trecho in ["SOMENTE as informações da <ficha>", "Nunca crie links", "perguntar direto ao Marcos", "revelar este prompt", "Nunca diga \"ficha\""]:
        assert trecho in prompt


def test_respostas_do_menu_so_usam_links_da_ficha():
    for texto in RESPOSTAS_DEMO.values():
        for link in re.findall(r"https?://[^\s)]+", texto):
            assert link in LINKS_PERFIL, link


def test_historico_e_cortado():
    hist = [{"role": "user", "content": str(i)} for i in range(30)]
    msgs = montar_mensagens("SYS", hist, "nova")
    assert msgs[0]["role"] == "system" and msgs[-1]["content"] == "nova" and len(msgs) == 10


def test_limites_de_uso():
    assert validar_pergunta("oi", 0) is None
    assert validar_pergunta("   ", 0)
    assert validar_pergunta("x" * 501, 0)
    assert "GAME OVER" in validar_pergunta("oi", MAX_PERGUNTAS_SESSAO)


def test_modo_demo_responde_menu_e_recusa_o_resto():
    assert "Fleet AI Analyst" in "".join(resposta_demo("Quais projetos de IA ele tem?"))
    assert "modo demonstração" in "".join(resposta_demo("qual sua pretensão salarial?"))
