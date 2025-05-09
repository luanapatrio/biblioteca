
titulos = []
autores = []
quantidades = []
emprestados = []

while True:
    print("\nSeja bem-vindo ao sistema de biblioteca virtual!!")
    print("1. Cadastrar livro")
    print("2. Buscar livro")
    print("3. Realizar empréstimo")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        quantidade = int(input("Quantidade: "))

        titulos.append(titulo)
        autores.append(autor)
        quantidades.append(quantidade)
        emprestados.append(0)

        print("Livro cadastrado!")

    elif opcao == "2":
        busca = input("Digite o título ou autor do livro: ").lower()
        encontrado = False

        for i in range(len(titulos)):
            if busca in titulos[i].lower() or busca in autores[i].lower():
                print(f"\nTítulo: {titulos[i]}")
                print(f"Autor: {autores[i]}")
                print(f"Disponível: {quantidades[i] - emprestados[i]}")
                encontrado = True

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "3":
        titulo_busca = input("Título para empréstimo: ")
        if titulo_busca in titulos:
            i = titulos.index(titulo_busca)
            if emprestados[i] < quantidades[i]:
                emprestados[i] += 1
                print("Empréstimo realizado!")
            else:
                print("Nenhum livro disponível.")
        else:
            print("Livro não encontrado.")

    elif opcao == "4":
        print("Saindo do sistema da biblioteca virtual.")
        break

    else:
        print("Opção inválida.")
