from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)

    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(output)

    print(output)

    return output


def remove(instance):
    if not instance or len(instance) == 0:
        return print("Não há elementos")

    file = instance.dequeue()

    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        print(search)
    except IndexError:
        sys.stderr.write("Posição inválida")
