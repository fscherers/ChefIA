import os
import textwrap
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent, message_text: str) -> str: # Removido ": Agent" para simplificar a importação neste arquivo
    """
    Envia uma mensagem a um agente e retorna sua resposta final.
    Cria uma nova sessão para cada chamada, não mantendo histórico entre chamadas
    diferentes.
    """
    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response += part.text
                    final_response += "\n"
    return final_response

# Função auxiliar para exibir texto formatado em Markdown no terminal
def to_markdown(text):
    text = text.replace('•', '  *') # Ajuste para renderização Markdown mais consistente
    # Remove formatação Markdown para uma saída de texto mais limpa no terminal
    text = text.replace('**', '')
    text = text.replace('###', '')
    text = text.replace('##', '')
    return textwrap.indent(text, '', predicate=lambda _: True) # Remove indentação extra se houver