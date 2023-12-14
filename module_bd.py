import os
import json

try:
    if not os.path.isdir("bd"):
        print("[OP-GOOSEBOT] База данных не найдена, процесс создания запущен!")
        os.mkdir("bd")
        os.chdir("bd")
        with open("bd.json", "w") as bd:
            bd.write("{\n}")
            print("[OP-GOOSEBOT] База данных успешно создана!")
    else:
        with open("bd/bd.json", "r") as bd:
            bd_list = json.load(bd)
            amount = len(bd_list.keys())

        print("[OP-GOOSEBOT] Подключение к Базе данных прошло успешно.")
        print(f"[OP-GOOSEBOT] Загружено пользователей: {amount}")
except:
    print("[OP-GOOSEBOT] Что-то пошло не так.")