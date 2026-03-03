#!/bin/bash
# Instrucciones para hacer push al repositorio de GitHub
# Ejecutar desde el directorio del repositorio

echo "=== PUSH A GITHUB ==="
echo "Repositorio: https://github.com/adrianlerer/predatory-invitations-as-extended-phenotype"
echo "Branch: main"
echo ""
echo "Ejecutando push..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Push exitoso!"
    echo "Ver repositorio en: https://github.com/adrianlerer/predatory-invitations-as-extended-phenotype"
else
    echo "❌ Push falló - se requiere autenticación"
    echo ""
    echo "Opciones:"
    echo "1. Configurar GitHub en la interfaz de GenSpark (pestaña #github)"
    echo "2. O ejecutar manualmente desde su máquina local"
fi
