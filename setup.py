#!/usr/bin/env python3
"""
Apollo Logística — Setup Automático
Execute este script UMA VEZ antes de rodar o servidor pela primeira vez.
Ele instala as dependências e cria o banco de dados.
"""

import subprocess
import sys
import os

def run(cmd):
    print(f"  → {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

print("=" * 55)
print("  🚀 Apollo Logística — Configuração Inicial")
print("=" * 55)

# 1. Instalar dependências
print("\n[1/2] Instalando dependências Python...")
ok = run(f"{sys.executable} -m pip install -r requirements.txt --quiet")
if not ok:
    print("  ⚠️  Tente manualmente: pip install -r requirements.txt")
else:
    print("  ✅ Dependências instaladas!")

# 2. Testar qrcode
print("\n[2/2] Verificando módulos...")
try:
    import flask, openpyxl, qrcode, PIL
    print("  ✅ Todos os módulos OK!")
    qr_ok = True
except ImportError as e:
    print(f"  ⚠️  Módulo faltando: {e}")
    print("  O QR Code será gerado pelo browser (modo fallback).")
    qr_ok = False

print("\n" + "=" * 55)
print("  ✅ Configuração concluída!")
print("\n  Para iniciar o servidor, execute:")
print("     python app.py")
print("\n  Acesse em: http://localhost:5000")
print("=" * 55)
