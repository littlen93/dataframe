import pandas as pd
import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)

# data присваиваю dataFrame
data = pd.DataFrame({"whoAmI": lst})

# data2 повторно присваиваю dataFrame, чтобы в дальнейшем провести сравнение
data2 = pd.DataFrame({"whoAmI": lst})

# Делаю новую pandas'скую выборку с названием 'whoAmI_human' в data2
data2.loc[data2["whoAmI"] == "human", "whoAmI_human"] = True
data2.loc[data2["whoAmI"] != "human", "whoAmI_human"] = False
data2.loc[data2["whoAmI"] == "robot", "whoAmI_robot"] = True
data2.loc[data2["whoAmI"] != "robot", "whoAmI_robot"] = False


# удаляю pandas'скую выборку 'whoAmI'
data2.pop("whoAmI")

# вывожу на экран dataFrame data2
print(data2)

# вывожу на экран dataFrame data с помощью get_dummies
res = pd.get_dummies(data, "whoAmI")
print(res)

# Сохраняю оба dataFrame в файлы, чтобы наглядно убедиться в файлах, что результат одинаковый
data2.to_csv("data2.csv")
res.to_csv("data1.csv")
