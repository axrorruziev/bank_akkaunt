name1 =input("введите свое имя")
name2 =input("введите свое имя")
print("ну что готовы-начинаем нашу игру")
player1 = input("введите /камень/ножницы/бумага/")
player2 = input("введите /камень/ножницы/бумага/")
if player1 =="камень" and player2 == "ножницы":
    print(f"поздравляем {name1} вы выграли!!!!")
elif player1 =="камень" and player2 =="бумага":
    print(f"поздравляем {name2} вы выграли!!!!")
elif player2 == "камень" and player1 == "ножницы":
    print(f"поздравляем {name2} вы выграли!!!!")
elif player2 == "камень" and player1 == "бумага":
    print(f"поздравляем {name1} вы выграли!!!!")
elif player1 == "камень" and player2 == "камень":
    print(" у вас ничья !!!!")
elif player2 == "ножницы" and player1 == "ножницы":
    print(" у вас ничья !!!!")
elif player2 == "бумага" and player1 == "бумага":
    print("у вас ничья !!!!")




