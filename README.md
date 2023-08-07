# SHIPPING QUOTATION SERVICE API

Esse é um serviço para cotação de valores relativos a fretes.

## Requisitos

* Docker
* Docker Compose
* Poetry (gerenciador de pacotes python usado no projeto)

Para instalar o poetry, basta inserir o comando no terminal:

```$ RUN curl -sSL https://install.python-poetry.org | python3 -```

ou acesse o site para mais informações: **https://python-poetry.org/**

## Instruções

Clone o projeto

```$ git clone git@github.com:Ramon5/shipping_quotation_service.git```

```$ cd shipping_quotation_service```

### configurando as variáveis de ambiente

O projeto possui dois arquivos de variáveis de ambiente: local.env e local.db.env

No terminal faça:

```
$ cp local.env .env 
$ cp local.db.env .db.env
```

Obs: Defina usuário e senha para o banco de dados

### Criando o ambiente virtual e instalando as dependências


```$ poetry install```

Caso haja necessidade em adicionair mais libs ao projeto e será necessário gerar um novo arquivo *requirements.txt* pois esse arquivo é usado
no build da imagem Docker. Para gerar um arquivo requirements atualizado basta executar o comando:

```$ make export_requirements```

### Menu de ajuda

Ao inserir o comando ```make``` no terminal, algumas opções de execução serão exibidas, para acioná-las
basta executar os comandos com o **poetry**:

Exemplo para execução dos formatadores:

```$ poetry run make format```

Exemplo para execução dos testes unitários:

```$ poetry run make unit-tests```

### Rodando a API

para executar os containers da aplicação rode o comando:

```$ docker-compose up```

Esse comando irá subir os containers da api e do banco de dados PostgreSQL

### Documentação dos Endpoints

Para checar os endpoints disponíveis basta acessar o endereço após subir os containers:

http://0.0.0.0/docs

### Melhorias mapeadas

Implementar as outras opções de CRUD, isolar os pipelines de ci/cd e acrescentar pull request semantico, release e um pipeline orquestrador para encadear as execuções de acordo com as prioridades.