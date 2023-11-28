

print("-------Bem vindo ao Mobile Assist primeiros socorros------")
print("!!!IMPORTANTE !!!")
print("Responda as perguntas a seguir com sim/não e siga as instruções até a emergência chegar")

print("Se possivel cheque os sinais vitais do paciente e siga com as perguntas")


     


perguntas = [
    
    "O paciente está conciente ?",
    "O paciente está repirando?",
    "O paciente tem batimento cardiaco?",
    "O paciente está sangrando?",
    "O paciente possui alguma fratura visível?",
    "O paciente bateu a cabeça?",
    "O paciente está com alguma queimadura visível?",
    "O paciente está se engasgando?",
    "O paciente se afogou?"
    
    
]

i = 0

respostas= []
""""
Laço while que faz a verificação das respostas do usuário e inclui a resposta na lista respostas

"""
while i < len(perguntas):
    resposta = input(f"{perguntas[i]} ------> sim/não :").lower()
    
    while resposta not in ['sim', 'não']:
        print("Por favor, responda apenas com 'sim' ou 'não'.")
        resposta = input(f"{perguntas[i]} ------> sim/não :").lower()

    i += 1
    respostas.append(resposta)

"""
Verificação para cada resposta com cada e caso necessário a
instrução realicionada a pergunta é digitada
"""
     
if respostas[0] == 'sim':
    print("""
          Mantenha o paciente aquecido , pergunte se está tudo bem e se sente alguma dor e espere a emergência chegar a local
          """)
else:
    print("""
          "--------- PACIENTE ESTÁ INCONSCIENTE ------------\n"
          Aguarde os primeiros socorros e siga as instruções seguintes : 
          """)

if respostas[1] == 'sim':
    print("Não mova o corpo do paciente e mantenha a cabeça do mesmo imóvel")
else:
     print("--------- PACIENTE NÃO RESPIRA ------------.\n"
     "Para realizar o movimento de ventilação em uma pessoa sem respiração durante a RCP, siga estas etapas:\n"
      "Após iniciar as compressões torácicas, abra as vias respiratórias da vítima inclinando a cabeça para trás.\n"
      "Se for seguro fazê-lo, tampe o nariz da vítima com os dedos que não estão na testa.\n"
      "Faça uma vedação hermética sobre a boca da vítima com sua boca.\n"
      "Dê uma ventilação, soprando ar suficiente para fazer o peito da vítima subir visivelmente.\n"
      "Permita que o peito da vítima caia antes de iniciar a próxima compressão torácica.\n"
      "Se treinado em RCP com ventilações, continue alternando entre compressões e ventilações.\n"
      "\nLembre-se de manter um ritmo consistente durante as compressões e ventilações até a chegada de ajuda profissional.")



if respostas[2] =='sim':
    print("Aguarde os primeiros socorros e siga as instruções seguintes : ")
else:
       print("--------- PACIENTE NÃO POSSUI BATIMENTO CARDÍACO ------------\n"
       "Se você se deparar com alguém que não tem pulso, a massagem cardíaca é essencial. Siga estes passos:\n"
      "Verifique a cena para segurança, chame ajuda profissional e tente acordar a vítima.\n"
      "Se a vítima não estiver respirando normalmente, posicione suas mãos no centro do peito e comprima para baixo 5-6 cm a uma frequência de 100-120 compressões por minuto.\n"
      "Continue as compressões sem interrupções até a chegada da ajuda profissional ou sinais de recuperação.\n"
      "Se treinado em RCP com ventilações, pode alternar compressões com ventilações.\n"
      "Lembre-se de que a consistência é crucial para manter o fluxo sanguíneo até que a ajuda profissional chegue.")


if respostas[3] == "sim":
    print("--------- PACIENTE ESTÁ SANGRANDO ------------\n"
      "Se você se deparar com um sangramento, siga estas instruções:\n"
      " Use um Paninho Limpo: Se possível, peça à vítima para pressionar um pano limpo, gaze ou curativo sobre a ferida.\n"
      " Eleve a Parte Lesionada: Se a ferida estiver em um braço ou perna, ajude a vítima a elevar a parte do corpo afetada.\n"
      " Aplique Pressão Direta: Aplique pressão direta sobre a ferida com as mãos ou usando o pano limpo.\n"
      " Seque o Sangue: Se o pano ficar saturado, adicione mais panos, mas evite retirar o pano original, pois isso pode perturbar o processo de coagulação.\n"
      " Chame Ajuda Profissional: Ligue para o serviço de emergência (SAMU ou equivalente) para obter ajuda profissional.\n"
      " Continue Aplicando Pressão: Continue aplicando pressão até que a ajuda profissional chegue ou até que o sangramento pare.\n"
      )         
else :
    print("Ótimo , mantenha a calma , espere pela emergência e siga as próximas intruções se necessário")

if respostas[4] == "sim":
 print("--------- PACIENTE ESTÁ COM MEMBRO FRATURADO ------------\n" 
       "Em caso de um membro quebrado ou fraturado, é essencial seguir as seguintes instruções de primeiros socorros:\n"
      "Mantenha a calma e tranquilize a vítima.\n"
      "Imobilize o membro ferido para evitar movimentos que possam causar mais danos.\n"
      "Se possível, aplique uma compressa fria na área para reduzir o inchaço.\n"
      "Chame ajuda profissional imediatamente ou peça a alguém para fazer isso.\n"
      "Evite movimentar a vítima, a menos que seja absolutamente necessário.\n"
      "Caso seja necessário mover a vítima, faça-o com extremo cuidado e mantenha o membro imobilizado.\n"
      "Observe sinais de choque, como palidez, respiração rápida ou pulso fraco, e tome medidas apropriadas.\n"
      "Forneça conforto e suporte emocional à vítima enquanto aguarda a chegada da ajuda profissional.")
