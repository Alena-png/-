import random
words = ["окрас", "козёл", "кит", "лошадь", "лосось", "компьютер", "улитка", "предок", "лось", "калория", "цвет", "родитель", "глаз", "орган", "преподаватель", "учитель", "ошибка", "старт", "финиш", "шифр", "цифра", "порядок", "запятая", "улыбка", "точка", "конец", "рассказ"]
word = random.choice(words)
shifr = len(word) * "*"
print(shifr)
jizn = 3
a = 0
while shifr != word:
    bukva = input()
    if bukva in word:
        n = word.index(bukva)
        shifr = shifr[:n] + bukva + shifr[n+1:]
        print(shifr)
    else:
        jizn -= 1
        a += 1
        print(shifr)
        if a == 1:
            print("_______________________________________",
                  "___$$$$$$$$$$________♥♥ _______________",
                  "___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___",
                  "______|___________________$$$$$$$______",
                  "______|___________________$$$$$$$______",
                  "______|___________________$$$$$$$______",
                  "_____$$$__________________$$$$$$$______",
                  "____$$$$$_________________$$$$$$$______",
                  "_____$$$__________________$$$$$$$______",
                  "___$$$$$$$________________$$$$$$$______",
                  "_________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "_______________________$$$$$$$$$$$$$___",
                  "____________$$$$$$$$$$$$$$$$$$$$$$$$$$$",
                  "___________________$$$$$$$$$$$$$$$$$$$$",
                  "___________________$$$$$$$$$$$$$$$$$$$$",
                  "__________________$$$$$$$$$$$$$$$$$$$$$",
                  "__________________$$$$$$$$$$$$$$$$$$$$$", sep="\n")
        if a == 2:
            print("_______________________________________",
                  "___$$$$$$$$$$________♥  _______________",
                  "___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___",
                  "______|___________________$$$$$$$______",
                  "______|___________________$$$$$$$______",
                  "______|___________________$$$$$$$______",
                  "_____$$$__________________$$$$$$$______",
                  "____$$$$$_________________$$$$$$$______",
                  "_____$$$__________________$$$$$$$______",
                  "___$$$$$$$________________$$$$$$$______",
                  "__$$$$$$$$$_______________$$$$$$$______",
                  "__$_$$$$$_$_______________$$$$$$$______",
                  "__$_$$$$$_$_______________$$$$$$$______",
                  "__$_$$$$$_$_______________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "__________________________$$$$$$$______",
                  "_______________________$$$$$$$$$$$$$___",
                  "____________$$$$$$$$$$$$$$$$$$$$$$$$$$$",
                  "___________________$$$$$$$$$$$$$$$$$$$$",
                  "___________________$$$$$$$$$$$$$$$$$$$$",
                  "__________________$$$$$$$$$$$$$$$$$$$$$",
                  "__________________$$$$$$$$$$$$$$$$$$$$$", sep="\n")
        if jizn == 0:
            print(  "_______________________________________",
                    "___$$$$$$$$$$________   _______________",
                    "___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___",
                    "______|___________________$$$$$$$______",
                    "______|___________________$$$$$$$______",
                    "______|___________________$$$$$$$______",
                    "_____$$$__________________$$$$$$$______",
                    "____$$$$$__Вы-Проиграли___$$$$$$$______",
                    "_____$$$__________________$$$$$$$______",
                    "___$$$$$$$________________$$$$$$$______",
                    "__$$$$$$$$$_______________$$$$$$$______",
                    "__$_$$$$$_$_______________$$$$$$$______",
                    "__$_$$$$$_$_______________$$$$$$$______",
                    "__$_$$$$$_$_______________$$$$$$$______",
                    "____$$_$$_________________$$$$$$$______",
                    "___$$___$$________________$$$$$$$______",
                    "___$$___$$________________$$$$$$$______",
                    "___$$___$$_____________$$$$$$$$$$$$$___",
                    "___$$___$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$",
                    "___________________$$$$$$$$$$$$$$$$$$$$",
                    "___________________$$$$$$$$$$$$$$$$$$$$",
                    "__________________$$$$$$$$$$$$$$$$$$$$$",
                    "__________________$$$$$$$$$$$$$$$$$$$$$", sep="\n")
            break
    if shifr == word:
        print(  "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠔⠈⠁⠄⠒⠢⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣀⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡠⠖⠉⠁⠄⠄⠄⠈⠉⠒⢤⡀⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⢠⠎⠄⠄⠄⠄⠄⢸⣆⠄⠄⢻⡆⠙⣆⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⢠⡇⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⣷⠄⠘⡄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⣿⠄⠄⡇⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠘⡆⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⢰⡟⠄⢠⠇⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠙⣄⠄⢀⠄⠄⠄⣸⠇⠄⠄⡿⠁⢠⠏⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠓⢤⣉⠁⠄⠄⠄⠄⣀⡤⠞⠁⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣽⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡌⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡘⢠⠁⡆⠄Вы-Выиграли⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⠁⢸⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⠸⠄⢃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠇⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⡆⠄⠈⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⡇⠄⠄⢃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⡇⠄⠄⠘⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⡟⡄⠄⠄⢣⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⠄⢰⠁⠈⠄⠄⠌⠑⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⣸⢰⢌⡘⠄⠄⠘⠄⠚⢿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠹⠸⠄⠇⠄⠄⠄⠘⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠘⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⠄⠄⠄⠄⠄⢇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠄⡘⠄⠄⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⢰⠁⠄⠄⠄⠄⠄⠄⠄⠈⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠄⠆⠄⠄⠄⠄⠄⠄⠄⠄⠄⢡⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⣼⣤⣤⣄⠄⠄⠄⠄⠄⠄⠄⠘⠿⠿⠷⠄⠄⠄⠄⠄⠄⠄⠄",
                "⠄⠄⠄⠄⠄⠄⠄⠉⠛⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄", sep="\n")
