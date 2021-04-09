import os
import piexif
import shutil

# Получаем список фотографий из указанной папки
# Папка должна лежать рядом с этим скриптом
directory = input('Скопируйте сюда путь к фото. Например: D:/Новая папка/')


files = os.listdir(directory)
files2 = filter(lambda x: x.endswith('.jpg') or x.endswith('.JPG'), files)
os.chdir(directory)

# Перебираем каждый файл из списка фото и вытаскиваем из его EXIF дату фотографирования
for x in files2:
    print(x)
    # Проверяем чтобы файл не был папкой
    if (os.path.isdir(x) == False):
        try:
            picture = piexif.load(x)
        except Exception:
            qq = None
        else:
            qq = None

            for i in ("0th", "Exif", "GPS", "1st"):
                for tag in picture[i]:
                    # Нам нужны EXIF теги DateTime и DateTimeOriginal
                    if ((piexif.TAGS[i][tag]["name"] == "DateTime") or (
                    (piexif.TAGS[i][tag]["name"] == "DateTimeOriginal"))):
                        qq = picture[i][tag]

        if (qq == None):
            # Еcли в EXIF нет даты то имя папки будет 0000
            # В нее будут складываться фотки без даты в EXIF
            g = "0000-00-00"
        else:
            qq = qq.decode("utf-8")
            qq = qq[0:7]
            qq = qq.replace(":", "-")
            g = qq

        z = g[5:7]

        # Заменяем цифры месяца на его название
        if (z == "01"):
            zz = "январь"
        elif (z == "02"):
            zz = "февраль"
        elif (z == "03"):
            zz = "март"
        elif (z == "04"):
            zz = "апрель"
        elif (z == "05"):
            zz = "май"
        elif (z == "06"):
            zz = "июнь"
        elif (z == "07"):
            zz = "июль"
        elif (z == "08"):
            zz = "август"
        elif (z == "09"):
            zz = "сентябрь"
        elif (z == "10"):
            zz = "октябрь"
        elif (z == "11"):
            zz = "ноябрь"
        elif (z == "12"):
            zz = "декабрь"
        else:
            zz = "no"

        g = g[0:5] + zz

        if (os.path.exists(g) != True):
            # Если папки не существует создаем ее
            os.mkdir(g)
        # Копируем фотку в папку и удаляем оригинал
        shutil.copyfile(x, g + "/" + x)
        os.remove(x)