else:
     print("Ótimo , mantenha a calma , espere pela emergência e siga as próximas intruções se necessário")

if respostas[5] == "sim":
         print("""
               --------- PACIENTE BATEU A CABEÇA ------------
       Em caso de lesão na cabeça, mantenha a calma e avalie a cena para garantir segurança.
       Verifique a consciência da vítima chamando seu nome e pedindo para abrir os olhos.
       Se consciente, oriente a vítima a permanecer imóvel, evitando movimentos na cabeça.
       Se houver suspeita de lesão na coluna cervical, evite mexer na cabeça e pescoço.
       Chame ajuda profissional imediatamente ou peça a alguém para fazer isso.
       Se a vítima estiver inconsciente, mas respirando normalmente, coloque-a em posição lateral de segurança para evitar aspiração.
       Se não estiver respirando, inicie a RCP conforme treinamento adequado.
       Mantenha a vítima aquecida com cobertores, se necessário, enquanto aguarda a chegada da ajuda profissional.
       Observe sinais de choque, como palidez, respiração rápida ou pulso fraco, e tome medidas apropriadas.
       Lembre-se de procurar ajuda médica imediata para avaliação e tratamento adequados em casos de lesões na cabeça.
       """)
else:
          print("Ótimo , mantenha a calma , espere pela emergência e siga as próximas intruções se necessário")

if respostas[6]:
     print("""
           "--------- PACIENTE ESTÁ COM QUEIMADURAS ------------"
     Em situações de queimaduras, é essencial agir com rapidez e precisão. Primeiramente, pare a fonte de calor para interromper a exposição à queimadura. 
     Em seguida, resfrie a área afetada sob água corrente fria por pelo menos 10 minutos, evitando o uso de água muito fria ou gelo. 
     Ao remover roupas e joias ao redor da queimadura, faça isso com cuidado, sem forçar a remoção se estiver grudada na pele.
     Proteja a queimadura com um pano limpo e seco ou um curativo estéril, evitando o uso direto de algodão na ferida. 
     Não aplique produtos como pomadas, manteiga ou pasta de dentes, pois isso pode aumentar o risco de infecção. 
     Em casos de queimaduras extensas, profundas ou que afetem áreas sensíveis como rosto, mãos, pés, genitais ou articulações,
     é crucial procurar ajuda médica imediatamente.
     Alivie a dor, se necessário, oferecendo analgésicos de venda livre conforme as instruções da embalagem. 
     Observe atentamente a vítima quanto a sinais de choque, como palidez, sudorese intensa, confusão mental ou respiração rápida.
     """)
else:
     print("Ótimo , mantenha a calma , espere pela emergência e siga as próximas intruções se necessário")

if respostas[7] == "sim":
           print("""
                 "--------- PACIENTE ESTÁ ENGASGANDO ------------"
           Como agir em caso de engasgo por corpo estranho: Manobra de Heimlich
           Posicione-se por trás e enlace a vítima com os braços ao redor do abdome (se for uma criança, ajoelhe-se primeiro), caso ela esteja consciente. 
           Uma das mãos permanece fechada sobre a chamada “boca do estômago” (região epigástrica). 
           A outra mão comprime a primeira, ao mesmo tempo em que empurra a “boca do estômago” para dentro e para cima,
           como se quisesse levantar a vítima do chão. 
           Faça movimentos de compressão para dentro e para cima (como uma letra “J”), até que a vítima elimine o corpo estranho
           """)

     
else:
      print("Ótimo , mantenha a calma , espere pela emergência e siga as próximas intruções se necessário")

if respostas[8] == "sim":
      print("""
            "--------- PACIENTE ESTÁ AFOGADO ------------"
      O primeiro passo deve ser verificar se a vítima está respirando observando se o tórax infla ou não. 
      Caso ela esteja respirando é necessário colocá-la de lado para que ela não sufoque se começar a vomitar.
      Caso seja necessário realizar a respiração boca a boca, o socorrista deve inclinar a cabeça da vítima para trás e levantar o queixo. 
      Aperte o nariz dela com o polegar e o indicador e com a outra mão abra a boca da vítima.
      Inspire normalmente e cubra a boca da pessoa com a sua, soprando o ar lenta e regularmente até que o peito infle. 
      Cada insuflação deve durar aproximadamente um segundo até que a vítima reaja.
    """)
else:
     print("Ótimo , mantenha a calma e espere pela emergência ")
     

      
     

print("-------Relatório final--------")

def imprimir_perguntas_respostas(perguntas, respostas):
    """
    Função que imprimime as perguntas e as respostas feitas pelo usuário
    Args:perguntas , respostas
        
    Returns:impressão das perguntas e as respostas dos usuários
    
    """
    for pergunta, resposta in zip(perguntas, respostas):
        print(f"Pergunta feita ----> {pergunta} /// Resposta ----> {resposta}")

imprimir_perguntas_respostas(perguntas, respostas)

help(imprimir_perguntas_respostas)          





        
        
    




