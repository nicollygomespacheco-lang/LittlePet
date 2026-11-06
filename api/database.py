import sqlite3
from pathlib import Path


PASTA = Path(__file__).resolve().parent
BANCO = PASTA / "littlepet.db"


def conectar_banco():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    with conectar_banco() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS animais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT NOT NULL,
                idade INTEGER NOT NULL,
                descricao TEXT
            )
        """)