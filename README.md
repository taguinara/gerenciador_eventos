# API de Gerenciamento de Produtos

## Descrição

Projeto desenvolvido durante o curso de Ciência de Dados para praticar Python, APIs REST, Flask, Git e GitHub. A aplicação permite gerenciar produtos por meio de requisições HTTP.

## Tecnologias

- Python
- Flask
- API REST
- Git e GitHub
- unittest para testes automatizados

## Funcionalidades

- Listar todos os produtos.
- Consultar um produto pelo ID.
- Cadastrar novos produtos.
- Atualizar produtos existentes.
- Excluir produtos.

## Instalação

Crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Inicie o servidor:

```bash
python server.py
```

A API ficará disponível em:

`http://127.0.0.1:5000`

## Testes

Em outro terminal, execute:

```bash
python -m unittest testar_api -v
```

## Rotas da API

| Método | Endpoint | Função |
|---|---|---|
| GET | `/produtos` | Lista produtos |
| GET | `/produtos?id=1` | Consulta por ID |
| POST | `/produtos` | Cadastra produto |
| PUT | `/produtos/1` | Atualiza produto |
| DELETE | `/produtos/1` | Exclui produto |

**Observação:** os dados são armazenados em memória. Eles são reiniciados quando o servidor é reiniciado.