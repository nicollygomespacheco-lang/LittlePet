from flask import Flask, request, jsonify
from flask_cors import CORS

from database import criar_tabela
from models.animal import Animal
from dao.animal_dao import AnimalDAO


app = Flask(__name__)
CORS(app)

dao = AnimalDAO()


# =========================
# GET - LISTAR ANIMAIS
# =========================

@app.route("/animais", methods=["GET"])
def listar_animais():
    try:
        animais = dao.listar()

        return jsonify([
            animal.to_dict()
            for animal in animais
        ]), 200

    except Exception:
        app.logger.exception("Erro ao listar animais")

        return jsonify({
            "erro": "Não foi possível listar os animais."
        }), 500


# =========================
# POST - CADASTRAR ANIMAL
# =========================

@app.route("/animais", methods=["POST"])
def cadastrar_animal():

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Envie os dados em formato JSON."
        }), 400

    nome = dados.get("nome")
    especie = dados.get("especie")
    idade = dados.get("idade")
    descricao = dados.get("descricao", "")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({
            "erro": "Informe o nome do animal."
        }), 400

    if not isinstance(especie, str) or not especie.strip():
        return jsonify({
            "erro": "Informe a espécie do animal."
        }), 400

    if (
        isinstance(idade, bool)
        or not isinstance(idade, int)
        or idade < 0
    ):
        return jsonify({
            "erro": "A idade deve ser um número inteiro igual ou maior que zero."
        }), 400

    if not isinstance(descricao, str):
        return jsonify({
            "erro": "A descrição deve ser um texto."
        }), 400

    try:

        animal = Animal(
            nome=nome.strip(),
            especie=especie.strip(),
            idade=idade,
            descricao=descricao.strip()
        )

        animal = dao.inserir(animal)

        return jsonify(animal.to_dict()), 201

    except Exception:
        app.logger.exception("Erro ao cadastrar animal")

        return jsonify({
            "erro": "Não foi possível cadastrar o animal."
        }), 500


# =========================
# GET - BUSCAR POR ID
# =========================

@app.route("/animais/<int:id>", methods=["GET"])
def buscar_animal_por_id(id):

    try:

        animal = dao.buscar_por_id(id)

        if animal is None:
            return jsonify({
                "erro": "Animal não encontrado."
            }), 404

        return jsonify(animal.to_dict()), 200

    except Exception:
        app.logger.exception("Erro ao buscar animal")

        return jsonify({
            "erro": "Não foi possível buscar o animal."
        }), 500


# =========================
# PUT - EDITAR ANIMAL
# =========================

@app.route("/animais/<int:id>", methods=["PUT"])
def atualizar_animal(id):

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Envie os dados em formato JSON."
        }), 400

    try:

        animal = dao.buscar_por_id(id)

        if animal is None:
            return jsonify({
                "erro": "Animal não encontrado."
            }), 404

        nome = dados.get("nome")
        especie = dados.get("especie")
        idade = dados.get("idade")
        descricao = dados.get("descricao", "")

        if not isinstance(nome, str) or not nome.strip():
            return jsonify({
                "erro": "Informe o nome do animal."
            }), 400

        if not isinstance(especie, str) or not especie.strip():
            return jsonify({
                "erro": "Informe a espécie do animal."
            }), 400

        if (
            isinstance(idade, bool)
            or not isinstance(idade, int)
            or idade < 0
        ):
            return jsonify({
                "erro": "A idade deve ser um número inteiro igual ou maior que zero."
            }), 400

        if not isinstance(descricao, str):
            return jsonify({
                "erro": "A descrição deve ser um texto."
            }), 400

        animal.nome = nome.strip()
        animal.especie = especie.strip()
        animal.idade = idade
        animal.descricao = descricao.strip()

        dao.atualizar(animal)

        return jsonify(animal.to_dict()), 200

    except Exception:
        app.logger.exception("Erro ao atualizar animal")

        return jsonify({
            "erro": "Não foi possível atualizar o animal."
        }), 500


# =========================
# DELETE - EXCLUIR ANIMAL
# =========================

@app.route("/animais/<int:id>", methods=["DELETE"])
def excluir_animal(id):

    try:

        animal = dao.buscar_por_id(id)

        if animal is None:
            return jsonify({
                "erro": "Animal não encontrado."
            }), 404

        dao.excluir(id)

        return jsonify({
            "mensagem": "Animal excluído com sucesso."
        }), 200

    except Exception:
        app.logger.exception("Erro ao excluir animal")

        return jsonify({
            "erro": "Não foi possível excluir o animal."
        }), 500


# =========================
# INICIAR SERVIDOR
# =========================

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True, port=5000)