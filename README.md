📝 To-Do List API - Python

Uma API RESTful desenvolvida em Python para gerenciamento de tarefas (To-Do List), com autenticação via tokens e controle de usuários.
O projeto inclui criação e conexão com banco de dados, autenticação segura, validação de dados e endpoints para CRUD de tarefas.


🚀 Funcionalidades

    Cadastro e autenticação de usuários com token JWT

    Criação, listagem, atualização e exclusão de tarefas

    Validação de dados de entrada

    Banco de dados relacional para persistência das informações

    Controle de acesso: apenas o dono da conta pode gerenciar suas tarefas

🛠 Tecnologias Utilizadas

    Python 3.10+

    Flask (ou FastAPI, dependendo do que usamos)

    SQLAlchemy (ORM para interação com o banco)

    SQLite/MySQL/PostgreSQL (dependendo do banco usado)

    PyJWT para autenticação via tokens

    Marshmallow para validação de dados

📚 Endpoints Principais
Autenticação

    POST /register → Criar conta de usuário

    POST /login → Autenticar e gerar token JWT

Tarefas

    GET /tasks → Listar todas as tarefas do usuário autenticado

    POST /tasks → Criar nova tarefa

    PUT /tasks/<id> → Atualizar tarefa

    DELETE /tasks/<id> → Excluir tarefa

    Obs: Todas as rotas de tarefas exigem token JWT no header:
    Authorization: Bearer <seu_token>
