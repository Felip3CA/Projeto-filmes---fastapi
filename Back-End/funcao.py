from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS movies (
                    id SERIAL PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    avaliacao REAL       
                    )

                 """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
                cursor.close()
                conexao.close()

criar_tabela()

def criar_filme(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO movies (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_filme("Era eu", "Ficção", 2005, 5.0)

def listar_movies():
    conexao, cursor = conectar()
    if conexao:
        try:
                cursor.execute(
                    "SELECT * FROM movies ORDER BY id"
                
            )
                return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()
listar_movies()


def atualizar_movies(id_filme, nova_avaliacao):
     conexao, cursor = conectar()
     if conexao:
        try:
            cursor.execute(
              "UPDATE movies SET avaliacao = %s WHERE id = %s",
              (nova_avaliacao, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar a nota do filme {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_filme(id_filme):
         conexao, cursor = conectar()
         if conexao:
            try:
                 cursor.execute(
                      "DELETE FROM movies WHERE id = %s", (id_filme,)
                 )
                 conexao.commit()
            except Exception as erro:
                 print(f"Erro ao deletar filme : {erro}")
            finally:
                cursor.close()
                conexao.close()

deletar_filme(4)


def buscar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM movies WHERE id = %s", (id_filme,)
            )
            filme = cursor.fetchone()
            return filme
        except Exception as erro:
            print(f"Erro ao buscar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()
