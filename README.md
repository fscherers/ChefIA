# 🧑‍🍳 ChefIA - Seu Assistente Culinário Inteligente

---

## Introdução

Em um mundo onde o ritmo de vida é cada vez mais acelerado, planejar refeições deliciosas e eficientes pode ser um desafio. O projeto **ChefIA** surge para revolucionar a sua cozinha, atuando como um assistente de IA multi-agente projetado para otimizar todo o processo culinário, desde a análise dos ingredientes que você já tem em casa até a sugestão de roteiros de compra e o passo a passo do preparo.

Utilizando o poder da **Google Agent Development Kit (ADK)** e o modelo **Gemini** da Google, o ChefIA orquestra múltiplos agentes inteligentes que trabalham em conjunto para oferecer uma experiência personalizada e sem estresse, garantindo que você aproveite ao máximo seu tempo e seus recursos.

**Experimente o ChefIA e descubra como a inteligência artificial pode transformar sua experiência na cozinha!**

---

## Visão Geral e Funcionalidades Chave

O ChefIA é construído com um sistema multi-agente robusto, onde cada agente possui uma especialidade e contribui para um plano culinário completo e adaptado às suas necessidades. Conheça as funcionalidades que fazem do ChefIA seu melhor amigo na cozinha:

### 1. 🔍 Agente Investigador de Preferências

* **O que faz:** Inicia a conversa de forma amigável, coletando informações essenciais como os **ingredientes disponíveis** em sua casa, sua **disposição para comprar** (e orçamento/endereço, se sim), o **tempo disponível** para o preparo e o **momento desejado** para a refeição.
* **Utilidade no Dia a Dia:** Garante que todas as sugestões de receita e planos sejam perfeitamente alinhadas com suas condições e preferências atuais, evitando surpresas e desperdícios.

### 2. 🍲 Agente Buscador de Receitas

* **O que faz:** Com base nas informações coletadas, este agente pesquisa e seleciona **cinco receitas** que melhor aproveitam seus ingredientes e se encaixam no seu tempo e disposição para compras. Ele é criativo e pode sugerir pratos surpreendentes!
* **Utilidade no Dia a Dia:** Acaba com o "e agora, o que eu faço com isso?" e te apresenta um leque de opções viáveis, pensando na sua despensa.

### 3. 🛒 Agente Criador de Roteiros de Compra

* **O que faz:** Se a receita escolhida exigir ingredientes extras, este agente inteligente cria um **roteiro de compras**. Ele pesquisa supermercados próximos (com base no seu endereço), estima tempos de deslocamento (a pé, de carro, de bicicleta) e até o custo aproximado dos itens.
* **Utilidade no Dia a Dia:** Poupa seu tempo e dinheiro, oferecendo a logística de compras de forma eficiente e otimizada, ou indicando quando nenhuma compra é necessária.

### 4. ✅ Agente Seletor de Receita

* **O que faz:** Avalia a viabilidade de todas as receitas sugeridas, considerando ingredientes, orçamento, tempo total (preparo + compra), e até mesmo os horários de funcionamento de lojas. Ele, então, seleciona a **melhor receita** para você e gera um **roteiro de execução detalhado**, do momento atual até o prato pronto.
* **Utilidade no Dia a Dia:** Tira o peso da decisão das suas costas, garantindo que o plano é realista e se encaixa perfeitamente na sua agenda.

### 5. 📚 Agente Revisor Culinário

* **O que faz:** Pega todo o plano gerado (receita, roteiro de compra, passo a passo de preparo) e o formata de uma maneira **clara, bonita e fácil de seguir**. Ele garante que você receba todas as informações organizadas para uma experiência culinária prazerosa.
* **Utilidade no Dia a Dia:** Apresenta o resultado final de forma impecável, permitindo que você siga o plano sem confusão.

---

## Estrutura do Projeto

chefia_project/

├── .env                # Variáveis de ambiente (sua API Key vai aqui)

├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git

├── README.md           # Este arquivo

├── requirements.txt    # Dependências do Python

└── src/

    ├── init.py         # Torna 'src' um pacote Python

    ├── main.py         # O fluxo principal de execução do ChefIA

    ├── agents.py       # Definições dos agentes inteligentes

    └── utils.py        # Funções auxiliares (chamar agente, formatação de texto)


## Como Rodar


### 1. Pré-requisitos


* Python 3.8+

* Git

* Uma API Key do Google Gemini (você pode obtê-la no [Google AI Studio](https://aistudio.google.com/))

* Uma API Key do Google Search (para as ferramentas de busca).


### 2. Configuração do Ambiente


1.  **Clone o repositório:**



2.  **Crie e ative um ambiente virtual (recomendado):**



3.  **Instale as dependências:**



4.  **Configure sua API Key:**

    Crie um arquivo chamado `.env` na raiz do projeto (`chefia_project/`) e adicione sua chave de API:

    ```

    GOOGLE_API_KEY=SUA_CHAVE_DE_API_AQUI

    ```

    **ATENÇÃO:** Nunca publique este arquivo `.env` 


### 3. Executando o ChefIA

python src/main.py


**Potencial e Futuro**

O ChefIA é mais do que um script; é uma prova do poder da IA multi-agente na resolução de problemas cotidianos. Seu potencial de expansão é vasto, podendo incluir funcionalidades como:

    Integração com calendários para agendamento de refeições.
    Suporte a mais idiomas e adaptação cultural de receitas.
    Conexão com APIs de supermercados para verificar disponibilidade de estoque e preços em tempo real.
    Personalização de dietas e restrições alimentares avançadas.

Estamos apenas começando a desvendar o que o ChefIA pode fazer!
Contato

Autor: Felipe Scherer da Silva

GitHub: https://github.com/fscherers

LinkedIn: https://www.linkedin.com/in/felipe-scherer/

© 2024 Projeto ChefIA. Desenvolvido para simplificar sua vida na cozinha.
