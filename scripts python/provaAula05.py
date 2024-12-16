aluno = []

while True:
    try:
        quantidade_de_alunos = int(input("quantidade de alunos avaliados: "))
        if quantidade_de_alunos > 0:
            break
        else:
            print("por favor, insira um número maior que zero")
    except ValueError:
        print("favor digite um número inteiro")

for quantidade in range(quantidade_de_alunos):
    nome = input(f"digite o nome do aluno {quantidade + 1}: ")

    notas = []
    for numero in range(3):
        while True:
            try:
                nota = float(input(f"digite a nota {numero + 1} de {nome}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("favor digitar uma nota de 0 a 10")
            except ValueError:
                print("entrada inválida, favor digite um novo número")

    if len(notas) == 3:  # Certifique-se de que todas as 3 notas foram inseridas
        media = sum(notas) / len(notas)
        status = "aprovado" if media >= 7 else "reprovado"
        aluno.append({'nome': nome, 'notas': notas, 'media': media, 'status': status})
    else:
        print(f"Erro: o aluno {nome} não possui todas as notas válidas.")

print("\nresultado dos alunos:")
for alunos in aluno:
    print(f"Aluno: {alunos['nome']}\nNotas: {', '.join(map(str, alunos['notas']))}\nMédia: {alunos['media']:.2f}\nStatus: {alunos['status']}\n")

# Verifique se a lista de alunos não está vazia para evitar erro na média geral
if len(aluno) > 0:
    media_geral = sum(alunos['media'] for alunos in aluno) / len(aluno)
    print(f"Média geral da turma: {media_geral:.2f}")
else:
    print("Não há alunos para calcular a média geral.")
