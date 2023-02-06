from ting_file_management.file_management import txt_importer


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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
