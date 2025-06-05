import json

with open("Turmas.json", "r", encoding="utf-8") as f:
    turmas = json.load(f)
with open("Salas.json", "r", encoding="utf-8") as f:
    salas = json.load(f)


############################################
ensalamento = []
# Verifica horariod da aula e sala
def horario_dentro(horario_aula, horario_sala):
    return (
        horario_aula["dia"].lower() == horario_sala["dia"].lower() and
        horario_aula["inicio"] >= horario_sala["inicio"] and
        horario_aula["fim"] <= horario_sala["fim"]
    )
# Verifica se a sala está ocupada
def tem_conflito(aula, ocupacoes):
    for ocupacao in ocupacoes:
        if ocupacao["dia"].lower() == aula["dia"].lower():
            # Verifica se os horários se sobrepõem
            if not (aula["fim"] <= ocupacao["inicio"] or aula["inicio"] >= ocupacao["fim"]):
                return True
    return False


for turma in turmas:
    for aula in turma["aulas"]:
        alocada = False
        for sala in salas:
            if turma["quantidade_alunos"] > sala["capacidade"]:
                continue
            if aula["tipo_sala"].lower() != sala["tipo"].lower():
                continue
            for disponibilidade in sala["disponibilidade"]:
                if horario_dentro(aula, disponibilidade):
                    if tem_conflito(aula, sala["ocupacoes"]):
                        continue
                    sala["ocupacoes"].append({
                        "turma": turma["turma"],
                        "dia": aula["dia"],
                        "inicio": aula["inicio"],
                        "fim": aula["fim"],
                    })
                    alocada = True
                    ensalamento.append({
                        "turma": turma["turma"],
                        "sala": sala["sala"],
                        "predio": sala["predio"],
                        "dia": aula["dia"],
                        "inicio": aula["inicio"],
                        "fim": aula["fim"],
                    })
                    break
            if alocada:
                break

with open("ensalamento.json", "w", encoding="utf-8") as f:
    json.dump(ensalamento, f, indent=2, ensure_ascii=False)

print("Alocação concluida.")