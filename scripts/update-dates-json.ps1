#!/usr/bin/env pwsh
# Script: update-dates-json.ps1
# Scans reports/ directory and updates dates.json for the date selector dropdown
$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot/..

$reportsDir = "reports"
$datesJson = "dates.json"

if (Test-Path $reportsDir) {
    $dates = Get-ChildItem $reportsDir -Filter "*.html" | ForEach-Object { $_.BaseName } | Sort-Object -Descending
} else {
    $dates = @()
}

# Force output as JSON array even for single element; ConvertTo-Json -AsArray needs PS 7+
$json = "[" + (($dates | ForEach-Object { "`"$_`"" }) -join ",") + "]"
Set-Content -Path $datesJson -Value $json -Encoding UTF8
Write-Host "Updated dates.json with $($dates.Count) entries"
Pop-Location
