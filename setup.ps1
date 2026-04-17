# Create virtual environment and install dependencies

$venvPath = ".venv"

if (-Not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venvPath
} else {
    Write-Host "Virtual environment already exists, skipping creation."
}

Write-Host "Installing dependencies from requirements.txt..."
& "$venvPath\Scripts\pip" install -r requirements.txt

Write-Host "Done."
