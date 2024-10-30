# 🐍 Projeto de Estudo com Arquitetura DDD em Python

Bem-vindo ao repositório do **Projeto de Estudo com Arquitetura Domain-Driven Design (DDD) usando Python**. Este projeto foi criado para demonstrar e praticar os princípios do DDD utilizando a linguagem Python.

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## 📚 Visão Geral

Este repositório contém uma aplicação exemplo que implementa uma arquitetura baseada em DDD. O objetivo principal é fornecer uma base sólida para desenvolver aplicações complexas, mantendo a lógica de negócios bem organizada e desacoplada de detalhes técnicos.

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web usado para a criação da API.
- **SQLAlchemy**: ORM utilizado para gerenciamento do banco de dados.
- **pytest**: Ferramenta de testes automatizados.

## 📂 Estrutura do Projeto

A estrutura do projeto segue os princípios do DDD, dividindo o código em camadas e módulos bem definidos:
project/ │ ├── app/ │ ├── init.py │ ├── controllers/ │ ├── models/ │ ├── repositories/ │ ├── services/ │ └── views/ │ ├── tests/ │ ├── init.py │ ├── test_controllers.py │ ├── test_models.py │ └── test_services.py │ ├── migrations/ │ ├── requirements.txt │ └── README.md


## 📝 Instalação

Para configurar o ambiente do projeto, siga os passos abaixo:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Crie um ambiente virtual e ative-o:
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

## 🧪 Testes

Para executar os testes automatizados, utilize o comando:
```bash
pytest

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

