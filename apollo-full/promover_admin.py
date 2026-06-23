#!/usr/bin/env python3
"""
Apollo Logística — Promover Admin
Execute: python3 promover_admin.py

Use este script para promover um usuário existente a administrador
diretamente pelo terminal, sem precisar de um admin já logado.
Útil para definir o primeiro administrador do sistema.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apollo.db')

def listar_usuarios(conn):
    rows = conn.execute(
        'SELECT id, usuario, email, role FROM usuarios WHERE verificado=1 ORDER BY id'
    ).fetchall()
    return rows

def main():
    print()
    print("=" * 52)
    print("  🛡️  Apollo Logística — Promover Administrador")
    print("=" * 52)

    if not os.path.exists(DB_PATH):
        print("\n  ❌ Banco de dados não encontrado.")
        print("  Inicie o servidor ao menos uma vez com: python app.py")
        print("  Depois crie uma conta pelo navegador e rode este script novamente.\n")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    usuarios = listar_usuarios(conn)

    if not usuarios:
        print("\n  ❌ Nenhum usuário cadastrado ainda.")
        print("  Acesse http://localhost:5000, crie uma conta e rode este script novamente.\n")
        conn.close()
        return

    print("\n  Usuários cadastrados:\n")
    print(f"  {'ID':<5} {'Usuário':<20} {'E-mail':<30} {'Perfil'}")
    print("  " + "-" * 65)
    for u in usuarios:
        perfil = "🛡️  Admin" if u['role'] == 'admin' else "👷 Funcionário"
        print(f"  {u['id']:<5} {u['usuario']:<20} {u['email']:<30} {perfil}")

    print()
    escolha = input("  Digite o nome de usuário ou e-mail para promover a Admin: ").strip()

    if not escolha:
        print("\n  ❌ Nenhum usuário informado. Encerrando.\n")
        conn.close()
        return

    alvo = conn.execute(
        'SELECT * FROM usuarios WHERE (usuario=? OR email=?) AND verificado=1',
        (escolha, escolha)
    ).fetchone()

    if not alvo:
        print(f"\n  ❌ Usuário '{escolha}' não encontrado ou não verificado.\n")
        conn.close()
        return

    if alvo['role'] == 'admin':
        print(f"\n  ⚠️  '{alvo['usuario']}' já é administrador.\n")
        conn.close()
        return

    print(f"\n  Promover '{alvo['usuario']}' ({alvo['email']}) a Administrador?")
    confirma = input("  Confirmar? (s/N): ").strip().lower()

    if confirma != 's':
        print("\n  ❌ Operação cancelada.\n")
        conn.close()
        return

    conn.execute("UPDATE usuarios SET role='admin' WHERE id=?", (alvo['id'],))
    conn.commit()
    conn.close()

    print()
    print("  ✅ Sucesso! Usuário promovido a Administrador.")
    print(f"     Login: {alvo['email']}")
    print(f"     Agora faça login em http://localhost:5000")
    print(f"     Você será redirecionado ao painel Admin automaticamente.")
    print()

if __name__ == '__main__':
    main()
