# 📌 Важно: файлы с тестами должны начинаться с test_ или заканчиваться на _test.py.
# Включи тесты в VS Code

Открой Command Palette → Ctrl+Shift+P.
Введи → Python: Configure Tests.
Выбери unittest.
Укажи папку, где лежат тесты (например, . или tests).



# 🔧 5. Возможные ошибки и решения
❌ ModuleNotFoundError: No module named 'task_functions'
➝ Проверь, что task_functions.py лежит в той же папке, что и тесты.
➝ Если в подпапке — нужно добавить __init__.py или поправить sys.path.

❌ ImportError: Failed to import test module
➝ Проверь имя файла (test_task_functions.py).


# Проверь запуск вручную В терминале запусти:
python -m unittest discover -s . -p "test_*.py"