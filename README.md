# API RIO

O projeto é desenvolvido com **FastAPI** e escrito em **Python**, utilizando **Docker** para containerização.

---

## REQUISITOS

- **Python** `v3.9+`
- **FastAPI** `v0.70.0+`
- **Uvicorn** `v0.15.0+`
- **Docker** `v20.10.x+`
- **Docker Compose** `v1.29.x+`

Caso você já tenha o Docker e Docker Compose instalados, execute:

**`docker-compose up -d`** 

Verifique se todos os requisitos estão instalados, executando os seguintes comandos:

**`python --version`**
**`docker --version`**
**`docker-compose --version`**


## COMO USAR

Com tudo devidamente instalado e configurado, use os seguintes comandos para rodar a aplicação:

- Se é a primeira vez rodando o projeto:

* **`docker-compose up -d`**: para rodar os containers da API e qualquer outro serviço necessário;

- Se você já possui o projeto configurado:

* **`docker-compose start`**: para iniciar o Docker já com os projetos nos containers;

- Nota: o Docker é reiniciado, então basta abrir o Docker e verificar se ele já está rodando.

## COMO CONSTRUIR PARA PRODUÇÃO

Para construir para produção siga os passos abaixo:

- Nota: certifique-se de criar um arquivo **.env** na raiz do projeto e configurá-lo conforme o **.env.example**.

* **`docker-compose -f docker-compose.yml up --build`**: para construir a imagem de produção e rodar os containers. 

## ALTA DISPONIBILIDADE

Para garantir alta disponibilidade, este projeto está configurado para ser executado com Docker Swarm.

1. Inicie o Docker Swarm:
```sh
docker swarm init
```

2. Faça o deploy da stack:
```sh
docker stack deploy -c docker-compose.yml api-rio
```
3. Monitore os serviços:
```sh
docker service ls
```

## DOCUMENTAÇÃO DA API
Após iniciar o projeto, você pode acessar a documentação interativa da API nas seguintes URLs:

- Swagger: http://localhost:8888/docs
- Redoc: http://localhost:8888/redoc

## Estrutura de Arquivos

API RIO/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       └── media.py
│   ├── core/
│   │   ├── auth.py
│   │   └── logger.py
│   └── main.py
├── .env
├── .env.example
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

---

_©2024 L8 Group_

---