print("-------Bem Vindo ao formulario de Usuario do Mobile Assit----------")
print("Primeiro vamos coletar algumas informações que serão utéis para o atendimento")
print("Esses dados são confidenciais e somente as equipes de socorristas terão acesso caso necessário")



perguntas = [
    "Possui alguma doença nos olhos? (óculos,astigmatismo,miupia etc)",
    "Possui alguma doença da audição , do ouvido,nariz ou da garganta ? surdez,aparelho auditivo,sinusite ou outros",
    "Alguma doença do cérebro ,do sistema nervoso ou doença psiquiatrica?",
    "Alguma doença no coração?(pressão alta,angia,arritimia,marca passo)",
    "Nasceu com alguma doença no coração ou realizou alguma cirurgia no coração?",
    "Alguma doença respiratória ou no pulmão ? (asma , bronquite ,tuberculose ou outros)",
    "Alguma doença nos rins ou bexiga ? (calculo renal,insuficiência renal)",
    "Alguma doença da mama , genital , ou sistema reprodutor feminino?",
    "Alguma doença do genital ou orgão reprodutor masculino?",
    "Alguma doença do sangue ,reumatismo,doença imunológica,do colágeno ou autoimune?",
    "Alguma doença nos intestinos ?(hepatites , hernia umbilical,gastrite ,cirrose ou outras?)",
    "Tem obesidade ou sobre peso, diabetes ,doença na tireóide ou outras?",
    "Alguma doença nos ossos ? (hérnias ,artrose , desvio de coluna,osteoporose ou outros)",
    "Algum tumor benigno , maligno ou câncer",
    "Alguma outra doença com necessidade de internação ?"
]



def fazerpergunta(pergunta):
    resposta = input(pergunta + " (sim/não): ")
    while resposta not in ["sim", "não"]:
        print("Por favor, responda com 'sim' ou 'não'.")
        resposta = input(pergunta + " (sim/não): ")
    return resposta

def fazerperguntas_list(list_perguntas):
    respostas = {}  

    for pergunta in list_perguntas:
        resposta = fazerpergunta(pergunta)
        respostas[pergunta] = resposta

    return respostas



respostas_usuario = fazerperguntas_list(perguntas)

def dados_extras():
    nome = input("Nome:")
    peso = input("Peso:")
    idade = input("Idade:")
    altura = input("Altura:")
    return nome,peso,idade,altura
    



print("------- Dados pessoais ---------")

nome,peso, idade, altura = dados_extras()

print(f"Nome: {nome}")
print(f"Peso: {peso}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")


print("\n------ Formulario de doenças preexistentes ---------")
for pergunta, resposta in respostas_usuario.items():
    print(f"{pergunta}: Resposta selecionada ---> {resposta}")









print(perguntas[0])


pergunta1 = perguntas[0]

resposta1 = input(f"{pergunta1} ------> sim/não")
if resposta1 == "sim":
    print()