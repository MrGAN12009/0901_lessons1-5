from getpass import getpass

from models import User, Product, Order
from database import Database

def show_products():
    products = Product.get_all()
    if not products:
        print("Продуктов в БД не найдено!")
        return
    
    print("\nСписок продуктов:")
    for product in products:
        print(f"{product.id}. {product.name} - {product.price}")
    print('-'*50)
    
def show_orders():
    orders = Order.get_all()
    if not orders:
        print("Заказов не найдено!")
        return
    
    print("\nЗаказы:")
    for order in orders:
        print(f"{order.id}. Пользователь user_id:{order.user_id} купил товар #{order.product_id}")
    print('-'*50)



def user_menu(user: User):
    while True:
        print("1. Посмотреть товары.")
        print("2. Сделать заказ")
        print("0. Выйти")

        choice = input(">")

        if choice == "1":
            show_products()

        elif choice == "2":
            show_products()
            product_id = input("Введите id продукта> ")
            Order.create(user.id, product_id)
            print("Заказ создан!")
        
        elif choice == "0":
            print("Завершение работы системы...")
            break
        
        else:
            print("Я не знаю такого варианта, выберите из перечисленных ниже вариантов:")
            continue

def admin_menu():
    while True:
        print("1. Посмотреть товары.")
        print("2. Добавить продукт")
        #не реализована логика
        print("3. Просмотр заказов")
        print("0. Выйти")

        choice = input(">")

        if choice == "1":
            show_products()

        elif choice == "2":
            name = input("ВВедите название продукта: ")
            price = input("Введите цену продукта: ")
            try:
                float(price)
            except ValueError:
                print("В цене не должно быть букв!")
                continue
            Product.create(name, float(price))
            print("Продукт успешно добавлен!")
        
        elif choice == "3":
            show_orders()
        
        elif choice == "0":
            print("Завершение работы системы...")
            break
        
        else:
            print("Я не знаю такого варианта, выберите из перечисленных ниже вариантов:")
            continue 

def main():
    print("==ВХОД==")
    username = input("ВВедите ваш логин: ")
    password = getpass("Введите ваш пароль: ")

    user = User.login(username, password)

    if not user:
        print("Неверный логин или пароль!")
        return
    
    print(f"Добро пожаловать, {user.username} ({user.role})")

    if user.role == "admin":
        admin_menu()
    else:
        user_menu(user)


if __name__ == '__main__':
    main()