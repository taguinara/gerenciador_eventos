
import unittest
import server


class TestAPIProdutos(unittest.TestCase):

    def setUp(self):
        # Restaura os produtos antes de cada teste
        server.produtos = [
            {"id": 1, "nome": "Notebook", "preco": 4500.00},
            {"id": 2, "nome": "celular", "preco": 2500.00}
        ]

        self.client = server.app.test_client()

    def test_listar_produtos(self):
        resposta = self.client.get("/produtos")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.get_json()), 2)

    def test_buscar_produto_por_id(self):
        resposta = self.client.get("/produtos?id=1")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["nome"], "Notebook")

    def test_produto_nao_encontrado(self):
        resposta = self.client.get("/produtos?id=999")

        self.assertEqual(resposta.status_code, 404)

    def test_criar_produto(self):
        resposta = self.client.post(
            "/produtos",
            json={"nome": "Mouse", "preco": 150.00}
        )

        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.get_json()["nome"], "Mouse")

    def test_atualizar_produto(self):
        resposta = self.client.put(
            "/produtos/1",
            json={"nome": "Notebook atualizado", "preco": 5000.00}
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(
            resposta.get_json()["nome"],
            "Notebook atualizado"
        )

    def test_excluir_produto(self):
        resposta = self.client.delete("/produtos/2")

        self.assertEqual(resposta.status_code, 200)

        consulta = self.client.get("/produtos?id=2")
        self.assertEqual(consulta.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
