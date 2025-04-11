import os
import shutil
import json


def prepare_deploy():
    """
    Prepara os arquivos para deploy no Webuzo.
    - Copia devotionals.json para webapp/data/
    - Verifica se todos os arquivos necessários estão presentes
    """
    print("Preparando arquivos para deploy...")

    # 1. Criar diretório data se não existir
    if not os.path.exists("webapp/data"):
        os.makedirs("webapp/data")
        print("Diretório webapp/data criado.")

    # 2. Copiar devotionals.json para webapp/data
    if os.path.exists("devotionals.json"):
        shutil.copy2("devotionals.json", "webapp/data/devotionals.json")
        print("Arquivo devotionals.json copiado para webapp/data/")

        # Verificar se o arquivo tem conteúdo válido
        try:
            with open("webapp/data/devotionals.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"devotionals.json contém {len(data)} registros.")
        except json.JSONDecodeError:
            print("AVISO: O arquivo devotionals.json não contém JSON válido!")
    else:
        print("ERRO: Arquivo devotionals.json não encontrado!")
        return

    # 3. Verificar se todos os arquivos necessários existem
    files_to_check = [
        "webapp/app.py",
        "webapp/wsgi.py",
        "webapp/requirements.txt",
        "webapp/templates/index.html",
        "webapp/static/css/style.css",
        "webapp/static/js/script.js"
    ]

    missing_files = []
    for file_path in files_to_check:
        if not os.path.exists(file_path):
            missing_files.append(file_path)

    if missing_files:
        print("AVISO: Os seguintes arquivos estão faltando:")
        for file_path in missing_files:
            print(f"  - {file_path}")
    else:
        print("Todos os arquivos necessários estão presentes.")

    print("\nPreparação concluída!")
    print("\nInstruções para deploy:")
    print("1. Compacte a pasta 'webapp' em um arquivo ZIP")
    print("2. Faça upload do arquivo ZIP para o servidor Webuzo")
    print("3. Descompacte o arquivo no servidor")
    print("4. Configure o Apache conforme as instruções no README.md")


if __name__ == "__main__":
    prepare_deploy()
