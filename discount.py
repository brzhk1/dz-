cost = input("Введите цену товара ")
skidka = input("Введите размер скидки в % ")
skidka_1 = (int(cost) / 100) * int(skidka)
print("Окончательная сумма = ", skidka_1)
