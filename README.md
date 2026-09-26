# Chat Simultâneo

Projeto de chat em tempo real com frontend em React + Vite e backend em Flask + SQLite.

Prints do projeto: https://drive.google.com/drive/folders/1iAwHyMjSkY95Ln24XsA_R1mS3WD5MGKx

## Visão geral

Este projeto permite enviar e visualizar mensagens em tempo real, com:

- Frontend em React
- Backend em Flask
- Banco SQLite para armazenamento das mensagens
- Comunicação via API REST

## Estrutura do projeto

```text
Chat Simultaneo/
├── Back-end/
│   ├── database.db
│   ├── requirements.txt
│   └── server.py
├── Front-end/
│   ├── App.tsx
│   ├── index.html
│   ├── main.tsx
│   ├── package.json
│   ├── style.css
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite-env.d.ts
│   └── vite.config.ts
├── .gitignore
├── README.md
└── LICENSE
```

## Requisitos

- Python 3.10+
- Node.js 18+
- npm

## Configuração do backend

1. Acesse a pasta do backend:
   ```bash
   cd Back-end
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o servidor:
   ```bash
   python server.py
   ```

O backend ficará disponível em:

- http://localhost:5000

## Configuração do frontend

1. Acesse a pasta do frontend:
   ```bash
   cd Front-end
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Inicie a aplicação:
   ```bash
   npm run dev
   ```

A aplicação ficará disponível em:

- http://localhost:5173

## Endpoints da API

### POST /send
Envia uma mensagem.

Exemplo de corpo JSON:

```json
{
  "username": "João",
  "message": "Olá, mundo!"
}
```

### GET /messages
Retorna todas as mensagens salvas.

## Funcionalidades

- Envio de mensagens com nome do usuário
- Listagem das mensagens em ordem cronológica
- Atualização automática da conversa
- Persistência local usando SQLite

## Autor

Matheus Oliveira

## Licença

Este projeto está sob licença MIT.
