@echo off
echo ========================================
echo 🚀 Gerando documentação HTML com pdoc...
echo ========================================

REM Ativa o ambiente virtual
call .venv\Scripts\activate

REM Cria pasta de saída se não existir
if not exist docs mkdir docs

REM Gera a documentação HTML dentro da pasta "docs"
python -m pdoc aventura_pkg -o docs --no-search

echo.
echo ✅ Documentação HTML gerada com sucesso!
echo 📂 Os arquivos estão na pasta: docs\
echo 🌐 Abra "docs\aventura_pkg.html" no seu navegador.
start docs\aventura_pkg.html
pause
