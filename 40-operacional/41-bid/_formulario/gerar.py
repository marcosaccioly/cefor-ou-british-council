#!/usr/bin/env python3
"""Gera formulario-preenchido.md a partir de respostas.md e compara com o OU2.

Uso:  python gerar.py
Saída: formulario-preenchido.md (mesma pasta) + relatório no terminal.

- Valida limites de palavras por campo.
- Conta marcadores TBD pendentes.
- Campos `status: usar-ou2` importam a resposta diretamente do formulário OU2.
- Campos com âncora `ou2:` são comparados com o que está no OU2
  (igual / DIFERENTE / vazio no OU2 / âncora não encontrada).
"""
import glob
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RESPOSTAS = os.path.join(BASE, "respostas.md")
SAIDA = os.path.join(BASE, "formulario-preenchido.md")
OU2_GLOB = os.path.join(BASE, "..", "_versao-ou", "*OU2.md")

ICONES = {"pronto": "✅", "rascunho": "🟨", "usar-ou2": "📥", "vazio": "🔴"}


def parse_respostas(path):
    campos = []
    atual = None
    em_meta = False
    for ln in open(path, encoding="utf-8").read().splitlines():
        m = re.match(r"^## +(\S+) +\| +(.+)$", ln)
        if m:
            atual = {"id": m.group(1), "pergunta": m.group(2).strip(),
                     "meta": {}, "corpo": []}
            campos.append(atual)
            em_meta = True
            continue
        if atual is None:
            continue
        if em_meta:
            mm = re.match(r"^- ([a-z0-9_]+):\s*(.*)$", ln)
            if mm:
                atual["meta"][mm.group(1)] = mm.group(2).strip()
                continue
            em_meta = False  # primeira linha não-metadado encerra o bloco
        atual["corpo"].append(ln)
    for c in campos:
        c["resposta"] = "\n".join(c["corpo"]).strip()
    return campos


def conta_palavras(texto):
    limpo = re.sub(r"[*_`>#]", " ", texto)
    return len(re.findall(r"\S+", limpo))


def carrega_ou2():
    achados = glob.glob(OU2_GLOB)
    if not achados:
        return None
    return open(achados[0], encoding="utf-8").read().splitlines()


def resposta_ou2(linhas, ancora):
    """Extrai, da linha-tabela do OU2 que contém a âncora, o texto da resposta
    (conteúdo da 1ª célula após o primeiro <br> que segue a âncora)."""
    for ln in linhas:
        if ancora in ln and ln.lstrip().startswith("|"):
            celulas = ln.split("|")
            celula1 = celulas[1] if len(celulas) > 2 else ln
            resto = celula1[celula1.find(ancora) + len(ancora):]
            br = resto.find("<br>")
            if br < 0:
                return ""  # campo existe mas sem resposta
            texto = resto[br:].replace("<br>", "\n")
            return "\n".join(t.strip() for t in texto.splitlines()).strip()
    return None  # âncora não encontrada


def normaliza(texto):
    return re.sub(r"\W+", " ", texto.lower()).strip()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    campos = parse_respostas(RESPOSTAS)
    ou2 = carrega_ou2()
    if ou2 is None:
        print("AVISO: formulário OU2 não encontrado em _versao-ou/ — comparação desativada.")

    saida = ["# Formulário recriado — gerado de `respostas.md`", "",
             "> NÃO EDITAR AQUI: este arquivo é gerado por `gerar.py`. "
             "Edite `respostas.md` e regenere.", ""]
    problemas, tbds, comparacoes = [], [], []
    contagem_status = {}
    secao_atual = None

    for c in campos:
        meta = c["meta"]
        status = meta.get("status", "vazio")
        limite = int(meta.get("limite", "0") or 0)
        ancora = meta.get("ou2", "")
        contagem_status[status] = contagem_status.get(status, 0) + 1

        if meta.get("secao") != secao_atual:
            secao_atual = meta.get("secao")
            saida += [f"## {secao_atual}", ""]

        resposta = c["resposta"]
        origem = ""
        if status == "usar-ou2" and ou2 is not None and ancora:
            ext = resposta_ou2(ou2, ancora)
            if ext:
                resposta, origem = ext, " *(importado do OU2)*"
            elif ext == "":
                problemas.append(f"{c['id']}: status usar-ou2 mas campo VAZIO no OU2")
            else:
                problemas.append(f"{c['id']}: status usar-ou2 mas âncora não encontrada no OU2")

        saida.append(f"### {c['pergunta']}" + (f" *(≤ {limite} palavras)*" if limite else ""))
        saida.append(f"**Status:** {ICONES.get(status, '?')} {status}{origem}")

        if resposta:
            n = conta_palavras(resposta)
            if limite:
                ok = "✅" if n <= limite else "⚠️ **EXCEDE**"
                saida.append(f"**Contagem:** {n}/{limite} {ok}")
                if n > limite:
                    problemas.append(f"{c['id']}: {n} palavras (limite {limite})")
            n_tbd = len(re.findall(r"\bTBD\b", resposta))
            if n_tbd:
                tbds.append(f"{c['id']}: {n_tbd} TBD")
            saida.append("")
            saida += ["> " + l for l in resposta.splitlines()]
        else:
            saida += ["", "> — *(vazio)*"]
            if meta.get("nota"):
                saida.append(f"> 📌 {meta['nota']}")

        # comparação com o OU2 (para campos próprios, não usar-ou2)
        if ou2 is not None and ancora and status != "usar-ou2":
            la = resposta_ou2(ou2, ancora)
            if la is None:
                cmp_txt = "âncora não encontrada no OU2"
            elif la == "":
                cmp_txt = "campo **vazio no OU2**" + (" — nossa resposta é nova" if resposta else "")
            elif resposta and normaliza(la) == normaliza(resposta):
                cmp_txt = "✅ **igual** ao OU2"
            elif resposta:
                cmp_txt = "⚠️ **DIFERENTE** do OU2 — substituir lá pela nossa versão"
            else:
                cmp_txt = "OU2 tem resposta; nós não — avaliar se adotamos"
            saida += ["", f"**Comparação OU2:** {cmp_txt}"]
            comparacoes.append(f"{c['id']}: {cmp_txt}")
        saida.append("")

    # resumo
    saida += ["---", "", "## Resumo da geração", ""]
    saida.append("| Status | Campos |")
    saida.append("|---|---|")
    for st in ("pronto", "rascunho", "usar-ou2", "vazio"):
        if st in contagem_status:
            saida.append(f"| {ICONES[st]} {st} | {contagem_status[st]} |")
    if problemas:
        saida += ["", "**⚠️ Problemas:**"] + [f"- {p}" for p in problemas]
    if tbds:
        saida += ["", "**TBDs pendentes:**"] + [f"- {t}" for t in tbds]

    open(SAIDA, "w", encoding="utf-8", newline="\n").write("\n".join(saida) + "\n")

    print(f"Gerado: {os.path.relpath(SAIDA, BASE)}  ({len(campos)} campos)")
    print("Status:", ", ".join(f"{k}={v}" for k, v in sorted(contagem_status.items())))
    for p in problemas:
        print("PROBLEMA:", p)
    for t in tbds:
        print("TBD:", t)
    for cp in comparacoes:
        print("OU2:", cp)


if __name__ == "__main__":
    main()
