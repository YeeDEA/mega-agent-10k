# PowerShell wrapper to run the simulation
param(
    [string]$Run = "Run1",
    [string]$ConfigPath = "config.yaml"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$pythonExe = "python"
$simScript = Join-Path $scriptDir "simulate.py"

Write-Host "Running simulation $Run with config $ConfigPath..."
& $pythonExe $simScript -c $ConfigPath -r $Run
if ($LASTEXITCODE -eq 0) {
    Write-Host "Simulation completed successfully."
} else {
    Write-Error "Simulation failed with exit code $LASTEXITCODE"
}
