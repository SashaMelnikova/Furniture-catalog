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
