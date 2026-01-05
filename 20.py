shopping_list = []

while True:
    choice = input("add / remove / show / quit: ")

    if choice == "add":
        item = input("Item: ")
        shopping_list.append(item)

    elif choice == "remove":
        item = input("Item: ")
        if item in shopping_list:
            shopping_list.remove(item)

    elif choice == "show":
        print(shopping_list)

    elif choice == "quit":
        break

