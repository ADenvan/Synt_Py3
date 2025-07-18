# /Projects/
# ├── project_a/
# │   └── main.py            ← Вы запускаете этот файл
# └── project_b/
#     └── mylib/
#         └── tools.py       ← Вы хотите импортировать его

# Импортируем библиотеки Python
import sys      # для работы со списком путей поиска модулей
import os       # для работы с путями на диске

# Получаем абсолютный путь до папки, где лежит нужный модуль
# Предположим, проект_b находится на один уровень выше project_a
# То есть: /Projects/project_a/main.py
#          /Projects/project_b/mylib/tools.py

# Шаг 1: получаем путь до project_b
project_b_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'project_b'))

# Шаг 2: добавляем этот путь в sys.path — список, где Python ищет модули
if project_b_path not in sys.path:
    sys.path.append(project_b_path)

# Теперь можно импортировать модуль
from mylib import tools

# Пример использования
tools.paly()


"""project_b_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'project_b')
)
🔍 Что делает эта строка по шагам:

__file__ — это путь до текущего файла (main.py).

os.path.dirname(__file__) — получаем папку, где находится main.py, то есть /Projects/project_a.

os.path.join(..., '..', 'project_b') — переходим на уровень выше (..) и добавляем project_b, получаем /Projects/project_b.

os.path.abspath(...) — преобразуем в абсолютный путь: C:/Users/.../Projects/project_b.
"""

"""if project_b_path not in sys.path:
    sys.path.append(project_b_path)
→ Мы добавляем путь к project_b в sys.path, если он ещё не добавлен. Теперь Python будет искать модули и в этой папке.
"""
# ⚠️ Важно:
# В папке mylib/ должен быть файл __init__.py (даже пустой). Это нужно, чтобы Python понял, что это модуль.

# Пример:

# markdown
# Copy
# Edit
# project_b/
# └── mylib/
#     ├── __init__.py   ← даже если пустой
#     └── tools.py