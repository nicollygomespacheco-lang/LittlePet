from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from pathlib import Path

app = Flask(__name__)
CORS(app)

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


@app.route("/animais", methods=["GET"])
def listar_animais():
    try:
        with conectar_banco() as conexao:
            animais = conexao.execute(
                "SELECT * FROM animais ORDER BY id DESC"
            ).fetchall()

        return jsonify([dict(animal) for animal in animais]), 200

    except sqlite3.Error:
        app.logger.exception("Erro ao listar animais")
        return jsonify({"erro": "Não foi possível listar os animais."}), 500


@app.route("/animais", methods=["POST"])
def cadastrar_animal():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie os dados em formato JSON."}), 400

    nome = dados.get("nome")
    especie = dados.get("especie")
    idade = dados.get("idade")
    descricao = dados.get("descricao", "")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "Informe o nome do animal."}), 400

    if not isinstance(especie, str) or not especie.strip():
        return jsonify({"erro": "Informe a espécie do animal."}), 400

    if isinstance(idade, bool) or not isinstance(idade, int) or idade < 0:
        return jsonify({"erro": "A idade deve ser um número inteiro igual ou maior que zero."}), 400

    if not isinstance(descricao, str):
        return jsonify({"erro": "A descrição deve ser um texto."}), 400

    try:
        with conectar_banco() as conexao:
            cursor = conexao.execute(
                """INSERT INTO animais (nome, especie, idade, descricao)
                   VALUES (?, ?, ?, ?)""",
                (nome.strip(), especie.strip(), idade, descricao.strip())
            )

            animal = conexao.execute(
                "SELECT * FROM animais WHERE id = ?",
                (cursor.lastrowid,)
            ).fetchone()

        return jsonify(dict(animal)), 201

    except sqlite3.Error:
        app.logger.exception("Erro ao cadastrar animal")
        return jsonify({"erro": "Não foi possível cadastrar o animal."}), 500


if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True, port=5000)