from colorama import init, Fore, Back, Style

# инициализация библиотеки
init()

# пример использования атрибутов Fore и Back
print(Fore.RED + 'Красный текст' + Fore.RESET)
print(Back.GREEN + 'Зеленый фон' + Back.RESET)

# пример использования атрибута Style
print(Style.DIM + 'Текст с затемнением' + Style.RESET_ALL)

# пример использования нескольких атрибутов одновременно
print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + 'Желтый текст на синем фоне с ярким стилем' + Style.RESET_ALL
