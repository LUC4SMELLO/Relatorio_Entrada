# **Relatório Entrada**

Este software foi desenvolvido para facilitar a conferência e manutenção das datas das cargas que chegam da fábrica.

## **Funcionalidades Pricipais**

* **`Preencher Relatório`**: Permite que o usuário preencha um relatório das cargas que chegam da fábrica.
* **`Visualizar Relatórios`**: Possibilita o usuário visualizar relatórios já preenchidos.

## **Tecnologias Utilizadas**

* **`Python 3.14.2+`**
* **`HTML5 e CSS3`**
* **`SQLite3 3.45.3+`**

## **Framework Utilizado**

* **Flask**

## **Banco Dados**

* **usuários.db** - contém todos os usuários cadastrados no sistema.

## Estrutura do Projeto

```
├── main.py
|
|
├── arquivos/
|   ├── PEDIDOS CTA DEZ-25.xlsm
|
├── backend/
|   ├── constants/
|   |    ├── __init__.py
|   |    ├── arquivos.py
|   |    ├── banco_dados.py
|   |
|   ├── models/
|   |    ├── __init__.py
|   |    ├── usuarios.py
|   |
|   ├── validators/
|       ├── __init__.py
|       ├── validar_cadastro.py
|       ├── validar_login.py

|
├── database/
|   ├── __init__.py
|   ├── banco_dados_usuarios.py
|   ├── usuarios.py
|
├── routes/
|   ├── __init__.py
|   ├── cadastro.py
|   ├── homepage.py
|   ├── login.py
|   ├── relatorio_entrada.py
|   ├── selecionar_opcoes.py
|
├── scripts/
|   ├── __init__.py
|   ├── cargas.py
|
├── static/
|   ├── css/
|   |    ├── cadastro.css
|   |    ├── homepage.css
|   |    ├── login.css
|   |    ├── relatorio_entrada.css
|   |    ├── selecionar_opcoes.css
|   |
|   ├── images/
|        ├── logo_dbcambui_2.png
|
├── templates/
|   ├── cadastro.html
|   ├── homepage.html
|   ├── login.html
|   ├── relatorio_entrada.html
|   ├── selecionar_opcoes.html
|
├── views/
|   ├── janela.py
|   ├── menu.py
|
├── .gitignore
├── README.md

```

## **Autoria**
- Lucas Pereira Silva Mello