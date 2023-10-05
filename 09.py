import sys

def encontrar_funcoes_sem_comentario(arquivo):
    with open(arquivo, 'r') as arquivo_fonte:
        linhas = arquivo_fonte.readlines()

    funcao_atual = None
    funcoes_sem_comentario = []

    for numero_linha, linha in enumerate(linhas, start=1):
        if linha.startswith('def '):
            funcao_atual = linha.strip().split(' ')[1].split('(')[0]

            linha_anterior_funcao = linhas[numero_linha - 2]

            if not linha_anterior_funcao.startswith('#'):
                if funcao_atual is not None:
                    funcoes_sem_comentario.append((funcao_atual, arquivo, numero_linha))
                    funcao_atual = None

    return funcoes_sem_comentario

def main():
    if len(sys.argv) < 2:
        print("Uso: python programa.py arquivo1.py arquivo2.py ...")
        sys.exit(1)

    arquivos = sys.argv[1:]

    for arquivo in arquivos:
        print(arquivo)
        try:
            funcoes_sem_comentario = encontrar_funcoes_sem_comentario(arquivo)
            if funcoes_sem_comentario:
                print(f"Funções sem comentários em '{arquivo}':")
                for funcao, arquivo, linha in funcoes_sem_comentario:
                    print(f"  - {funcao}, arquivo: {arquivo}, linha: {linha}")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{arquivo}' não existe.")
        except IOError:
            print(f"Erro ao abrir o arquivo '{arquivo}'.")

main()