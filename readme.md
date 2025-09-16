# TechBlog

Projeto de exemplo utilizando **FastAPI**, **Postgres** e **Vite (React)**.

## Tecnologias utilizadas
- **FastAPI** – Backend em Python
- **Postgres** – Banco de dados relacional
- **Vite** – Frontend em React

## Pré-requisitos
- Docker e Docker Compose instalados na sua máquina
- Node.js (apenas se quiser rodar o frontend fora do container)

## Como executar o projeto

1. Clone o repositório:
```bash
git clone <url-do-repo>
cd <nome-do-repo>
```

2. Execute os containers
```bash
docker-compose up --build
```

Isso irá subir:
- banco de dados na porta 5432
- backend FastAPI na porta 8000
- frontend no Vite na porta 5173

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

## Estrutura do Projeto
```bash
.
├── backend/       # Código da API FastAPI
├── frontend/      # Código do frontend Vite/React
├── docker-compose.yml
└── README.md
```
