import xlsxwriter
from less_01 import array


def writer(parametr):
    # Создаеться фаил ЕХЕЛ.
    book = xlsxwriter.Workbook(r"D:\Lan-Python\Project\Parsing-Scraping\BfS4_Requ\data.xlsx")
    # Создаеться страница нашей таблици.
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    # Задаем ширину колонок.
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    # Итерируем данные по колонкам записывая данные по координатам.
    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1
    book.close()

writer(array)
