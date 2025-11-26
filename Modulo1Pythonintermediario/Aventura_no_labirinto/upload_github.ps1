# Caminho da pasta do jogo
$PastaJogo = "C:\Users\wagner\Desktop\Aventura_no_labirinto"
$RepoGitHub = "https://github.com/deborahmelo-0128/Pythonintermediario/tree/main/Modulo1Pythonintermediario"

# ========== Verificações ==========
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git não está instalado. Instale o Git e rode o script novamente." -ForegroundColor Red
    exit
}

if (-not (Test-Path $PastaJogo)) {
    Write-Host "❌ A pasta $PastaJogo não foi encontrada!" -ForegroundColor Red
    exit
}

Set-Location $PastaJogo
Write-Host "📂 Diretório atual: $PastaJogo" -ForegroundColor Cyan

# ========== Criar .gitignore se não existir ==========
if (-not (Test-Path ".gitignore")) {
    @"
__pycache__/
*.pyc
*.pyo
*.DS_Store
.vscode/
"@ | Out-File -Encoding UTF8 ".gitignore"
    Write-Host "🧹 Arquivo .gitignore criado." -ForegroundColor Green
}

# ========== Inicializar Git se necessário ==========
if (-not (Test-Path ".git")) {
    git init | Out-Null
    Write-Host "🚀 Repositório Git inicializado." -ForegroundColor Green
}

# ========== Verificar conexão com o repositório remoto ==========
$remote = git remote get-url origin 2>$null
if (-not $remote) {
    git remote add origin $RepoGitHub
    Write-Host "🔗 Repositório remoto conectado a:" $RepoGitHub -ForegroundColor Green
}
elseif ($remote -ne $RepoGitHub) {
    git remote set-url origin $RepoGitHub
    Write-Host "🔁 Repositório remoto atualizado para:" $RepoGitHub -ForegroundColor Yellow
}

# ========== Adicionar e fazer commit apenas se houver mudanças ==========
$Status = git status --porcelain
if ($Status) {
    git add .
    $data = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "Atualização automática em $data"
    Write-Host "💾 Commit criado com as mudanças." -ForegroundColor Green
} else {
    Write-Host "✅ Nenhuma mudança detectada. Nada para enviar." -ForegroundColor Yellow
}

# ========== Configurar branch principal ==========
git branch -M main

# ========== Enviar para o GitHub ==========
Write-Host "⬆️ Enviando alterações para o GitHub..." -ForegroundColor Cyan
try {
    git push -u origin main
    Write-Host "🎉 Upload concluído com sucesso! Verifique no GitHub." -ForegroundColor Green
}
catch {
    Write-Host "⚠️ Ocorreu um erro ao enviar. Verifique a conexão e as credenciais." -ForegroundColor Red
}
