# Catalog_app.py
Данный файл отвечает за обеспечение функциональности приложения и взаимедейстыия пользователя с ним.  
В нём создаётся класс `FurnitureCatalog`, который содержит в себе методы класса, отвечающие за подсоединение базы данных к файлу, осуществление фильтрации данных по SQL-запросам, вывод результатов.
## Методы класса
```
def __init__(self, db_path: str = "furniture.db"):
        self.db_path = db_path

def _db_connection(self):
        return sqlite3.connect(self.db_path)
```
Метод `def __init__` инициализирует путь к базе данных, а `def _db_connection` создаёт соединение к ней.
Далее идут методы, отвечающие за фильтрацию данных:
* **def get_catalog**
```
def get_catalog(self):
        with self._db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM furniture")
            return cursor.fetchall()
```
Получает весь каталог со всеми товарами.  
`cursor.execute("SELECT * FROM furniture")` - Выполняет SQL-запрос `SELECT`, которые выбирает все данные из таблицы.  
`return cursor.fetchall()` - Возвращает результаты запроса.  
Все методы класса, отвечающие за фильтрацию имеет одинаковую структуру, где отличаются только SQL-запросы, поэтому далее будут рассмотрены только они.
* **def search_furniture_by_available**
```
cursor.execute("SELECT * FROM furniture WHERE available = 1")
```
Выбирает только те строки, где в полях столбца `available` указано значение "1", т.е товар есть в наличии.
* **def search_furniture_by_category**
```
cursor.execute("SELECT * FROM furniture WHERE category = ?", (category,))
```
Выбирает только те строки, где поля столбца `category` соответсвуют запросу пользователя. Например только те товары, которые относятся к категории "Кровати".
* **def search_furniture_by_price**
```
cursor.execute("SELECT * FROM furniture WHERE price BETWEEN ? AND ?", (min_price, max_price))
```
Выбирает только те строки, где цена товара находится в указанном пользователем диапазоне.
* **search_furniture_by_material**
```
cursor.execute("SELECT * FROM furniture WHERE material LIKE ?", (f'%{material}%',))
```
Выбирает только те строки, где в материалах есть тот, который указан пользователем. Переменная `material` указана между знаком %, т.к в поле может через запятую быть указано несколько материалов, которые являетются целой строкой.
```
def display(self, furniture_list: List[tuple]):
        if not furniture_list:
            print("Мебель не найдена")
            return    
        print("\n" + "=" * 125)
        print(f"{'ID':<4} {'Название':<25} {'Категория':<15} {'Цена':<10} {'Материал':<25} {'Размер':<15} {'Цвет':<15} {'В наличии'}")
        print("="*125)
        for item in furniture_list:
            id, name, category, price, material, size, color, available = item
            available_text = "Да" if available else "Нет"
            print(f"{id:<4} {name:<25} {category:<15} {price:<10} {material:<25} {size:<15} {color:<15} {available_text}")
        print()
```
Оивечает за красивый вывод данных в консоль. Также если нет соотвествующего запросу пользователя результата, то программа сообщит об этом.
## Взаимодействие через консоль
```
catalog_app = FurnitureCatalog()
while(True):
    print("1 - Показать весь каталог\n"
          "2 - Показать мебель, которая есть в наличии\n"
          "3 - Поиск мебели по категории\n"
          "4 - Поиск мебели по диапазону цены\n"
          "5 - Поиск мебели по материалу\n"
          "6 - Выход\n")
    answer = int(input("Выберите действие: "))
    match(answer):
        case 1:
            furniture = catalog_app.get_catalog()
            catalog_app.display(furniture)
        case 2:
            furniture = catalog_app.search_furniture_by_available()
            catalog_app.display(furniture)
        case 3:
            category = input("Введите категорию: ")
            furniture = catalog_app.search_furniture_by_category(category)
            catalog_app.display(furniture)
        case 4:
            min_price = int(input("Минимальная цена: "))
            max_price = int(input("Максимальная цена: "))
            furniture = catalog_app.search_furniture_by_price(min_price, max_price)
            catalog_app.display(furniture)
        case 5:
            material = input("Введите название материала: ")
            furniture = catalog_app.search_furniture_by_material(material)
            catalog_app.display(furniture)
        case 6:
            print("Выход из программы")
            break
```
Обеспечивает взаимодействие пользователя с программой через консоль, где посредством ввода человек выбирает необходимую ему фукнкцию.
