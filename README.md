# Gerador de Resumo de Texto com Azure AI
Gerador de Resumo de Texto com Azure AI

Este projeto é uma aplicação web simples que utiliza o Azure AI Services para extrair palavras-chave de um texto, permitindo que os usuários obtenham um resumo dos principais tópicos abordados.

# Funcionalidades
Extração de Palavras-Chave: Utiliza o serviço de Análise de Texto do Azure para identificar as principais palavras-chave no texto inserido.
Limite de Palavras: O campo de entrada possui uma verificação para textos com até 5120 palavras, exibindo uma mensagem de advertência caso o limite seja excedido.
Interface Simples: Uma página HTML permite que o usuário cole o texto, clique em "Gerar Resumo" e visualize o resumo automaticamente na mesma página.

# Pré-requisitos
Conta no Azure: Necessário para configurar o Azure AI Services.

Chave de API e Endpoint do serviço de Análise de Texto do Azure. 
( As chaves que se encontram no projeto e so para efeito de teste , ja foram trocadas não vai funcionar ) 

Python 3.x: Recomenda-se Python 3.7 ou superior.

# Tecnologias Utilizadas
Python com Flask para o backend
JavaScript para a interação com o backend
HTML/CSS para a interface simples do usuário
Azure AI Services para a extração de palavras-chave



Estrutura de Arquivos


nome do repositorio ( ou diretorio) 
├── app.py                   
├── templates
  └── index.html           
├── requirements.txt    
└── README.md 

# Siga o passo a passo
faça o clone do projeto no seu computador : git clone https://github.com/seu-usuario/nome-do-repositorio.git

cd nome-do-repositorio

Instale as dependências:pip install -r requirements.txt

crie uma conta no Azure - e crie um grupo de recursos - Azure services AI - language_text

rie um recurso de Análise de Texto no portal Azure.

Obtenha o endpoint e a key.

Insira essas informações no arquivo app.py nas variáveis endpoint e key.

para mais informações sobre como criar seu reposito no azure  acesse : https://learn.microsoft.com/pt-br/training/modules/analyze-text-ai-language/8-exercise-analyze-text


no terminal, execute o seguinte comando para iniciar o servidor Flask:ython app.py


Acesse a Aplicação:  


Abra o navegador e vá para http://127.0.0.1:5000.

so:
Cole o texto no campo "Cole seu texto aqui".
Clique no botão "Gerar Resumo".
O resumo gerado aparecerá na seção "Resumo".






