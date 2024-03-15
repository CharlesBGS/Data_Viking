
# Pesquisei como criar vários arquivos .py de uma vez para facilitar minha jornada após criar 10 arquivos manualmente.

# Importar a biblioteca necessária OS:
import os

# Definir o Diretório onde os arquivos serão criados:
diretorio = "./"

# Verificar se o diretório existe, caso não existir, cria-lo:
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Cria os 40 arquivos vazios
for i in range(11, 51):
    nome_arquivo = f"Exerc_{i}.py"
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_arquivo, "w") as arquivo:
        pass  # Arquivo vazio

print("Arquivos criados com sucesso!")

'''
Explicação do código passo a passo:

1. Importando o módulo os: 'import os'

import os

    - O módulo 'os' fornece funções para interagir com o sistema operacional, como manipulação de arquivos e diretórios.

2. Definindo o diretório onde os arquivos serão criados: diretorio = "./arquivos_python"

diretorio = "./arquivos_python"

    - Neste caso, estamos definindo o diretório como "arquivos_python", que será criado no diretório atual.
    - Como eu queria criar os arquivos diretamente no diretório em que já estava, usei "./".

3. Verificando se o diretório existe e criando-o, se necessário:

if not os.path.exists(diretorio):
    os.makedirs(diretorio)
    
    - 'os.path.exists(diretorio)' verifica se o diretório especificado já existe.
    - 'os.makedirs(diretorio)' cria o diretório se ele não existir.

4. Criando os arquivos:

for i in range(11, 51):
    nome_arquivo = f"Exerc_{i}.py"
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_arquivo, "w") as arquivo:
        pass  # Arquivo vazio

    - O 'loop' for percorre os números de 11 a 50 (inclusive).
    - Para cada número 'i', o nome do arquivo é criado usando uma f-string (f"Exerc_{i}.py"), onde '{i}' é substituído pelo valor atual de 'i'.
    - 'os.path.join(diretorio, nome_arquivo)' é usado para criar o caminho completo do arquivo, combinando o diretório e o nome do arquivo.
    - 'open(caminho_arquivo, "w")' abre o arquivo no modo de escrita ("w"), criando-o se ainda não existir.
    - 'with' é usado para garantir que o arquivo seja fechado corretamente após a conclusão das operações.
    - 'pass' é usado como placeholder dentro do bloco 'with' para indicar que o arquivo está vazio.

5. Mensagem de confirmação:

print("Arquivos criados com sucesso!")
    - Uma mensagem simples para indicar que a criação dos arquivos foi concluída com sucesso.

'''