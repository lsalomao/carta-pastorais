# Cartas Pastorais

Aplicação web para visualização e consulta de pregações e cartas pastorais.

## Funcionalidades

- Visualização de cartas pastorais em formato de cards
- Filtragem por autor, tema e texto bíblico
- Estatísticas sobre quantidade de pregações e pregadores únicos
- Interface responsiva e amigável

## Tecnologias Utilizadas

- Backend: Python com Flask
- Frontend: HTML, CSS, JavaScript
- Estilização: Bootstrap 5
- Web scraping: Selenium e BeautifulSoup
- Armazenamento: JSON

## Estrutura do Projeto

- `/app.py` - Aplicação principal com rotas Flask e funções de scraping
- `/templates/` - Templates HTML
- `/static/` - Arquivos estáticos (CSS, JavaScript)
- `/devotionals.json` - Banco de dados em formato JSON
- `/scraper/` - Scripts para scraping (opcional)
- `/prepare_deploy.py` - Script para preparação de deploy

## Como Usar

1. Clone o repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Execute a aplicação com `python app.py`
4. Acesse a aplicação em `http://localhost:5000`

## Licença

Este projeto está sob a licença MIT. 