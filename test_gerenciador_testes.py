import unittest
from unittest.mock import patch
from io import StringIO

# Importa as funções que serão testadas
from gerenciador_testes_app import adicionar_cenario, listar_cenarios, deletar_cenario

class TestGerenciadorCenarios(unittest.TestCase):

    # Testa a adição de um cenário válido
    def test_adicionar_cenario_valido(self):
        cenarios = []
        with patch('builtins.input', return_value='Cenário: login com credenciais válidas'):
            with patch('sys.stdout', new=StringIO()) as output:
                adicionar_cenario(cenarios)
        self.assertIn('Cenário: login com credenciais válidas', cenarios)
        self.assertIn('✅ Cenário adicionado com sucesso!', output.getvalue())

    # Testa a tentativa de adicionar uma descrição vazia
    def test_adicionar_cenario_vazio(self):
        cenarios = []
        with patch('builtins.input', return_value='   '):  # Apenas espaços
            with patch('sys.stdout', new=StringIO()) as output:
                adicionar_cenario(cenarios)
        self.assertEqual(cenarios, [])  # Lista deve continuar vazia
        self.assertIn('⚠️ Descrição vazia não pode ser adicionada.', output.getvalue())

    # Testa a listagem correta de cenários
    def test_listar_cenarios(self):
        cenarios = ['Login com sucesso', 'Cadastro com email inválido']
        with patch('sys.stdout', new=StringIO()) as output:
            listar_cenarios(cenarios)
        out = output.getvalue()
        self.assertIn('1. Login com sucesso', out)
        self.assertIn('2. Cadastro com email inválido', out)

    # Testa a deleção de um cenário com índice válido
    def test_deletar_cenario_valido(self):
        cenarios = ['Login', 'Logout']
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_cenario(cenarios)
        self.assertEqual(cenarios, ['Logout'])
        self.assertIn('🗑️ Cenário', output.getvalue())

    # Testa tentativa de deletar com um número fora do intervalo
    def test_deletar_cenario_numero_invalido(self):
        cenarios = ['Ação de compra']
        with patch('builtins.input', return_value='10'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_cenario(cenarios)
        self.assertEqual(cenarios, ['Ação de compra'])  # Nada deve ser removido
        self.assertIn('❌ Número inválido.', output.getvalue())

    # Testa a tentativa de deletar com uma entrada não numérica
    def test_deletar_cenario_input_nao_numerico(self):
        cenarios = ['Cadastro']
        with patch('builtins.input', return_value='abc'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_cenario(cenarios)
        self.assertEqual(cenarios, ['Cadastro'])
        self.assertIn('❌ Entrada inválida.', output.getvalue())

    # Testa a tentativa de deletar usando um índice negativo
    def test_deletar_cenario_indice_negativo(self):
        cenarios = ['Busca por produto', 'Filtro por categoria']
        with patch('builtins.input', return_value='-1'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_cenario(cenarios)
        self.assertEqual(cenarios, ['Busca por produto', 'Filtro por categoria'])
        self.assertIn("❌ Número inválido.", output.getvalue())

    # Testa a adição de um cenário com caracteres especiais
    def test_adicionar_cenario_com_caractere_especial(self):
        cenarios = []
        with patch('builtins.input', return_value='Teste de segurança: SQL Injection #42'):
            with patch('sys.stdout', new=StringIO()) as output:
                adicionar_cenario(cenarios)
        self.assertIn('Teste de segurança: SQL Injection #42', cenarios)
        self.assertIn("✅ Cenário adicionado com sucesso!", output.getvalue())

# Executa os testes se o arquivo for rodado diretamente
if __name__ == '__main__':
    unittest.main()
