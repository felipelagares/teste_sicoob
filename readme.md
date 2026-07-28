# Books Scraper RPA

Projeto desenvolvido em Python para automatizar a coleta de dados do site **Books to Scrape**, realizar o download das capas dos livros, armazenar as imagens no Google Drive e registrar os dados em uma planilha do Google Sheets.

## Tecnologias utilizadas

* Python 3.10+
* Selenium
* Google Drive API
* Google Sheets API
* Google Service Account
* Logging

---

# Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd books-scraper
```

Crie um ambiente virtual:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Configurando a autenticação do Google Drive e Google Sheets

O projeto utiliza **Service Account** para acessar as APIs do Google.

## 1. Criar um projeto no Google Cloud

Acesse:

https://console.cloud.google.com/

Crie um novo projeto.

---

## 2. Habilitar as APIs

No menu lateral:

**APIs e Serviços → Biblioteca**

Habilite as seguintes APIs:

* Google Drive API
* Google Sheets API

---

## 3. Criar uma Conta de Serviço

Acesse:

**APIs e Serviços → Credenciais**

Clique em:

**Criar credenciais → Conta de serviço**

Informe um nome para a conta de serviço, por exemplo:

```
books-scraper
```

Conclua a criação.

---

## 4. Gerar a chave JSON

Abra a conta de serviço criada.

Acesse a aba **Chaves**.

Clique em:

```
Adicionar chave
```

Depois:

```
Criar nova chave
```

Selecione:

```
JSON
```

Clique em **Criar**.

O navegador fará o download do arquivo JSON.

Renomeie o arquivo para:

```
credentials.json
```

Crie a pasta `config` no projeto (caso não exista) e mova o arquivo para:

```
project/
│
├── config/
│   └── credentials.json
```

---

## 5. Compartilhar recursos com a Conta de Serviço

A conta de serviço possui um e-mail semelhante a:

```
books-scraper@meu-projeto.iam.gserviceaccount.com
```

Caso utilize uma planilha ou pasta já existente, compartilhe esses recursos com esse e-mail concedendo permissão de **Editor**.

---

# Estrutura do projeto

```
project/
│
├── config/
│   └── credentials.json
│
├── images/
│
├── logs/
│   └── execution.log
│
├── downloader.py
├── drive.py
├── logger.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Executando o projeto

Execute:

```bash
python main.py
```

Durante a execução o robô irá:

* Navegar pelas páginas do catálogo.
* Extrair as informações dos livros.
* Baixar as imagens das capas.
* Criar uma pasta no Google Drive.
* Fazer upload das imagens.
* Registrar os dados na planilha do Google Sheets.
* Salvar os logs em:

```
logs/execution.log
```

---

# Dependências

Instale todas as dependências utilizando:

```bash
pip install -r requirements.txt
```

---

# Observações

* O arquivo `credentials.json` não deve ser versionado no Git.
* Adicione `config/credentials.json` ao arquivo `.gitignore`.
* O diretório `logs/` será criado automaticamente durante a execução.
* O diretório `images/` armazenará temporariamente as capas dos livros baixadas antes do envio ao Google Drive.
