# Gerador de Resumo de Texto com Azure AI
Gerador de Resumo de Texto com Azure AI

Este projeto é uma aplicação web simples que utiliza o Azure AI Services para extrair palavras-chave de um texto, permitindo que os usuários obtenham um resumo dos principais tópicos abordados.

Funcionalidades
Extração de Palavras-Chave: Utiliza o serviço de Análise de Texto do Azure para identificar as principais palavras-chave no texto inserido.
Limite de Palavras: O campo de entrada possui uma verificação para textos com até 5120 palavras, exibindo uma mensagem de advertência caso o limite seja excedido.
Interface Simples: Uma página HTML permite que o usuário cole o texto, clique em "Gerar Resumo" e visualize o resumo automaticamente na mesma página.

Pré-requisitos
Conta no Azure: Necessário para configurar o Azure AI Services.
Chave de API e Endpoint do serviço de Análise de Texto do Azure.
Python 3.x: Recomenda-se Python 3.7 ou superior.

Tecnologias Utilizadas
Python com Flask para o backend
JavaScript para a interação com o backend
HTML/CSS para a interface simples do usuário
Azure AI Services para a extração de palavras-chave


Memória atualizada
Ótima ideia! Vou ajudá-la a criar um arquivo README.md para explicar o projeto.

Aqui está uma estrutura básica que você pode usar:

Gerador de Resumo de Texto com Azure AI
Este projeto é uma aplicação web simples que utiliza o Azure AI Services para extrair palavras-chave de um texto, permitindo que os usuários obtenham um resumo dos principais tópicos abordados.

Funcionalidades
Extração de Palavras-Chave: Utiliza o serviço de Análise de Texto do Azure para identificar as principais palavras-chave no texto inserido.
Limite de Palavras: O campo de entrada possui uma verificação para textos com até 5120 palavras, exibindo uma mensagem de advertência caso o limite seja excedido.
Interface Simples: Uma página HTML permite que o usuário cole o texto, clique em "Gerar Resumo" e visualize o resumo automaticamente na mesma página.
Pré-requisitos
Conta no Azure: Necessário para configurar o Azure AI Services.
Chave de API e Endpoint do serviço de Análise de Texto do Azure.
Python 3.x: Recomenda-se Python 3.7 ou superior.
Tecnologias Utilizadas
Python com Flask para o backend
JavaScript para a interação com o backend
HTML/CSS para a interface simples do usuário
Azure AI Services para a extração de palavras-chave
Como Configurar o Projeto
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

Instale as dependências:

No terminal, execute:

bash
Copiar código
pip install -r requirements.txt
Configure o Azure AI:

Crie um recurso de Análise de Texto no portal Azure.
Obtenha o endpoint e a key.
Insira essas informações no arquivo app.py nas variáveis endpoint e key.
Execute a Aplicação:

No terminal, execute o seguinte comando para iniciar o servidor Flask:

bash
Copiar código
python app.py
Acesse a Aplicação:

Abra o navegador e vá para http://127.0.0.1:5000.

Uso
Cole o texto no campo "Cole seu texto aqui".
Clique no botão "Gerar Resumo".
O resumo gerado aparecerá na seção "Resumo".


Memória atualizada
Ótima ideia! Vou ajudá-la a criar um arquivo README.md para explicar o projeto.

Aqui está uma estrutura básica que você pode usar:

Gerador de Resumo de Texto com Azure AI
Este projeto é uma aplicação web simples que utiliza o Azure AI Services para extrair palavras-chave de um texto, permitindo que os usuários obtenham um resumo dos principais tópicos abordados.

Funcionalidades
Extração de Palavras-Chave: Utiliza o serviço de Análise de Texto do Azure para identificar as principais palavras-chave no texto inserido.

Limite de Palavras: O campo de entrada possui uma verificação para textos com até 5120 palavras, exibindo uma mensagem de advertência caso o limite seja excedido.

Interface Simples: Uma página HTML permite que o usuário cole o texto, clique em "Gerar Resumo" e visualize o resumo automaticamente na mesma página.

Pré-requisitos

Conta no Azure: Necessário para configurar o Azure AI Services.
obter a Chave de API e Endpoint do serviço de Análise de Texto do Azure.
( as chaves que constam neste projeto estão desativadas , so deixei como exemplo)

Python 3.x: Recomenda-se Python 3.7 ou superior.
Tecnologias Utilizadas
Python com Flask para o backend
JavaScript para a interação com o backend
HTML/CSS para a interface simples do usuário
Azure AI Services para a extração de palavras-chave
Como Configurar o Projeto
Clone o repositório:


git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Instale as dependências:

No terminal, execute:


pip install -r requirements.txt
Configure o Azure AI:

Crie um recurso de Análise de Texto no portal Azure.
Obtenha o endpoint e a key.
Insira essas informações no arquivo app.py nas variáveis endpoint e key.
Execute a Aplicação:

No terminal, execute o seguinte comando para iniciar o servidor Flask:

bash
Copiar código
python app.py
Acesse a Aplicação:

Abra o navegador e vá para http://127.0.0.1:5000.

Uso
Cole o texto no campo "Cole seu texto aqui".
Clique no botão "Gerar Resumo".
O resumo gerado aparecerá na seção "Resumo".


Estrutura de Arquivos



nome-do-repositorio/
├── app.py                   # Código principal da aplicação Flask
├── templates/
│   └── index.html           # Página HTML com a interface do usuário
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo de documentação
