# Guia de Uso

## Índice
[1 Introdução](#1-introdução)

[2 Guia de uso do executável](#2-guia-de-uso-do-executável)

[3 Guia de desenvolvimento](#3-guia-de-desenvolvimento)

## 1 Introdução

## 2 Guia de uso do executável

### 2.1 Windows

### 2.2 Linux

### 2.3 Mac

### 2.4 TODO: \* REQUISITOS FUNCIONAIS / NAO FUNCIONAIS ?

## 3 Guia de desenvolvimento

### 3.1 Download do projeto

Faça o download deste repositório ou clone via SSH, como descrito abaixo.

Configure uma chave SSH para sua conta no GitHub:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

Clone o repositório do GitHub para sua máquina:
```
$ git clone git@github.com:tamiresdr/tool-manager.git
```

### 3.2 Dependências
- Python >= 3.10
- Poetry (`$ pip install poetry`)
- Git

### 3.3 Como utilizar?
\* Garanta que todas as dependências listadas na seção [Dependências](#32-dependências) estão instaladas corretamente.

Copie o arquivo `env-example` para seu `.env`:
```
$ cp env-example .env
```

Prepare seu ambiente de desenvolvimento:
```
$ make init-dev
```

Crie as tabelas no banco de dados:
```
$ make migrate
```

Agora rode a aplicação e "corra para o abraço":
```
$ make run
```

### 3.4 Garanta um código limpo e padronizado
Formate o código automaticamente:
```
$ make lint
```

Cheque se o código está seguindo as boas práticas:
```
$ make lint-check
```

### 3.5 Testes automatizados
