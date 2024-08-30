## Gerenciador de Questões em Flask
Este é um projeto de aplicação web desenvolvido em Flask para gerenciar questões de múltipla escolha. A aplicação permite adicionar, editar, excluir e verificar respostas de questões armazenadas em um banco de dados SQLite. Este projeto é ideal para criar e gerenciar bancos de questões em ambientes de estudo ou avaliações.

## Funcionalidades
Exibir Questões: Visualize todas as questões armazenadas no banco de dados.
Adicionar Questões: Adicione novas questões com enunciado, alternativas, resposta correta e categoria.
Editar Questões: Edite os detalhes de uma questão existente, incluindo o enunciado e a resposta correta.
Excluir Questões: Remova questões do banco de dados.
Verificar Respostas: Envie respostas para verificar se estão corretas.
Tecnologias Utilizadas
Python 3.x
Flask: Framework web usado para criar a aplicação.
SQLAlchemy: ORM usado para interação com o banco de dados.
SQLite: Banco de dados utilizado para armazenar as questões.
HTML/CSS: Para renderização das páginas web.
Pré-requisitos
Antes de executar o projeto, certifique-se de ter o Python 3.x instalado no seu ambiente.

## Dependências
Instale as dependências do projeto usando o pip:

bash
Copiar código
pip install -r requirements.txt
Estrutura do Projeto
plaintext
Copiar código
|-- app.py                  # Arquivo principal da aplicação Flask
|-- questoes.db             # Banco de dados SQLite (gerado automaticamente)
|-- templates/
|   |-- home.html           # Página inicial
|   |-- questoes.html       # Página que exibe as questões
|   |-- adicionar.html      # Formulário para adicionar uma nova questão
|   |-- editar_1etapa.html  # Página para iniciar a edição de uma questão
|   |-- editar_2etapa.html  # Página para editar uma questão específica
|   |-- excluir.html        # Página para excluir questões
|   |-- confirmado.html     # Página de confirmação após operações
|   |-- erro.html           # Página de erro para buscas não encontradas
|-- static/
    |-- styles.css          # Arquivo de estilo CSS

## Como Executar
Clone o repositório:

bash
Copiar código
git clone https://github.com/LucasPimentel91/BancoQuestao.git
cd nome-do-repositorio
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie o banco de dados:

O banco de dados será criado automaticamente ao executar o aplicativo pela primeira vez.

## Inicie o servidor Flask:

bash
Copiar código
python app.py
A aplicação estará disponível em http://127.0.0.1:5000.

Rotas Principais
/: Página inicial.
/questoes: Exibe todas as questões.
/verificar_resposta: Verifica a resposta enviada (POST).
/adicionar: Página para adicionar uma nova questão.
/editar: Inicia o processo de edição de uma questão.
/editar_questao/<int:id>: Edita uma questão específica.
/excluir: Página para excluir questões.
/config: Página de configuração da aplicação.
## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou encontrar algum problema, fique à vontade para abrir uma issue ou enviar um pull request.

## Autor
Lucas Pimentel - Desenvolvedor - @LucasPimentel91