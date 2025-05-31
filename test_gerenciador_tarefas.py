import unittest
from unittest.mock import patch
from io import StringIO

# Importa as funções diretamente do script se ele for modularizado
# Aqui estamos assumindo que você salvou o código anterior em um arquivo chamado `gerenciador.py`
from gerenciador import adicionar_tarefa, listar_tarefas, deletar_tarefa

class TestGerenciadorTarefas(unittest.TestCase):

    def test_adicionar_tarefa(self):
        tarefas = []
        with patch('builtins.input', return_value='Estudar Python'):
            with patch('sys.stdout', new=StringIO()) as output:
                adicionar_tarefa(tarefas)
        self.assertIn('Estudar Python', tarefas)
        self.assertIn('✅ Tarefa adicionada com sucesso!', output.getvalue())

    def test_adicionar_tarefa_vazia(self):
        tarefas = []
        with patch('builtins.input', return_value='   '):
            with patch('sys.stdout', new=StringIO()) as output:
                adicionar_tarefa(tarefas)
        self.assertEqual(tarefas, [])
        self.assertIn('⚠️ Tarefa vazia não pode ser adicionada.', output.getvalue())

    def test_listar_tarefas(self):
        tarefas = ['Lavar louça', 'Estudar']
        with patch('sys.stdout', new=StringIO()) as output:
            listar_tarefas(tarefas)
        out = output.getvalue()
        self.assertIn('1. Lavar louça', out)
        self.assertIn('2. Estudar', out)

    def test_deletar_tarefa_valida(self):
        tarefas = ['Lavar louça', 'Estudar']
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_tarefa(tarefas)
        self.assertEqual(tarefas, ['Estudar'])
        self.assertIn('🗑️ Tarefa', output.getvalue())

    def test_deletar_tarefa_invalida(self):
        tarefas = ['Tarefa 1']
        with patch('builtins.input', return_value='10'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_tarefa(tarefas)
        self.assertEqual(tarefas, ['Tarefa 1'])
        self.assertIn('❌ Número inválido.', output.getvalue())

    def test_deletar_tarefa_input_invalido(self):
        tarefas = ['Tarefa 1']
        with patch('builtins.input', return_value='abc'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_tarefa(tarefas)
        self.assertEqual(tarefas, ['Tarefa 1'])
        self.assertIn('❌ Entrada inválida.', output.getvalue())
   
    def test_deletar_tarefa_com_indice_negativo(self):
        tarefas = ['Estudar', 'Ler livro']
        with patch('builtins.input', return_value='-1'):
            with patch('sys.stdout', new=StringIO()) as output:
                deletar_tarefa(tarefas)
        self.assertEqual(tarefas, ['Estudar', 'Ler livro'])  # Nenhuma tarefa removida
        self.assertIn("❌ Número inválido.", output.getvalue())

    def test_adicionar_tarefa_com_caractere_especial(self):
        tarefas = []
        with patch('builtins.input', return_value='Revisar código @ 23h!'):
            with patch('sys.stdout', new=StringIO()) as output:
                adicionar_tarefa(tarefas)
        self.assertIn('Revisar código @ 23h!', tarefas)
        self.assertIn("✅ Tarefa adicionada com sucesso!", output.getvalue())

if __name__ == '__main__':
    unittest.main()
