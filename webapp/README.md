# Aplicação de Visualização de Pregações

## Descrição

Aplicação web para visualizar e filtrar dados de pregações/cartas pastorais.

## Estrutura do Projeto

```
webapp/
  ├── app.py              # Aplicação Flask principal
  ├── wsgi.py             # Arquivo WSGI para implantação
  ├── requirements.txt    # Dependências do projeto
  ├── data/               # Diretório para armazenar os dados
  │   └── devotionals.json  # Arquivo de dados (deve ser copiado para este diretório)
  ├── static/             # Arquivos estáticos
  │   ├── css/            # Estilos CSS
  │   │   └── style.css
  │   └── js/             # Scripts JavaScript
  │       └── script.js
  └── templates/          # Templates HTML
      └── index.html
```

## Requisitos

- Python 3.8 ou superior
- Flask e outras dependências (listadas em requirements.txt)

## Instruções para Implantação no Webuzo

### 1. Preparação do Ambiente

1. Acesse o painel de controle do Webuzo.
2. Instale o Python (se ainda não estiver instalado).
3. Instale o mod_wsgi para Apache (se ainda não estiver instalado).

### 2. Transferência de Arquivos

1. Faça upload de toda a pasta `webapp` para o servidor (via FTP ou outro método).
2. Certifique-se de que o arquivo `devotionals.json` esteja presente no diretório `data/`.

### 3. Configuração do Ambiente Virtual (Opcional, mas Recomendado)

```bash
cd /caminho/para/webapp
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configuração do Apache

1. Acesse o painel de controle do Webuzo.
2. Vá para a seção de Virtual Hosts ou Apache Configuration.
3. Adicione uma nova configuração ou edite a existente, incluindo:

```apache
<VirtualHost *:80>
    ServerName seudominio.com

    WSGIDaemonProcess pregacoes python-home=/caminho/para/webapp/venv python-path=/caminho/para/webapp
    WSGIProcessGroup pregacoes
    WSGIScriptAlias / /caminho/para/webapp/wsgi.py

    <Directory /caminho/para/webapp>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

4. Reinicie o Apache:

```bash
service apache2 restart
```

### 5. Verificação

1. Acesse seu domínio em um navegador para verificar se a aplicação está funcionando corretamente.
2. Verifique os logs de erro do Apache em caso de problemas.

## Manutenção

### Atualização de Dados

Para atualizar os dados, copie o novo arquivo `devotionals.json` para o diretório `data/` e reinicie a aplicação:
