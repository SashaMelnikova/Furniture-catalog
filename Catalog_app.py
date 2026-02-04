import sqlite3
from typing import List

class FurnitureCatalog:
    def __init__(self, db_path: str = "furniture.db"):
        self.db_path = db_path

    def _db_connection(self):
        return sqlite3.connect(self.db_path)
    
    def get_catalog(self):
        with self._db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM furniture")
            return cursor.fetchall()
        
    def search_furniture_by_available(self):
        with self._db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM furniture WHERE available = 1")
            return cursor.fetchall()
        
    def search_furniture_by_category(self, category: str):
        with self._db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM furniture WHERE category = ?", (category,))
            return cursor.fetchall()
        
    def search_furniture_by_price(self, min_price: int, max_price: int):
        with self._db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM furniture WHERE price BETWEEN ? AND ?", (min_price, max_price))
            return cursor.fetchall()
        
    def search_furniture_by_material(self, material):
        with self._db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM furniture WHERE material LIKE ?", (f'%{material}%',))
            return cursor.fetchall()
    
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