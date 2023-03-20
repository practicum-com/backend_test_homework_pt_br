import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['program.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in dir_files, f"O arquivo `{filename}` não foi encontrado na raiz do repositório"

    try:
        import program
    except Exception as e:
        assert False, (
            'Falha na execução de `program.py`. '
            'Corrija os erros:\\n'
            f'{e}'
        )
