def exists_word(word, instance):
    search = []

    for index in range(len(instance)):
        file = instance.search(index)
        line = 0

        output = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for item in file["linhas_do_arquivo"]:
            line += 1
            if word.lower() in item.lower():
                output["ocorrencias"].append({"linha": line})

        if output["ocorrencias"]:
            search.append(output)

    return search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
