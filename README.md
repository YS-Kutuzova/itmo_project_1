# ITMO first project - Flights programme

Проект предназначен для для работы с данными аэропортов, авиакомпаний и маршрутов,
содержащимися в базе данных. 
Он позволяет:  
- Загружать данные из CSV/(JSON-исходный формат).  
- Работать с данными напрямую из базы данных. 
- Просматривать данные авиаперелетов.  
- Находить рейсы по городу вылета.
- Находить рейсы по авиалинии.

## Установка  
1. Клонируйте репозиторий:  
   ```bash
   git clone https://github.com/YS-Kutuzova/itmo_project_1.git
2. Перейдите в папку проекта:
   cd itmo_project_1  
3. Создайте и активируйте виртуальное окружение: 
   python -m venv .venv  
   source .venv/bin/activate  # Linux/macOS  
   .\.venv\Scripts\activate   # Windows   
4. Установите зависимости:
   pip install -r requirements.txt  
5. Запустите проект:
   Menu_and_def.py
