# Sicoob Book Scraper

## Descrição

O **Sicoob Book Scraper** é um projeto de automação desenvolvido em **Python** para realizar a coleta de dados do catálogo do site **Books to Scrape**.

O robô navega pelas páginas do catálogo, extrai informações dos livros, faz o download das imagens das capas, realiza o upload das imagens para o **Google Drive** e registra os dados em uma **planilha do Google Sheets**.

---

# Tecnologias utilizadas

* Python 3.12.7
* Selenium
* WebDriver Manager
* Requests
* Google Drive API
* Google Sheets API
* OAuth 2.0
* Logging

---

# Estrutura do projeto

```text
teste_sicoob/
│
├── config/
│   ├── client_secret.json
│   ├── token.json
│   └── token_sheets.json
│
├── google_api/
│   ├── drive.py
│   └── sheets.py
│
├── images/
│
├── logs/
│   ├── execution.log
│   └── logger.py
│
├── scrapping/
│   ├── image_downloader.py
│   └── scrapper.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Como instalar

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Acesse a pasta:

```bash
cd teste_sicoob
```

Crie um ambiente virtual:

Windows

```bash
python -m venv venv
```

Ative o ambiente virtual:

Windows (PowerShell)

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Como executar

Execute:

```bash
python main.py
```

Durante a primeira execução será aberta uma janela do navegador solicitando autorização da conta Google.

Após a autorização serão criados automaticamente os arquivos:

```text
config/token.json
config/token_sheets.json
```

Nas próximas execuções não será necessário realizar uma nova autenticação.

---

# Configuração das credenciais do Google

Este projeto utiliza **OAuth 2.0** para autenticação nas APIs do Google Drive e Google Sheets.

## 1. Criar um projeto

Acesse o Google Cloud Console:

https://console.cloud.google.com/

Crie um novo projeto.

---

## 2. Ativar as APIs

No projeto criado, habilite:

* Google Drive API
* Google Sheets API

---

## 3. Configurar a Tela de Consentimento OAuth

Em **APIs e Serviços → Tela de consentimento OAuth**:

* Tipo de usuário: Externo
* Preencha os campos obrigatórios
* Adicione sua conta Google em **Usuários de teste**

---

## 4. Criar as credenciais OAuth

Em **APIs e Serviços → Credenciais**:

* Criar credenciais
* ID do cliente OAuth
* Tipo: Aplicativo para computador (Desktop App)

Faça o download do arquivo JSON.

Renomeie o arquivo para:

```text
client_secret.json
```

Coloque-o na pasta:

```text
config/
```

**Importante:** o arquivo `client_secret.json` contém informações sensíveis e **não deve ser enviado ao repositório Git**.

Recomenda-se adicionar ao arquivo `.gitignore`:

```text
config/client_secret.json
config/token.json
config/token_sheets.json
```

---

# Funcionamento do robô

O fluxo da automação é:

1. Acessa o site Books to Scrape.
2. Percorre as três primeiras páginas do catálogo.
3. Extrai:

   * título;
   * preço;
   * avaliação (rating);
   * disponibilidade;
   * URL da imagem.
4. Faz o download da imagem da capa.
5. Envia a imagem para uma pasta no Google Drive.
6. Cria uma planilha no Google Sheets.
7. Registra os dados dos livros e o link da imagem na planilha.
8. Registra toda a execução no arquivo `logs/execution.log`.

---

# Logs

Os logs da aplicação são gravados em:

```text
logs/execution.log
```

São registrados:

* início e fim da execução;
* processamento de páginas;
* upload das imagens;
* criação da planilha;
* exceções e falhas durante a execução.

---

# Decisões técnicas

Durante o desenvolvimento foram tomadas as seguintes decisões:

* Utilização do Selenium para navegação por apresentar uma implementação simples e adequada ao desafio.
* Separação da aplicação em módulos (`scrapping`, `google_api` e `logs`) para melhorar a organização e facilitar a manutenção.
* Utilização do módulo `logging` para registrar a execução e possíveis erros.
* Utilização do `webdriver-manager` para eliminar a necessidade de instalação manual do ChromeDriver.
* Utilização do OAuth 2.0 para autenticação no Google Drive e Google Sheets, permitindo integração com contas Google pessoais.

---

# Possíveis melhorias

Caso houvesse mais tempo disponível, seriam implementadas as seguintes melhorias:

* Configuração por meio de variáveis de ambiente (.env).
* Testes unitários para os módulos de scraping e integração.
* Tratamento mais detalhado de exceções e política de retentativas para falhas temporárias.
* Execução paralela do download e upload das imagens para melhorar desempenho.
* Parametrização da quantidade de páginas a serem processadas.
* Geração automática de relatórios ao término da execução.
