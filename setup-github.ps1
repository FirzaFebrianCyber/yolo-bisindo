# Script untuk Push ke GitHub
# Jalankan: .\setup-github.ps1

Write-Host "🚀 YOLO BISINDO - GitHub Push Setup" -ForegroundColor Cyan
Write-Host ""

# Input GitHub username
$username = Read-Host "Masukkan GitHub username Anda"
if ([string]::IsNullOrEmpty($username)) {
    Write-Host "❌ Username tidak boleh kosong!" -ForegroundColor Red
    exit
}

# Input repo name (optional, default: yolo-bisindo)
$repoName = Read-Host "Masukkan nama repository (default: yolo-bisindo)"
if ([string]::IsNullOrEmpty($repoName)) {
    $repoName = "yolo-bisindo"
}

$repoUrl = "https://github.com/$username/$repoName.git"

Write-Host ""
Write-Host "📝 Konfigurasi:" -ForegroundColor Green
Write-Host "  Username: $username"
Write-Host "  Repository: $repoName"
Write-Host "  URL: $repoUrl"
Write-Host ""

# Confirm
$confirm = Read-Host "Lanjutkan? (y/n)"
if ($confirm -ne "y") {
    Write-Host "❌ Dibatalkan" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "🔧 Mengkonfigurasi Git..." -ForegroundColor Yellow

# Add remote
git remote add origin $repoUrl
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error menambahkan remote" -ForegroundColor Red
    exit
}

# Rename branch to main
git branch -M main
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️ Warning pada rename branch (mungkin sudah 'main')" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📤 Pushing ke GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ SUCCESS! Repository berhasil di-push ke GitHub!" -ForegroundColor Green
    Write-Host "🌐 URL: https://github.com/$username/$repoName" -ForegroundColor Green
    Write-Host ""
    Write-Host "🚀 Untuk deploy ke Streamlit Cloud:" -ForegroundColor Cyan
    Write-Host "   1. Buka https://share.streamlit.io"
    Write-Host "   2. Login dengan GitHub"
    Write-Host "   3. Create app dengan repo: $repoName"
    Write-Host "   4. Main file: yolo_bisindo.py"
} else {
    Write-Host ""
    Write-Host "❌ Error saat push. Pastikan:" -ForegroundColor Red
    Write-Host "   - Repository sudah dibuat di GitHub"
    Write-Host "   - Git credentials sudah ter-setup"
    Write-Host "   - Network connection aktif"
}
