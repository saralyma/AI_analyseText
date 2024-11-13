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



nome-do-repositorio
├── app.py                   
├── templates
  └── index.html           
├── requirements.txt    
└── README.md 

