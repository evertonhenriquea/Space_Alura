# ✨ Alura Space: Galeria de Fotos Cósmicas

## 📝 Sobre o Projeto

Este projeto nasceu da necessidade de aplicar, de forma prática e em um projeto real, os conceitos de desenvolvimento back-end com **Python** e o framework **Django**. 

O **Alura Space** é uma galeria de fotos cósmicas que simula um sistema de gerenciamento de conteúdo (Content-Driven), permitindo aos usuários autenticados catalogar, exibir e administrar imagens espaciais. Nosso foco foi construir uma aplicação **robusta, modular e segura**, seguindo as melhores práticas do Django para **autenticação** e **CRUD** de dados.

---

## 🚀 Funcionalidades Chave

* **🔑 `apps/usuarios/auth/`**: **Autenticação Full-Stack**
    * Sistema completo de **Login**, **Cadastro** e **Logout** implementado em um App dedicado (`usuarios`), garantindo isolamento da lógica de autenticação.
* **📸 `apps/galeria/crud/`**: **CRUD de Imagens**
    * Completa manipulação de fotos (**Criar**, **Ler**, **Atualizar**, **Deletar**) via interface do usuário, além do acesso pelo Django Admin.
* **🔍 `apps/galeria/filters/`**: **Filtros e Pesquisas**
    * Funcionalidade de pesquisa textual por nome e filtro por categorias (ex: "Nebulosas", "Planetas") para otimizar a organização e visualização do conteúdo.
* **🛡️ `templates/shared/`**: **Boas Práticas & Reuso**
    * Estrutura modular (`galeria`, `usuarios`), separação de templates (`partials`, `shared`) e gestão eficiente de *static files*, refletindo a arquitetura limpa do projeto.

---

## 🛠️ Stack Tecnológica

| Tecnologia | Descrição |
| :--- | :--- |
| 🐍 **Python** | Linguagem principal de desenvolvimento. |
| 🌐 **Django** | Framework web de alto nível para desenvolvimento rápido e seguro. |
| 🖥️ **HTML/CSS** | Front-end renderizado via *Django Templates*. |
| 🗃️ **SQLite3** | Banco de dados padrão para desenvolvimento local. |

---
## ⚙️ Configuração e Instalação

Siga estes passos simples para rodar o projeto localmente:

### 1. Clonagem e Navegação

git clone [https://github.com/evertonhenriquea/Space_Alura]

cd alura-space


### 2. Ambiente Virtual e Dependências

python3 -m venv venv

source venv/bin/activate

pip install -r riquarements.txt

### 3. Banco de Dados e Migrações

python manage.py makemigrations

python manage.py migrate

### 4. Superusuário (Opcional)

python manage.py createsuperuser

### 5. Execução do Servidor

python manage.py runserver


---

## 📂 Estrutura de Diretórios (Básica)

| Diretório | Tipo | Função |
| :--- | :--- | :--- |
| `setup/` | **Core** | Configurações globais (`settings.py`, `urls.py` principal). |
| `apps/galeria/` | **App** | Lógica (Models, Views) e Templates para o CRUD de fotos. |
| `apps/usuarios/` | **App** | Lógica (Views) e Forms para Autenticação (Login, Cadastro). |
| `templates/` | **Front-end** | Arquivos HTML organizados por App e reutilizáveis (`shared/`). |
| `static/` | **Assets** | Arquivos estáticos (CSS, imagens) da aplicação. |

---

## 🧑‍💻 Autor

Desenvolvido por **[Everton Henrique]** como parte da Formação Django da Alura.

* [**LinkedIn**](https://www.linkedin.com/in/everton-henrique-b447ab299/)
* [**GitHub**](https://github.com/evertonhenriquea)