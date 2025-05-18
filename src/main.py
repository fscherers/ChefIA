import os
import pytz
import datetime
from dotenv import load_dotenv 

# Importa agentes
from src.agents import (
    agente_investigador,
    agente_buscador,
    agente_de_compra,
    agente_seletor,
    agente_revisor_culinario
)
# Importa as funções auxiliares
from src.utils import call_agent, to_markdown 

# --- Configuração da API Key ---
load_dotenv() # Carrega as variáveis do arquivo .env

os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

if os.environ["GOOGLE_API_KEY"] is None:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está configurada.")
    print("Certifique-se de ter um arquivo .env com GOOGLE_API_KEY=SUA_CHAVE ou que a variável esteja definida no sistema.")
    exit() # Sai do programa se a chave não for encontrada


# --- Fluxo Principal de Execução ---

# 1. Obtenção da Data e Hora Atual no Fuso Horário do Brasil
fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
# Obtém o horário UTC e depois converter para o fuso local
data_e_hora_atual_tz = datetime.datetime.now(pytz.utc).astimezone(fuso_horario_brasil)
# Formata a data e hora para passar para os agentes, incluindo nome e offset do fuso
data_e_hora_formatada_para_agente = data_e_hora_atual_tz.strftime("%A, %d de %B de %Y, %H:%M:%S %Z%z")

# 2. Iniciar a Interação com o Agente Investigador
agente_de_coleta = agente_investigador()
print(to_markdown(f"**E aí, mestre-cuca! 🧑‍🍳 Chega de sofrer pra decidir o rango, né?**\n\nEu sou o **ChefIA**, seu novo parceiro culinário inteligente, e tô aqui pra virar essa chave na sua cozinha! Bora transformar **o que você tem por aí** em pratos incríveis, sem estresse e com muito sabor?\n\nPra começar, qual a boa de hoje na sua despensa, geladeira, horta...?"))

informacoes_coletadas = "" # Variável para armazenar a resposta final do agente_investigador
historico_conversacao = []

while True:
    user_input = input("Você: ")
    historico_conversacao.append(f"Usuário: {user_input}")

    contexto_para_agente = "\n".join(historico_conversacao)
    agent_response = call_agent(agente_de_coleta, contexto_para_agente)
    historico_conversacao.append(f"Agente: {agent_response}")

    if agent_response.strip().startswith("FIM"):
        output_agente1 = agent_response.replace("FIM\n", "", 1).strip()
        print("\nInformações coletadas com sucesso!\n")
        print(to_markdown(output_agente1))
        break
    else:
        print(to_markdown(f"Agente: {agent_response}"))

print(to_markdown("\n**Trabalhando na sua solicitação. Aguarde, isso pode levar alguns instantes...**"))
# 3. Chamar o Agente Buscador de Receitas
#print("\n--- Próxima Etapa: Buscando Receitas ---")
receitas_sugeridas = agente_buscador(output_agente1)
#print(receitas_sugeridas)

# 4. Chamar o Agente Criador de Roteiros de Compra
#print("\n--- Próxima Etapa: Criando Roteiros de Compra ---")
roteiros_de_compra_finais = agente_de_compra(output_agente1, receitas_sugeridas)
#print(roteiros_de_compra_finais)

# 5. Chamar o Agente Seletor de Receita e Gerar Roteiro Final
#print("\n--- Próxima Etapa: Selecionando a Receita e Criando o Roteiro Final ---")

receita_e_roteiro_final = agente_seletor(
    informacoes_basicas_usuario=output_agente1,
    data_e_hora_atual=data_e_hora_formatada_para_agente,
    roteiros_de_compra_e_receitas=roteiros_de_compra_finais
)
# print(receita_e_roteiro_final) # Você pode comentar esta linha se quiser apenas a saída final do revisor

# 6. Chamar o Agente Revisor Culinário para Formatação Final
#print("\n--- Próxima Etapa: Preparando a Apresentação Final para Você! ---")
output_final_para_usuario = agente_revisor_culinario(receita_e_roteiro_final)
print(to_markdown(output_final_para_usuario))