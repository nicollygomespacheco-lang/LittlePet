from database import conectar_banco
from models.animal import Animal


class AnimalDAO:

    def listar(self):
        with conectar_banco() as conexao:

            registros = conexao.execute("""
                SELECT id, nome, especie, idade, descricao
                FROM animais
                ORDER BY id DESC
            """).fetchall()

        return [
            Animal(
                id=registro["id"],
                nome=registro["nome"],
                especie=registro["especie"],
                idade=registro["idade"],
                descricao=registro["descricao"]
            )
            for registro in registros
        ]

    def buscar_por_id(self, id):
        with conectar_banco() as conexao:

            registro = conexao.execute("""
                SELECT id, nome, especie, idade, descricao
                FROM animais
                WHERE id = ?
            """, (id,)).fetchone()

        if registro is None:
            return None

        return Animal(
            id=registro["id"],
            nome=registro["nome"],
            especie=registro["especie"],
            idade=registro["idade"],
            descricao=registro["descricao"]
        )

    def inserir(self, animal):
        with conectar_banco() as conexao:

            cursor = conexao.execute("""
                INSERT INTO animais
                (nome, especie, idade, descricao)
                VALUES (?, ?, ?, ?)
            """, (
                animal.nome,
                animal.especie,
                animal.idade,
                animal.descricao
            ))

            animal.id = cursor.lastrowid

        return animal

    def atualizar(self, animal):
        with conectar_banco() as conexao:

            conexao.execute("""
                UPDATE animais
                SET nome = ?,
                    especie = ?,
                    idade = ?,
                    descricao = ?
                WHERE id = ?
            """, (
                animal.nome,
                animal.especie,
                animal.idade,
                animal.descricao,
                animal.id
            ))

    def excluir(self, id):
        with conectar_banco() as conexao:

            conexao.execute("""
                DELETE FROM animais
                WHERE id = ?
            """, (id,))