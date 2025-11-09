# Script de limpieza de archivos antiguos
# =========================================
# Este script mueve los archivos antiguos a una carpeta de respaldo

Write-Host "`n" -NoNewline
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🧹 SCRIPT DE LIMPIEZA - Proyecto ABB" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Lista de archivos antiguos
$archivosAntiguos = @(
    "abb_con_sucesor.py",
    "arbol_abb.py",
    "arbol_circulos.py",
    "arbol_formato_grafico.py",
    "visualizador_grafico.py",
    "resultado_ejercicio.py"
)

Write-Host "📋 Archivos que se moverán a la carpeta 'archivos_antiguos':" -ForegroundColor Yellow
Write-Host ""

foreach ($archivo in $archivosAntiguos) {
    if (Test-Path $archivo) {
        Write-Host "  ✓ $archivo" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $archivo (no encontrado)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "⚠️  IMPORTANTE: Esta acción moverá los archivos a 'archivos_antiguos/'" -ForegroundColor Yellow
Write-Host "   Los archivos NO se eliminarán, solo se moverán." -ForegroundColor Yellow
Write-Host ""

$respuesta = Read-Host "¿Deseas continuar? (S/N)"

if ($respuesta -eq "S" -or $respuesta -eq "s") {
    Write-Host ""
    Write-Host "🚀 Iniciando limpieza..." -ForegroundColor Cyan
    Write-Host ""
    
    # Crear carpeta de respaldo si no existe
    if (-not (Test-Path "archivos_antiguos")) {
        New-Item -ItemType Directory -Path "archivos_antiguos" | Out-Null
        Write-Host "  ✓ Carpeta 'archivos_antiguos' creada" -ForegroundColor Green
    } else {
        Write-Host "  ✓ Carpeta 'archivos_antiguos' ya existe" -ForegroundColor Green
    }
    
    Write-Host ""
    Write-Host "📦 Moviendo archivos..." -ForegroundColor Cyan
    Write-Host ""
    
    # Mover cada archivo
    $movidosExitosos = 0
    foreach ($archivo in $archivosAntiguos) {
        if (Test-Path $archivo) {
            try {
                Move-Item $archivo "archivos_antiguos/" -Force
                Write-Host "  ✓ Movido: $archivo" -ForegroundColor Green
                $movidosExitosos++
            } catch {
                Write-Host "  ✗ Error al mover: $archivo" -ForegroundColor Red
            }
        }
    }
    
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "✅ Limpieza completada!" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📊 Resumen:" -ForegroundColor Yellow
    Write-Host "  - Archivos movidos: $movidosExitosos" -ForegroundColor White
    Write-Host "  - Ubicación: archivos_antiguos/" -ForegroundColor White
    Write-Host ""
    Write-Host "💡 Tip: Puedes eliminar la carpeta 'archivos_antiguos' cuando estés" -ForegroundColor Yellow
    Write-Host "   seguro de que todo funciona correctamente." -ForegroundColor Yellow
    Write-Host ""
    
} else {
    Write-Host ""
    Write-Host "❌ Limpieza cancelada. No se movió ningún archivo." -ForegroundColor Red
    Write-Host ""
}

Write-Host "Presiona cualquier tecla para continuar..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
