import os

FILENAME = 'data.csv'

def load_data():
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data.append(line.strip().split(','))
    return data

def save_data(data):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for row in data:
            f.write(','.join(row) + '\n')

def print_table(data):
    if not data:
        print("Таблица пуста.")
        return
    for i, row in enumerate(data):
        print(f"{i+1}. {', '.join(row)}")

def main():
    data = load_data()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Очистка консоли
        print("=== Интерфейс редактирования таблицы ===")
        print_table(data)
        print("\nВыберите действие:")
        print("1. Добавить строку")
        print("2. Удалить строку")
        print("3. Выход и сохранение")

        choice = input("> ")

        if choice == '1':
            # Добавление строки: вводим три пункта через запятую
            new_row = input("Введите три пункта через запятую: ").split(',')
            if len(new_row) == 3:
                data.append([item.strip() for item in new_row])
                print("Строка добавлена.")
            else:
                print("Ошибка: введено неверное количество пунктов.")
            input("\nНажмите Enter для продолжения...")

        elif choice == '2':
            if not data:
                print("В таблице нет строк для удаления.")
            else:
                print_table(data)
                try:
                    index = int(input("Введите номер строки для удаления: ")) - 1
                    if 0 <= index < len(data):
                        removed = data.pop(index)
                        print(f"Удалена строка: {', '.join(removed)}")
                    else:
                        print("Неверный номер строки.")
                except ValueError:
                    print("Введите число.")
            input("\nНажмите Enter для продолжения...")

        elif choice == '3':
            save_data(data)
            print("Изменения сохранены. До свидания!")
            break

if __name__ == "__main__":
    main()
