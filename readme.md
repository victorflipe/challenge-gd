# TechBlog

Projeto MVP para Compartilhamento de Artigos onde é possível:
- Publicar Artigos com suas TAGs correspondentes
- Comentar nos artigos 
- E fazer a busca por TAGs ou pelo título dos artigos

## Tecnologias utilizadas
- **FastAPI** – Backend em Python
- **Postgres** – Banco de dados relacional
- **Vite** – Frontend em React

## Pré-requisitos
- Docker e Docker Compose instalados na sua máquina

## Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/victorflipe/challenge-gd.git
cd challenge-gd
```

2. Execute os containers
```bash
docker-compose up --build -d
```

Isso irá executar:
- A criação dos dados do arquivo json
- O banco de dados na porta 5432
- O backend FastAPI na porta 8000
- O frontend no Vite na porta 5173

3. Acesse o frontend pelo endereço:
```bash
http://localhost:5173
```

4. Acesse a documentação da API em:
```bash
http://localhost:8000/docs
```

Comandos úteis

- Para todos os containers
```bash
docker-compose down
```

- Sobe todos os containers
```bash
docker-compose up --build -d
```

## Estrutura do Projeto
```bash
.
├── backend/       # Código da API FastAPI
├── frontend/      # Código do frontend Vite/React
├── docker-compose.yml
└── README.md
```

## Estrutura do backend
```bash
backend
├── .venv
├── app
│ ├── api
│ ├── application
│ ├── config
│ ├── crud
│ ├── data
│ ├── domain
│ ├── infrastructure
│ ├── schemas
│ ├── tests
│ ├── utils
│ └── main.py
├── .env
├── alembic.ini
├── Dockerfile
└── requirements.txt
```

## Estrutura do frontend
```bash
├── dist
├── node_modules
├── public
├── src
├── .gitignore
├── Dockerfile
├── eslint.config.js
├── index.html
├── package-lock.json
├── package.json
├── README.md
├── tailwind.config.js
└── vite.config.js
```

## Acessando a aplicação

Para acessar a aplicação, basta pegar um usuário que está no json para popular o banco e fazer o seguinte:

- Utilize o primeiro nome + segundo nome + "@teste.com". (Exemplo: victorfelipe@teste.com)
- A senha para todos os usuários do json é "teste"


