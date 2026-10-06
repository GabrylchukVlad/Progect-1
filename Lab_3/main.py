catalog = {
    1: {"name": "Ноутбук", "price": 25000, "stock": 5},
    2: {"name": "Мишка", "price": 450, "stock": 12},
    3: {"name": "Клавіатура", "price": 1200, "stock": 8},
    4: {"name": "Навушники", "price": 899.99, "stock": 15},
    5: {"name": "Монітор", "price": 6800, "stock": 3},
}
cart = {}
admin = "admin"
format_price = lambda price: f"{price:.2f}грн"

def help():
    print("Доступні команди:")
    print("1 - Показати каталог товарів")
    print("2 - Додати товар до кошика")
    print("3 - Видалити товар з кошика")
    print("4 - Оформити замовлення")
    print("5 - Зайти в профіль адміністратора")
    print("6 - Показати підказку")

def main():
    help()
    while True:
        choice = input("Виберіть дію(Для підказки введіть '6'): ")
        if choice == "1":
            print("Каталог товарів:")
            for item_id, item in catalog.items():
                print(f"{item_id}. {item['name']} - {format_price(item['price'])}")

        elif choice == "2":
            take = int(input("Введіть ID товару, який хочете додати до кошика(1-5): "))
            if take in catalog:
                item = catalog[take]
                if item["stock"] > 0:
                    cart[take] = cart.get(take, 0) + 1
                    item["stock"] -= 1
                    print(f"Товар {item['name']} додано до кошика.")
                else:
                    print("Товару немає в наявності.")
            else:
                print("Введено невірний ID товару.")
                    
        elif choice == "3":
            delete = int(input("Введіть ID товару, який хочете видалити з кошика(1-5): "))
            if delete in cart and cart[delete] > 0:
                cart[delete] -= 1
                catalog[delete]["stock"] += 1
                if cart[delete] == 0:
                    del cart[delete]
                print(f"Товар {catalog[delete]['name']} видалено з кошика.")
            else:
                print("Товару немає в кошику.")
        
        elif choice == "4":
            print("Замовлення оформлено. Дякуємо за покупку!")
            cart.clear()
            
        elif choice == "5":
            password = input("Введіть пароль адміністратора: ")
            if password == admin:
                print("Ви увійшли в профіль адміністратора.")
                print("Товари:")
                for item_id, item in catalog.items():
                    print(f"{item_id}. {item['name']} - {format_price(item['price'])} - В наявності: {item['stock']}")
            else:
                print("Невірна пароль.")
        elif choice == "6":
            help()
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            
if __name__ == "__main__":
    main()
